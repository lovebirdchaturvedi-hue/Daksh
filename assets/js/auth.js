import { auth, db } from "./firebase-init.js";
import { onAuthStateChanged } from
"https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { doc, getDoc } from
"https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

onAuthStateChanged(auth, async (user) => {
  if (!user) {
    document.body.dataset.plan = "guest";
    document.body.dataset.status = "guest";
    return;
  }

  const snap = await getDoc(doc(db, "suppliers", user.uid));

  if (!snap.exists()) {
    document.body.dataset.plan = "guest";
    document.body.dataset.status = "pending";
    return;
  }

  const d = snap.data();
  document.body.dataset.plan = d.plan;
  document.body.dataset.status = d.status;
});
