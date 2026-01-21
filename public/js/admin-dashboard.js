import {
  auth,
  db,
  onAuthStateChanged,
  collection,
  getDocs,
  doc,
  updateDoc
} from "./firebase-init.js";

onAuthStateChanged(auth, async (user) => {
  if (!user) {
    window.location.href = "/supplier-login.html";
    return;
  }

  const token = await user.getIdTokenResult(true);

  if (token.claims.role !== "admin") {
    alert("Access denied");
    return;
  }

  loadSuppliers();
});

async function loadSuppliers() {
  const snap = await getDocs(collection(db, "suppliers"));
  snap.forEach(docu => {
    console.log(docu.id, docu.data());
  });
}
