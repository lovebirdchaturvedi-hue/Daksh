import { db } from "./firebase-init.js";
import {
  collection,
  addDoc,
  serverTimestamp
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const form = document.getElementById("rfqForm");
const successMsg = document.getElementById("successMsg");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const rfq = {
    product: document.getElementById("product").value,
    quantity: document.getElementById("quantity").value,
    country: document.getElementById("country").value,
    company: document.getElementById("company").value,
    contactPerson: document.getElementById("contactPerson").value,
    email: document.getElementById("email").value,
    phone: document.getElementById("phone").value,
    details: document.getElementById("details").value,
    status: "pending",      // admin approval
    createdAt: serverTimestamp()
  };

  await addDoc(collection(db, "rfqs"), rfq);

  form.reset();
  successMsg.style.display = "block";
});
