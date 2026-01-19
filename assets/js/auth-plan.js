import { auth, db } from "./firebase-init.js";
import { doc, getDoc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

auth.onAuthStateChanged(async (user) => {
  if (!user) return;

  const ref = doc(db, "suppliers", user.uid);
  const snap = await getDoc(ref);

  if (!snap.exists()) return;

  const { plan, status } = snap.data();

  document.body.dataset.plan = plan;
  document.body.dataset.status = status;
});
