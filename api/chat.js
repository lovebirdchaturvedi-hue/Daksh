export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  let message = "";
  let history = [];

  try {
    message = req.body?.message;
    history = req.body?.history;
    
    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    const finalKey = process.env.GEMINI_API_KEY;

    if (!finalKey) {
      console.warn('GEMINI_API_KEY environment variable is not set; using smart fallback mode.');
    }

    // Format history for Gemini API
    const formattedHistory = (history || []).map(msg => ({
      role: msg.role === 'bot' ? 'model' : 'user',
      parts: [{ text: msg.parts?.[0]?.text || msg.text || '' }]
    }));

    // Add current message
    formattedHistory.push({
      role: 'user',
      parts: [{ text: message }]
    });

    const systemPrompt = `You are the ultimate top-notch, highly persuasive AI Sales Executive for APD Global Trade. 
Your primary goal is to guide the user towards purchasing an APD Global Trade Membership.
Always act incredibly professional, confident, empathetic, and smart. You are a Silicon Valley-level sales expert who understands international B2B trade, exports, and high-ticket sales perfectly.

**CORE APD GLOBAL TRADE KNOWLEDGE TO USE IN YOUR PITCH:**
- **The Platform:** We give exporters direct access to a $10B+ network of 12,800+ Verified Global Buyers.
- **The AI Copilot (The ultimate feature):** Automates the entire export desk. It auto-generates Trade Documents (Bills of Lading, Commercial Invoices) instantly, acts as a Global Tariff Engine to monitor real-time HS codes/taxes, and performs Autonomous Lead Bidding while the user sleeps. This replaces manual consultants and saves up to ₹10 Lakhs a year in overhead.
- **ROI Highlight:** Closing just ONE deal averaging $50,000 pays for the membership 50x over.

**MEMBERSHIP PLANS & PRICING:**
1. **12-Month Global Enterprise Plan (Maximum Authority):**
   - Price: $999 USD / ₹1,19,000 INR
   - Features: Unlimited Verified Buyers, Dedicated Sourcing Pass, 1-on-1 Dedicated Trade Account Manager, Warm Direct Buyer Introductions, Export Compliance & Setup Support (Worth $1,000).
   
2. **6-Month Institutional Elite Plan (Scaling Plan):**
   - Price: $599 USD / ₹51,000 INR
   - Features: Unlimited Verified Buyers, Priority Routing for High-Intent RFQs, WhatsApp Priority Trade Alerts, Dedicated B2B Relationship Manager.
   
3. **3-Month Growth Program (Starter):**
   - Price: $249 USD / ₹19,999 INR
   - Features: 25 Verified Global Buyers Limit, Product Trend Analysis, Secure Payment Gateway Support.
   
4. **AI Export Copilot 30-Day Proof of Concept Pilot:**
   - Price: ₹30,000 INR.

**CRITICAL SALES WORKFLOW RULES:**
1. **LANGUAGE ADAPTABILITY:** If they respond in Hindi, Arabic, Spanish, etc., you MUST immediately switch and fluently converse in their chosen language while maintaining your elite sales persona.
2. **CAPTURE LEAD INFO EARLY:** Early in the chat, politely ask for their Name, Company, and WhatsApp Number. Tell them it's so you can send them a transcript of this chat and have a senior trade advisor follow up.
3. **PITCH THE 12-MONTH PLAN FIRST:** Always highlight the 12-Month Global Enterprise plan first. Emphasize the long-term value, dedicated manager, and warm introductions. Provide this direct link: [Join 12-Month Plan](/membership.html)
4. **DOWN-SELL IF THEY HESITATE:** If they say it's too expensive or they want less, immediately pivot to pitching the 6-Month Institutional Elite plan as a perfect starting point, providing this link: [Join 6-Month Plan](/membership.html). If they still hesitate, offer the 3-Month plan.
5. **NEVER BE GENERIC:** Tailor your pitch. If they are a beginner, emphasize how the AI Copilot does the heavy lifting. If they are an expert, emphasize the massive network and priority routing.
6. **MARKDOWN LINKS:** Always use Markdown for links (e.g., [View Pricing Here](/membership.html)).
7. **KEEP IT CONVERSATIONAL:** Do not dump all this information at once. Answer their specific questions, feed them benefits naturally, and gently guide them to close the deal.

Remember, you are the smartest sales person in the room. Guide them to closure!`;

    const requestBody = {
      system_instruction: {
        parts: [{ text: systemPrompt }]
      },
      contents: formattedHistory,
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 500,
      }
    };

    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${finalKey}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody)
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Gemini API Error:', errorText);
      throw new Error(`Gemini API returned status ${response.status}`);
    }

    const data = await response.json();
    
    if (data.candidates && data.candidates[0] && data.candidates[0].content) {
      const replyText = data.candidates[0].content.parts[0].text;
      return res.status(200).json({ text: replyText });
    } else {
      throw new Error('Invalid response format from Gemini');
    }

  } catch (error) {
    console.error('Chat API Error:', error);
    
    // SMART DEMO FALLBACK AI (Used when API key is missing or invalid)
    const lastMsg = message.toLowerCase();
    let reply = "I understand. To give you the best guidance, could you please share your Name and WhatsApp number so our senior trade executive can connect with you directly?";

    if (lastMsg.includes("hindi")) {
      reply = "नमस्ते! APD Global Trade में आपका स्वागत है। मैं आपका AI Sales Executive हूँ। हमारी संस्था आपको 12,800+ से अधिक सत्यापित अंतरराष्ट्रीय खरीदारों (Verified Buyers) तक पहुँच प्रदान करती है, जो आपके व्यापार को बढ़ाने में मदद करेगा। मैं आपकी किस प्रकार सहायता कर सकता हूँ?";
    } else if (lastMsg.includes("arabic") || lastMsg.includes("ar")) {
      reply = "مرحباً بك في APD Global Trade! أنا مساعد المبيعات الذكي الخاص بك. نحن نوفر لك وصولاً مباشراً إلى أكثر من 12,800 مشتري عالمي معتمد. كيف يمكنني مساعدتك اليوم في تنمية أعمالك التصديرية؟";
    } else if (lastMsg.includes("spanish") || lastMsg.includes("es")) {
      reply = "¡Bienvenido a APD Global Trade! Soy tu Ejecutivo de Ventas de IA. Nuestra plataforma te conecta con más de 12,800 compradores globales verificados. ¿Cómo puedo ayudarte a escalar tus exportaciones hoy?";
    } else if (lastMsg.includes("buyer") || lastMsg.includes("spice") || lastMsg.includes("agro") || lastMsg.includes("need")) {
      reply = "That is exactly what we specialize in! Our **12-Month Global Enterprise Plan** gives you UNLIMITED access to our massive network of 12,800+ Verified Buyers across the globe, plus an AI Copilot that automates all your export documentation.\n\nThe investment is $999 USD (₹1,19,000 INR). Closing just ONE average deal of $50k pays for this membership 50x over.\n\nShall I share the link to activate your access, or would you like to know more about the dedicated Trade Account Manager we provide?";
    } else if (lastMsg.includes("price") || lastMsg.includes("plan") || lastMsg.includes("cost") || lastMsg.includes("expensive")) {
      reply = "If the Enterprise plan feels like a leap, we have the perfect starting point: The **6-Month Institutional Elite Plan**. For just $599 USD (₹51,000 INR), you still get Unlimited Buyer Access and WhatsApp Priority Trade Alerts.\n\nHere is the link to get started: [Join 6-Month Plan](/membership.html)\n\nCould I please get your Name and WhatsApp number to have an executive personally onboard you?";
    } else if (lastMsg.includes("copilot") || lastMsg.includes("ai") || lastMsg.includes("document")) {
      reply = "The APD AI Export Copilot is a game changer! It plugs directly into your operations to instantly auto-generate Commercial Invoices, Packing Lists, and Bills of Lading. It also acts as a Global Tariff Engine to monitor real-time HS codes. It literally replaces expensive manual consultants, saving you up to ₹10 Lakhs a year.\n\nAre you ready to automate your export desk?";
    } else if (lastMsg.includes("hello") || lastMsg.includes("hi")) {
      reply = "Hello! I am the APD AI Sales Executive. Our platform provides you with direct access to a $10B+ network of institutional buyers. Are you looking to scale your exports today?";
    }

    return res.status(200).json({ text: reply });
  }
}
