import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
    import { getFirestore, initializeFirestore, collection, addDoc, serverTimestamp, getDocs } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

    const firebaseConfig = {
      apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
      authDomain: "apd-globaltrade-prod.firebaseapp.com",
      projectId: "apd-globaltrade-prod",
      storageBucket: "apd-globaltrade-prod.firebasestorage.app",
      messagingSenderId: "226407312435",
      appId: "1:226407312435:web:f8a54b1132af3899170746"
    };

    const app = initializeApp(firebaseConfig);
    const db = initializeFirestore(app, { experimentalForceLongPolling: true });

    // AUTOCOMPLETE LOGIC
    (async function initSearchAutocomplete() {
        try {
            const snap = await getDocs(collection(db, "rfqs"));
            const suggestions = new Set();
            snap.forEach(doc => {
                const data = doc.data();
                if(data.product) suggestions.add(data.product.trim());
                if(data.destination) suggestions.add(data.destination.trim());
            });
            const datalist = document.createElement('datalist');
            datalist.id = 'searchSuggestions';
            suggestions.forEach(item => {
                const option = document.createElement('option');
                option.value = item;
                datalist.appendChild(option);
            });
            document.body.appendChild(datalist);
        } catch (err) {
            console.error("Autocomplete init failed:", err);
        }
    })();

    window.handleQuickRFQ = async function(e) {
        e.preventDefault();
        const btn = document.getElementById("qr_btn");
        btn.innerText = "Securing Order...";
        btn.disabled = true;

        const product = document.getElementById("qr_product").value;
        const qty = document.getElementById("qr_qty").value + " " + document.getElementById("qr_unit").value;
        const dest = document.getElementById("qr_dest").value;

        try {
            // Save it to Firebase as pending
            const docRef = await addDoc(collection(db, "rfqs"), {
                buyerName: document.getElementById("qr_name").value,
                company: document.getElementById("qr_company").value,
                whatsapp: document.getElementById("qr_whatsapp").value,
                product: product,
                quantity: qty,
                destination: dest,
                specifications: document.getElementById("qr_specs").value,
                status: "payment_pending",
                source: "homepage_quick",
                deposit: "refundable",
                createdAt: serverTimestamp()
            });

            // Redirect to custom payment for the refundable deposit
            const isUSD = document.body.classList && document.body.classList.contains('currency-usd');
            const amount = isUSD ? 25 : 2000;
            const currency = isUSD ? 'USD' : 'INR';
            
            // Redirect to the payment page
            window.location.href = `/membership.html`;
            return;
        } catch (err) {
            alert('Error initiating verification: ' + err.message);
            btn.innerText = "Secure Verification & Post";
            btn.disabled = false;
        }
    };