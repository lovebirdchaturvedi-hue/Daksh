// /assets/js/auth.js

import { auth, db } from "./firebase-init.js";
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { doc, getDoc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

onAuthStateChanged(auth, async (user) => {
  if (!user) {
    document.body.dataset.plan = "guest";
    document.body.dataset.role = "guest";
    document.body.dataset.status = "guest";
    return;
  }

  const snap = await getDoc(doc(db, "suppliers", user.uid));

  if (!snap.exists()) {
    document.body.dataset.plan = "guest";
    document.body.dataset.role = "guest";
    document.body.dataset.status = "pending";
    return;
  }

  const data = snap.data();

  document.body.dataset.plan = data.plan || "basic";
  document.body.dataset.role = "supplier";
  document.body.dataset.status = data.status || "pending";
});
