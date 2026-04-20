/**
 * Sales Bot Frontend Logic (Modular v9+ Version)
 * Integrated with APD Global Trade Platform
 */

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getFunctions, httpsCallable } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-functions.js";

const firebaseConfig = {
    apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
    authDomain: "apd-globaltrade-prod.firebaseapp.com",
    projectId: "apd-globaltrade-prod",
    storageBucket: "apd-globaltrade-prod.firebasestorage.app",
    messagingSenderId: "226407312435",
    appId: "1:226407312435:web:f8a54b1132af3899170746"
};

// Initialize self-contained Firebase for the bot
const app = initializeApp(firebaseConfig, "salesBotApp");
const functions = getFunctions(app, "us-central1"); // Hardcoded region for reliability

const SalesBot = {
    isOpen: false,
    history: [],
    handoffNumber: '919266418868',

    init() {
        this.renderWidget();
        this.addEventListeners();
        
        // Auto-open disabled per request
        /*
        setTimeout(() => {
            if (!this.isOpen) {
                this.toggleChat();
                this.addMessage("Hey, my name is Suhana! How can I help you today?", 'bot');
            }
        }, 3000);
        */
    },

    renderWidget() {
        if (document.getElementById('salesBot')) return;
        const widgetHTML = `
            <div class="sales-bot-widget" id="salesBot">
                <div class="bot-bubble" id="botBubble">
                    <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>
                </div>
                <div class="chat-window" id="chatWindow">
                    <div class="chat-header">
                        <div class="bot-info">
                            <span class="name">Suhana - APD Sales</span>
                            <span class="status">Online</span>
                        </div>
                        <button id="closeChat" style="background:none; border:none; color:white; font-size:1.5rem; cursor:pointer;">&times;</button>
                    </div>
                    <div class="chat-messages" id="chatMessages">
                        <!-- Messages will be injected here -->
                    </div>
                    <div class="chat-input-area">
                        <input type="text" class="chat-input" id="chatInput" placeholder="Type your message...">
                        <button class="send-btn" id="sendBtn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
                        </button>
                    </div>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', widgetHTML);
    },

    addEventListeners() {
        const bubble = document.getElementById('botBubble');
        const closeBtn = document.getElementById('closeChat');
        const sendBtn = document.getElementById('sendBtn');
        const input = document.getElementById('chatInput');

        bubble.onclick = () => this.toggleChat();
        closeBtn.onclick = () => this.toggleChat();
        sendBtn.onclick = () => this.sendMessage();
        input.onkeypress = (e) => { if (e.key === 'Enter') this.sendMessage(); };
    },

    toggleChat() {
        const window = document.getElementById('chatWindow');
        this.isOpen = !this.isOpen;
        window.classList.toggle('active', this.isOpen);
    },

    async sendMessage() {
        const input = document.getElementById('chatInput');
        const text = input.value.trim();
        if (!text) return;

        input.value = '';
        this.addMessage(text, 'user');

        try {
            const response = await this.callAI(text);
            this.addMessage(response, 'bot');

            if (response.toLowerCase().includes('whatsapp') || response.toLowerCase().includes('proceed') || response.toLowerCase().includes('contact')) {
                this.addWAHandoffButton("Chat with our Sales Team on WhatsApp");
            }

            this.history.push({ role: 'user', parts: [{ text }] });
            this.history.push({ role: 'model', parts: [{ text: response }] });

        } catch (error) {
            console.error(error);
            this.addMessage("I'm experiencing a slight connection issue, but you can chat with us directly on WhatsApp!", 'bot');
            this.addWAHandoffButton("Contact Support on WhatsApp");
        }
    },

    addMessage(text, sender) {
        const container = document.getElementById('chatMessages');
        const msg = document.createElement('div');
        msg.className = `msg ${sender}`;
        msg.innerText = text;
        container.appendChild(msg);
        container.scrollTop = container.scrollHeight;
    },

    addWAHandoffButton(label) {
        const container = document.getElementById('chatMessages');
        const btn = document.createElement('a');
        btn.href = `https://wa.me/${this.handoffNumber}?text=Hi, I was chatting with your AI Assistant. I'm interested in the Membership options for APD Global Trade.`;
        btn.target = "_blank";
        btn.className = "wa-handoff-btn";
        btn.innerText = `💬 ${label}`;
        container.appendChild(btn);
        container.scrollTop = container.scrollHeight;
    },

    async callAI(message) {
        const msg = message.toLowerCase();
        try {
            // Priority 1: Current Name (Force us-central1 as the standard for these projects)
            const salesBotChat = httpsCallable(functions, 'salesBotChat');
            let result;
            
            try {
                result = await salesBotChat({ message: message, history: this.history });
            } catch (innerError) {
                console.warn("salesBotChat failed, trying legacy salesBotAI...", innerError);
                const legacyBot = httpsCallable(functions, 'salesBotAI');
                result = await legacyBot({ message: message, history: this.history });
            }

            if (result.data && result.data.text) return result.data.text;
            if (result.data && result.data.error) throw new Error(result.data.error);

            throw new Error("Empty response from AI");
            
        } catch (error) {
            console.error("Firebase Function Error Final:", error);
            
            /* --- SUHANA HYPER-INTELLIGENCE (OFFLINE ENGINE) --- */
            
            // 0. Conversational Flow (Confirmation handlers)
            const isConfirmed = msg === 'yes' || msg.includes('yes ') || msg.includes(' sure') || msg.includes(' ok') || msg === 'yeah' || msg === 'yep';
            if (isConfirmed) {
                return "Excellent! I'll guide you. To see our Live Buyer RFQs and verify active demand for your product, simply click the **'View Live RFQs'** button on the home page or go to our **'Buyer RFQs'** menu. Should I walk you through how to unlock their contact details next?";
            }

            // 1. Export Inquiries
            if (msg.includes('export') || msg.includes('sell') || msg.includes('sending')) {
                return "We specialize in helping high-volume exporters like you reach verified global markets. Whether it's Grains, Agro, or Commodities, we have the buyer network ready. Would you like to start with a $250 trial to see one specific buyer's requirements immediately?";
            }

            // 2. Durations / Specific Offers
            if (msg.includes('month') || msg.includes('year') || msg.includes('6') || msg.includes('12')) {
                return "Our 6-month and Annual Institutional Memberships are the best way to get long-term trade benefits without commissions. For short-term verification, we also have the **$250 Ready-Buyer Trial**. Which one fits your current goal?";
            }

            // 3. Pricing / Plan Inquiries
            if (msg.includes('plan') || msg.includes('price') || msg.includes('cost') || msg.includes('how much') || msg.includes('fee') || msg.includes('trial') || msg.includes('pay')) {
                return "We have two main options: our **Full Institutional Membership** for high-volume scale (no commission), and a **$250 Ready-Buyer Trial**. The trial gives you immediate access to one verified buyer L/C and their requirements. Ready to see the link?";
            }
            
            // 4. Platform / What you do
            if (msg.includes('platform') || msg.includes('hub') || msg.includes('do') || msg.includes('service') || msg.includes('system') || msg.includes('help')) {
                return "APD Global Trade is an Elite B2B Hub that connects you **directly** to 5 Million+ verified buyers. We eliminate middlemen, protect your profit margins, and provide structured trade tools for professional export execution. Want a quick demo of the RFQ feed?";
            }

            // 5. Getting Started / How it works
            if (msg.includes('start') || msg.includes('join') || msg.includes('how') || msg.includes('work') || msg.includes('process') || msg.includes('step') || msg.includes('procedure')) {
                return "The process is simple: 1. Apply for membership. 2. Clear KYC/Identity check. 3. Access the 'Hidden' buyer data and start closing deals. Should I send you the direct signup link?";
            }
            
            // 6. Buyer Inquiries
            if (msg.includes('buyer') || msg.includes('customer') || msg.includes('market') || msg.includes('rfq') || msg.includes('lead') || msg.includes('sale')) {
                return "Our network handles over **$10B in annual trade volume** with more than **5 Million verified buyers**. We have active, urgent demand in Food, Grains, and Commodities. Are you an exporter looking for new markets?";
            }
            
            // 7. Trust / Legality
            if (msg.includes('safe') || msg.includes('scam') || msg.includes('verify') || msg.includes('real') || msg.includes('legit') || msg.includes('trust')) {
                return "Security is our core value. Every buyer must provide an **active L/C** or Bank Comfort Letter before they can post RFQs. We are an institutional-grade platform. You can see real-time verification proof on our Suppliers page.";
            }
            
            // 8. Greetings
            if (msg.includes('hi') || msg.includes('hello') || msg.includes('hey') || msg.includes('greet') || msg.includes('suhana')) {
                return "Hello! I'm Suhana, your APD Sales Assistant. I help serious exporters scale by providing direct, protected access to verified global buyers. How can I help you grow your trade volume today?";
            }

            // Global Professional Fallback
            return "As an APD Sales Assistant, my goal is to get you direct access to our **$10B+ volume network**. Would you like me to send you the direct link to our Membership options, or would you prefer a direct WhatsApp chat with our verification team?";
        }
    }
};

// Initializing
SalesBot.init();
