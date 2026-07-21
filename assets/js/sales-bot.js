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
    handoffNumbers: ['919266418868', '919217114472'],
    botName: 'APD AI Sales BOT',
    botStatus: 'ACTIVE SALES AGENT',
    avatar: '/assets/img/sales-agent.png',

    init() {
        this.renderWidget();
        this.addEventListeners();
        
        // Auto-open disabled per user request
    },

    renderWidget() {
        if (document.getElementById('salesBot')) return;
        const widgetHTML = `
            <div class="sales-bot-widget" id="salesBot">
                <div class="bot-bubble" id="botBubble" style="background: linear-gradient(135deg, var(--bot-navy) 0%, var(--bot-navy-deep) 100%);">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--bot-gold);"><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path><path d="M12 8V4H8"></path></svg>
                </div>
                <div class="chat-window" id="chatWindow">
                    <div class="chat-header">
                        <div class="bot-info" style="display: flex; align-items: center; gap: 10px;">
                            <img src="/assets/img/sales-agent.png" style="width: 35px; height: 35px; border-radius: 50%; object-fit: cover; border: 1px solid var(--gold);">
                            <div style="display: flex; flex-direction: column;">
                                <span class="name">APD AI Sales BOT</span>
                                <span class="status" style="color: #4ade80; font-size: 10px;">• ACTIVE SALES AGENT</span>
                            </div>
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
                this.addWAHandoffButton("Chat with Executive 1", this.handoffNumbers[0]);
                this.addWAHandoffButton("Chat with Executive 2", this.handoffNumbers[1]);
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

    addWAHandoffButton(label, numberOverride) {
        const container = document.getElementById('chatMessages');
        const number = numberOverride || this.handoffNumbers[0];
        const btn = document.createElement('a');
        btn.href = `https://wa.me/${number}?text=Hi, I was chatting with your AI Assistant on the APD Global Trade platform. I need executive assistance.`;
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
                return "Excellent! Before I provide you with our verified buyer matching credentials, could you please confirm your current export capacity (MT per month) and your primary rice variety (e.g., Basmati, Long Grain, Parboiled)?";
            }

            // 1. Export Inquiries
            if (msg.includes('export') || msg.includes('sell') || msg.includes('rice') || msg.includes('sending')) {
                return "We have massive institutional mandates for **Rice (Basmati & Parboiled)** and Agro-Commodities across the GCC and West Africa. We focus on connecting you directly to the importing companies. What is your current warehouse location and target export market?";
            }

            // 2. Pricing / Plan Inquiries
            if (msg.includes('plan') || msg.includes('price') || msg.includes('cost') || msg.includes('how much') || msg.includes('fee') || msg.includes('trial') || msg.includes('pay')) {
                return "We operate on an Institutional Membership model to ensure only verified exporters enter the corridor. Our **3-Month Premium Trial ($499)** includes 100 bulk buyer credits to get you established immediately. Should I share the direct activation link?";
            }
            
            // 3. Platform / What you do
            if (msg.includes('platform') || msg.includes('hub') || msg.includes('do') || msg.includes('service') || msg.includes('system') || msg.includes('help')) {
                return "APD Global Trade is an Institutional Data Gateway. We provide you with direct, unmasked access to 5 Million+ verified global buyers, helping you eliminate middlemen and protect your margins. Would you like me to walk you through our matching process?";
            }

            // 4. Getting Started / How it works
            if (msg.includes('start') || msg.includes('join') || msg.includes('how') || msg.includes('work') || msg.includes('process') || msg.includes('step') || msg.includes('procedure')) {
                return "The onboarding process is structured: 1. Institutional Registration. 2. KYC/Identity Clearance. 3. Access to High-Volume Matchmaking. Shall I send you the secure registration link to begin?";
            }
            
            // 5. Greetings
            if (msg.includes('hi') || msg.includes('hello') || msg.includes('hey') || msg.includes('greet')) {
                return "Hello! I'm the APD Senior Sales Assistant. I help serious exporters scale by providing direct, protected access to verified institutional buyers. How can I assist you with your trade volume today?";
            }

            // Global Professional Fallback
            return "As your Institutional Trade Assistant, my goal is to guide you into our **$10B+ volume network**. Please tell me more about your product category and export targets so I can provide the correct mandates.";
        }
    }
};

// Initializing
SalesBot.init();
