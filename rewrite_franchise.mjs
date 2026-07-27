import fs from 'fs';

const html = fs.readFileSync('franchise.html', 'utf8');

const heroStart = html.indexOf('<section class="hero">');
const footerStart = html.indexOf('<footer');

if (heroStart === -1 || footerStart === -1) {
    console.error("Could not find hero or footer tags.");
    process.exit(1);
}

const newBody = `
  <section class="hero">
    <h1>Global Franchise & Distributorship</h1>
    <p>
      Secure exclusive franchise and distribution rights for top-tier brands like Amul. We provide end-to-end consulting, legal setup, and procurement facilitation to launch your local franchise successfully.
    </p>
  </section>

  <div class="container">
    <h2 class="section-title">Franchise Consulting & Setup</h2>
    <p class="subtitle">Secure your territory with official brand partnerships.</p>

    <div class="plans" style="display: flex; justify-content: center; margin-bottom: 80px;">
      <div class="plan highlight" style="max-width: 600px; width: 100%; text-align: left;">
        <div class="badge" style="background: #d4af37; color: black; margin-bottom: 15px;">⭐ EXCLUSIVE OPPORTUNITY</div>
        <h3 style="color: #d4af37; font-size: 24px;">Franchise Allocation Consulting</h3>
        <p style="font-size: 0.9rem; color: #94a3b8; margin-bottom: 15px;">Complete End-to-End Setup</p>
        
        <div class="price" style="margin-top: 5px; margin-bottom: 10px;">₹60,000 <span style="font-size: 14px; font-weight: normal; color: #94a3b8;">Total Consulting Fee</span></div>
        
        <div style="background: rgba(239, 68, 68, 0.1); border-left: 3px solid #ef4444; padding: 12px; margin-bottom: 25px; border-radius: 4px;">
            <p style="font-size: 0.9rem; color: #f87171; margin: 0; line-height: 1.4;"><strong>Booking Amount:</strong> ₹11,000 (Non-Refundable)</p>
            <p style="font-size: 0.8rem; color: #94a3b8; margin: 5px 0 0 0; line-height: 1.4;">The remaining balance of ₹49,000 is strictly payable ONLY upon successful franchise allocation.</p>
        </div>

        <h4 style="margin-top: 25px; margin-bottom: 15px; color: #fff; font-size: 16px;">Consultation Includes:</h4>
        <ul style="margin-bottom: 30px; line-height: 1.8; color: #cbd5e1; font-size: 14px; list-style: none; padding-left: 0;">
          <li><span style="color: #4ade80;">✅</span> Location Viability & Demand Analysis</li>
          <li><span style="color: #4ade80;">✅</span> Official Brand Application Processing</li>
          <li><span style="color: #4ade80;">✅</span> Documentation & Legal Compliance Setup</li>
          <li><span style="color: var(--gold);">✨</span> End-to-End Liaison with Brand Executives</li>
          <li><span style="color: var(--gold);">✨</span> Supply Chain & Procurement Setup</li>
        </ul>

        <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 30px 0;">

        <h3 style="font-family: 'Playfair Display', serif; font-size: 22px; color: var(--gold); margin-bottom: 15px;">Application Form</h3>
        <form id="franchiseForm" onsubmit="submitApplication(event)">
            <div style="margin-bottom: 15px;">
                <label style="display: block; margin-bottom: 5px; color: #cbd5e1; font-size: 13px;">Full Name *</label>
                <input type="text" id="f_name" required style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.3); color: white; box-sizing: border-box;">
            </div>
            
            <div style="margin-bottom: 15px;">
                <label style="display: block; margin-bottom: 5px; color: #cbd5e1; font-size: 13px;">WhatsApp Number (with Country Code) *</label>
                <input type="text" id="f_whatsapp" required placeholder="+91..." pattern="^\\+.*" title="Must start with + and include country code" style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.3); color: white; box-sizing: border-box;">
            </div>

            <div style="margin-bottom: 15px;">
                <label style="display: block; margin-bottom: 5px; color: #cbd5e1; font-size: 13px;">Target Company / Franchise (e.g., Amul) *</label>
                <input type="text" id="f_company" required style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.3); color: white; box-sizing: border-box;">
            </div>

            <div style="margin-bottom: 15px;">
                <label style="display: block; margin-bottom: 5px; color: #cbd5e1; font-size: 13px;">Type of Franchise *</label>
                <select id="f_type" required style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.3); color: white; box-sizing: border-box;">
                    <option value="">Select Type</option>
                    <option value="Retail Outlet">Retail Outlet</option>
                    <option value="Distribution Level">Distribution Level</option>
                    <option value="Master Franchise">Master Franchise</option>
                    <option value="Other">Other</option>
                </select>
            </div>

            <div style="margin-bottom: 25px;">
                <label style="display: block; margin-bottom: 5px; color: #cbd5e1; font-size: 13px;">Full Address for Proposed Franchise *</label>
                <textarea id="f_address" required rows="3" style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.3); color: white; box-sizing: border-box;"></textarea>
            </div>

            <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 8px; margin-bottom: 25px; border: 1px solid rgba(255,255,255,0.05);">
                <label style="display: flex; align-items: flex-start; gap: 10px; cursor: pointer;">
                    <input type="checkbox" id="termsAgree" required style="margin-top: 4px; width: 18px; height: 18px; cursor: pointer;">
                    <span style="font-size: 0.8rem; color: #cbd5e1; line-height: 1.5;">
                        <strong>I agree to the Terms & Conditions:</strong><br>
                        1. We do not guarantee a franchise, as it depends strictly on brand policies, your location, and existing area demand.<br>
                        2. The initial consultation fee of ₹11,000 is strictly non-refundable under any circumstances.<br>
                        3. I agree to pay the balance of ₹49,000 upon successful franchise allocation.
                    </span>
                </label>
            </div>

            <button type="submit" id="submitBtn" class="btn" style="background: #5f259f; color: white; font-weight: 800; width: 100%; border: 2px solid white;">
                SUBMIT & PAY ₹11,000
            </button>
            <div id="phonepeError" style="color: #ef4444; margin-top: 15px; font-size: 14px; display: none; text-align: center;"></div>
        </form>
      </div>
    </div>
  </div>

  <script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
    import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-firestore.js";

    const firebaseConfig = {
      apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
      authDomain: "apd-globaltrade-prod.firebaseapp.com",
      projectId: "apd-globaltrade-prod",
      storageBucket: "apd-globaltrade-prod.firebasestorage.app",
      messagingSenderId: "226407312435",
      appId: "1:226407312435:web:f8a54b1132af3899170746"
    };

    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);

    window.submitApplication = async function(e) {
        e.preventDefault();
        const btn = document.getElementById('submitBtn');
        const err = document.getElementById('phonepeError');
        
        if(!document.getElementById('termsAgree').checked) {
            err.innerText = "Please agree to the Terms & Conditions.";
            err.style.display = "block";
            return;
        }

        btn.innerText = 'Initializing Payment...';
        btn.disabled = true;
        err.style.display = "none";

        try {
            // First save to DB
            const docRef = await addDoc(collection(db, "franchise_applications"), {
                name: document.getElementById('f_name').value,
                whatsapp: document.getElementById('f_whatsapp').value,
                company: document.getElementById('f_company').value,
                type: document.getElementById('f_type').value,
                address: document.getElementById('f_address').value,
                status: "Pending Payment",
                timestamp: serverTimestamp()
            });

            // Then initiate PhonePe
            const res = await fetch('/api/phonepe-init', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ amount: 11000, planName: 'Franchise Consultation Booking' })
            });
            const data = await res.json();
            
            if (data.success && data.url) { 
                window.location.href = data.url; 
            } else { 
                err.innerText = data.error || 'Payment gateway failed. Your form is saved. Contact support.';
                err.style.display = 'block'; 
                btn.innerText = 'SUBMIT & PAY ₹11,000'; 
                btn.disabled = false; 
            }
        } catch(error) {
            console.error("Error submitting form: ", error);
            err.innerText = 'Network Error. Please try again.';
            err.style.display = 'block';
            btn.innerText = 'SUBMIT & PAY ₹11,000';
            btn.disabled = false;
        }
    }
  </script>
`;

const newHtml = html.substring(0, heroStart) + newBody + html.substring(footerStart);

fs.writeFileSync('franchise.html', newHtml, 'utf8');
console.log("Updated franchise.html");
