// social-proof.js
// Injects a floating "recent activity" ticker to build trust and FOMO.

document.addEventListener("DOMContentLoaded", () => {
    // Prevent showing on small mobile screens if it clutters too much, or keep it small
    
    const messages = [
        "exporter from Mumbai just unlocked 3 buyers in Dubai.",
        "XYZ Spices upgraded to the Institutional Elite Plan.",
        "A $140,000 Rice RFQ was just posted in Saudi Arabia.",
        "Agro Exporter from Gujarat successfully connected with a buyer in Oman.",
        "A premium membership was just activated in Delhi.",
        "buyer in Qatar just viewed a supplier's profile.",
        "Global Enterprise Plan unlocked by a Top Rice Mill in Haryana."
    ];

    const container = document.createElement("div");
    container.id = "social-proof-ticker";
    container.style.cssText = `
        position: fixed;
        bottom: -100px;
        left: 30px;
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 12px;
        padding: 15px 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 15px rgba(212, 175, 55, 0.2);
        z-index: 99998; /* Just below chat widget */
        display: flex;
        align-items: center;
        gap: 15px;
        max-width: 350px;
        transition: bottom 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.6s ease;
        opacity: 0;
        pointer-events: none;
    `;

    const icon = document.createElement("div");
    icon.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>`;
    icon.style.cssText = `
        flex-shrink: 0;
        background: rgba(212, 175, 55, 0.1);
        padding: 8px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    `;

    const textWrap = document.createElement("div");
    
    const title = document.createElement("div");
    title.innerText = "Verified Activity";
    title.style.cssText = `
        font-size: 0.75rem;
        color: #4ade80;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 3px;
    `;

    const message = document.createElement("div");
    message.id = "social-proof-msg";
    message.style.cssText = `
        font-size: 0.9rem;
        color: #fff;
        line-height: 1.4;
        font-family: 'Inter', sans-serif;
    `;

    textWrap.appendChild(title);
    textWrap.appendChild(message);
    
    container.appendChild(icon);
    container.appendChild(textWrap);
    
    document.body.appendChild(container);

    // Adjust position based on chat widget to avoid overlap
    const adjustPosition = () => {
        if (window.innerWidth <= 768) {
            container.style.left = "50%";
            container.style.transform = "translateX(-50%)";
            container.style.width = "90%";
        } else {
            container.style.left = "30px";
            container.style.transform = "none";
            container.style.width = "auto";
        }
    };
    
    window.addEventListener('resize', adjustPosition);
    adjustPosition();

    function showRandomMessage() {
        const randomMsg = messages[Math.floor(Math.random() * messages.length)];
        // Add random time like "2 mins ago"
        const time = Math.floor(Math.random() * 15) + 1;
        message.innerHTML = `An <strong>${randomMsg}</strong> <span style="opacity: 0.6; font-size: 0.8rem; display: block; margin-top: 4px;">${time} min${time>1?'s':''} ago</span>`;
        
        // Slide up
        container.style.opacity = "1";
        // To avoid overlapping with chat widget on desktop (chat widget is at bottom: 30px, height: 65px -> so bottom: 110px is safe)
        container.style.bottom = window.innerWidth <= 768 ? "100px" : "110px";
        
        // Hide after 6 seconds
        setTimeout(() => {
            container.style.opacity = "0";
            container.style.bottom = "-100px";
        }, 6000);
    }

    // Initial delay before first popup
    setTimeout(() => {
        showRandomMessage();
        // Then repeat every 15-25 seconds randomly
        setInterval(() => {
            showRandomMessage();
        }, Math.floor(Math.random() * 10000) + 15000);
    }, 3000);

});
