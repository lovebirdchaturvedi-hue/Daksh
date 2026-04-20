/**
 * APD Global Trade – Firebase Functions
 * MAIN ENTRY POINT (Optimized for Fast Initialization)
 */

const functions = require("firebase-functions");
const admin = require("firebase-admin");

// Optimized Initialization
admin.initializeApp();

// Lazy load Gemini for faster startup
let genAI = null;
const getGenAI = () => {
  if (!genAI) {
    const { GoogleGenerativeAI } = require("@google/generative-ai");
    genAI = new GoogleGenerativeAI("AIzaSyDwqwd8HY8FKHMsIveCPZXWJSBYtj0B6Is");
  }
  return genAI;
};

const SYSTEM_INSTRUCTION = `
You are the APD Global Trade Sales Assistant.
Key Facts: Over 1 Million+ verified RFQs and 5 Million+ high-quality Buyer leads.
Goal: Sell Membership. $250 Trial only if requested.
WhatsApp: +91 9266418868
`;

// 1. SALES BOT AI (onCall)
exports.salesBotChat = functions.https.onCall(async (data, context) => {
  const { message, history } = data;
  try {
    const ai = getGenAI();
    const model = ai.getGenerativeModel({ model: "gemini-pro" });
    const chat = model.startChat({
      history: history || [],
      generationConfig: { maxOutputTokens: 500 }
    });
    const result = await chat.sendMessage(SYSTEM_INSTRUCTION + "\n\nUser: " + message);
    const response = await result.response;
    return { text: response.text() };
  } catch (error) {
    console.error("Sales Bot Error:", error);
    return { error: "I'm having a little trouble connecting. Please try again!" };
  }
});

// 2. APPROVE SUPPLIER (onRequest)
exports.approveSupplier = functions.https.onRequest(async (req, res) => {
  try {
    const supplierId = req.query.supplierId;
    if (!supplierId) return res.status(400).json({ error: "supplierId required" });
    const ref = admin.firestore().collection("suppliers").doc(supplierId);
    await ref.update({ approved: true, approvedAt: admin.firestore.FieldValue.serverTimestamp() });
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// 3. SECURE CONTACT FORM (onCall)
exports.sendContactEmail = functions.https.onCall(async (data, context) => {
  const { name, email, subject, message } = data;
  
  if (!name || !email || !subject || !message) {
    throw new functions.https.HttpsError('invalid-argument', 'All fields are required.');
  }

  try {
    // A. Store in Firestore as Backup (Permanent Record)
    const ticketRef = admin.firestore().collection("contact_inquiries").doc();
    await ticketRef.set({
      id: ticketRef.id,
      name,
      email,
      subject,
      message,
      timestamp: admin.firestore.FieldValue.serverTimestamp(),
      status: 'new'
    });

    // B. Attempt Email Delivery
    const nodemailer = require("nodemailer");
    
    // We use environment config for SMTP
    const smtpUser = functions.config().smtp?.user;
    const smtpPass = functions.config().smtp?.pass;

    if (!smtpUser || !smtpPass) {
      console.warn("⚠️ SMTP Credentials missing in Firebase Config. Message stored in Firestore only.");
      return { success: true, message: "Inquiry registered. Live email pending SMTP configuration." };
    }

    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: { user: smtpUser, pass: smtpPass }
    });

    const mailOptions = {
      from: `"APD Support" <${smtpUser}>`,
      to: 'info@apdglobaltrade.com',
      replyTo: email,
      subject: `[WEB INQUIRY] ${subject}`,
      text: `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`,
      html: `<div style="font-family:sans-serif;padding:20px;">
                <h2 style="color:#D4AF37;">New Inquiry: ${subject}</h2>
                <p><strong>From:</strong> ${name} (${email})</p>
                <hr>
                <p style="white-space:pre-wrap;">${message}</p>
             </div>`
    };

    await transporter.sendMail(mailOptions);
    return { success: true, message: "Message transmitted successfully." };

  } catch (err) {
    console.error("Contact Form Error:", err);
    // We don't throw error to user if Firestore part worked
    return { success: true, message: "Inquiry received and logged for review." };
  }
});
