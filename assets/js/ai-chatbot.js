(function() {
    // Inject Font
    const fontLink = document.createElement('link');
    fontLink.href = 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap';
    fontLink.rel = 'stylesheet';
    document.head.appendChild(fontLink);

    // Chatbot HTML Structure
    const chatHTML = `
    <div id="apd-chat-widget" style="position: fixed; bottom: 30px; right: 30px; z-index: 99999; font-family: 'Inter', sans-serif;">
        <!-- Chat Bubble -->
        <div id="apd-chat-bubble" style="width: 60px; height: 60px; background: linear-gradient(135deg, #d4af37, #facc15); border-radius: 50%; box-shadow: 0 10px 25px rgba(212,175,55,0.4); display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.3s ease; position: relative;">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
            <span style="position: absolute; top: -5px; right: -5px; width: 15px; height: 15px; background: #ef4444; border-radius: 50%; border: 2px solid #000; animation: pulse 2s infinite;"></span>
        </div>

        <!-- Chat Window -->
        <div id="apd-chat-window" style="display: none; position: absolute; bottom: 80px; right: 0; width: 350px; height: 500px; background: #020617; border: 1px solid rgba(212,175,55,0.3); border-radius: 16px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.6); flex-direction: column;">
            
            <!-- Header -->
            <div style="background: linear-gradient(90deg, #0f172a, #1e293b); padding: 20px; border-bottom: 1px solid rgba(212,175,55,0.2); display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 10px; height: 10px; background: #22c55e; border-radius: 50%;"></div>
                    <div>
                        <div style="color: #fff; font-weight: 700; font-size: 15px;">APD AI Sourcing</div>
                        <div style="color: #94a3b8; font-size: 11px;">Typically replies instantly</div>
                    </div>
                </div>
                <button id="apd-chat-close" style="background: transparent; border: none; color: #94a3b8; cursor: pointer; font-size: 20px; padding: 0;">&times;</button>
            </div>

            <!-- Messages Area -->
            <div id="apd-chat-messages" style="flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 15px; background: rgba(2,6,23,0.95);">
                <!-- Initial Bot Message -->
                <div style="display: flex; gap: 10px; align-items: flex-end;">
                    <div style="width: 25px; height: 25px; border-radius: 50%; background: #d4af37; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: bold; color: #000;">AI</div>
                    <div style="background: #1e293b; color: #e2e8f0; padding: 12px 15px; border-radius: 12px 12px 12px 0; font-size: 13px; line-height: 1.5; max-width: 80%;">
                        Hello! Welcome to APD Global Trade. Are you looking to source verified commodities or apply as a supplier?
                    </div>
                </div>
                
                <!-- Options -->
                <div id="apd-chat-options" style="display: flex; flex-direction: column; gap: 8px; margin-left: 35px; max-width: 80%;">
                    <button class="apd-chat-opt" data-flow="buy" style="background: rgba(212,175,55,0.1); border: 1px solid rgba(212,175,55,0.3); color: #d4af37; padding: 10px 15px; border-radius: 8px; text-align: left; cursor: pointer; font-size: 13px; font-weight: 500; transition: all 0.2s;">I want to Buy (Source RFQs)</button>
                    <button class="apd-chat-opt" data-flow="sell" style="background: rgba(212,175,55,0.1); border: 1px solid rgba(212,175,55,0.3); color: #d4af37; padding: 10px 15px; border-radius: 8px; text-align: left; cursor: pointer; font-size: 13px; font-weight: 500; transition: all 0.2s;">I want to Sell (Supplier)</button>
                    <button class="apd-chat-opt" data-flow="compliance" style="background: rgba(212,175,55,0.1); border: 1px solid rgba(212,175,55,0.3); color: #d4af37; padding: 10px 15px; border-radius: 8px; text-align: left; cursor: pointer; font-size: 13px; font-weight: 500; transition: all 0.2s;">Check Compliance & Certs</button>
                </div>
            </div>

            <!-- Input Area -->
            <div style="padding: 15px; border-top: 1px solid rgba(255,255,255,0.1); background: #0f172a; display: flex; gap: 10px;">
                <input type="text" id="apd-chat-input" placeholder="Type your message..." style="flex: 1; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 10px 15px; border-radius: 20px; color: #fff; font-size: 13px; outline: none;">
                <button id="apd-chat-send" style="background: linear-gradient(90deg, #d4af37, #facc15); border: none; width: 40px; height: 40px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                </button>
            </div>
        </div>
    </div>
    <style>
        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(239, 68, 68, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
        }
        .apd-chat-opt:hover { background: rgba(212,175,55,0.2) !important; color: #facc15 !important; }
        
        @media screen and (max-width: 480px) {
            #apd-chat-window {
                width: 90vw !important;
                right: -15px !important;
                bottom: 70px !important;
            }
        }
    </style>
    `;

    document.body.insertAdjacentHTML('beforeend', chatHTML);

    const bubble = document.getElementById('apd-chat-bubble');
    const windowEl = document.getElementById('apd-chat-window');
    const closeBtn = document.getElementById('apd-chat-close');
    const messagesEl = document.getElementById('apd-chat-messages');
    const inputEl = document.getElementById('apd-chat-input');
    const sendBtn = document.getElementById('apd-chat-send');
    const options = document.querySelectorAll('.apd-chat-opt');

    // Toggle Chat
    bubble.addEventListener('click', () => {
        windowEl.style.display = windowEl.style.display === 'none' ? 'flex' : 'none';
        bubble.querySelector('span').style.display = 'none'; // hide red dot
    });

    closeBtn.addEventListener('click', () => {
        windowEl.style.display = 'none';
    });

    function addUserMessage(text) {
        const msg = `
        <div style="display: flex; justify-content: flex-end; margin-bottom: 10px;">
            <div style="background: linear-gradient(90deg, #d4af37, #b8860b); color: #000; padding: 12px 15px; border-radius: 12px 12px 0 12px; font-size: 13px; line-height: 1.5; max-width: 80%; font-weight: 500;">
                ${text}
            </div>
        </div>`;
        messagesEl.insertAdjacentHTML('beforeend', msg);
        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    function addBotMessage(text) {
        const msg = `
        <div style="display: flex; gap: 10px; align-items: flex-end; margin-bottom: 10px;">
            <div style="width: 25px; height: 25px; border-radius: 50%; background: #d4af37; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: bold; color: #000; flex-shrink: 0;">AI</div>
            <div style="background: #1e293b; color: #e2e8f0; padding: 12px 15px; border-radius: 12px 12px 12px 0; font-size: 13px; line-height: 1.5; max-width: 80%;">
                ${text}
            </div>
        </div>`;
        messagesEl.insertAdjacentHTML('beforeend', msg);
        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    // Handle Quick Options
    options.forEach(btn => {
        btn.addEventListener('click', function() {
            const flow = this.getAttribute('data-flow');
            const text = this.innerText;
            
            document.getElementById('apd-chat-options').style.display = 'none';
            addUserMessage(text);
            
            setTimeout(() => {
                if (flow === 'buy') {
                    addBotMessage("Excellent. To view live institutional requirements and submit a quote request, please visit our <a href='/buyer-rfqs.html' style='color:#d4af37;'>Buyer RFQs</a> page.");
                } else if (flow === 'sell') {
                    addBotMessage("Great! We are always looking for verified exporters. You can apply for a Supplier Membership <a href='/membership.html' style='color:#d4af37;'>here</a>.");
                } else {
                    addBotMessage("All our suppliers undergo strict DUNS tracking and KYC checks. We map directly to WCO guidelines. Please leave your WhatsApp number below to speak with our compliance officer.");
                }
            }, 800);
        });
    });

    // Handle Custom Input
    function handleSend() {
        const val = inputEl.value.trim();
        if (!val) return;
        
        addUserMessage(val);
        inputEl.value = '';
        
        document.getElementById('apd-chat-options').style.display = 'none';
        
        setTimeout(() => {
            if (val.match(/\\d{7,15}/)) {
                addBotMessage("Thank you. An APD Global Trade representative will contact you shortly on this number to assist you further.");
            } else {
                addBotMessage("I am a virtual assistant. To better help you with that, please provide your WhatsApp number or email address, and a human expert will connect with you.");
            }
        }, 1000);
    }

    sendBtn.addEventListener('click', handleSend);
    inputEl.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });

})();
