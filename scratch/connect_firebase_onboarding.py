import codecs

with codecs.open('registration-onboarding.html', 'r', encoding='utf-8') as f:
    text = f.read()

firebase_logic = """
<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
  import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

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

  document.getElementById('onboardingForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const btn = e.target.querySelector('button');
    btn.innerText = "Processing & Securing Profile...";
    btn.disabled = true;
    
    try {
        await addDoc(collection(db, "suppliers"), {
            companyName: document.getElementById('company').value.trim(),
            contact: document.getElementById('repName').value.trim(),
            email: document.getElementById('email').value.trim().toLowerCase(),
            taxId: document.getElementById('taxId').value.trim(),
            tcSigned: document.getElementById('tc').checked,
            status: "approved",
            role: "buyer",
            plan: "elite_12m",
            onboardingDate: serverTimestamp()
        });
        
        setTimeout(() => {
          document.getElementById('formContainer').style.display = 'none';
          document.getElementById('successContainer').style.display = 'block';
        }, 1500);
    } catch (err) {
        console.error(err);
        alert("Error saving registration. Please try again.");
        btn.innerText = "Sign & Complete Onboarding";
        btn.disabled = false;
    }
  });
</script>
"""

# Replace the old <script> block
idx_start = text.find('<script>')
idx_end = text.find('</script>', idx_start) + 9

new_text = text[:idx_start] + firebase_logic + text[idx_end:]

with codecs.open('registration-onboarding.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated registration-onboarding.html with real Firebase integration.")
