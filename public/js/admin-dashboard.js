import { auth } from "./firebase-init.js";
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

onAuthStateChanged(auth, async (user) => {
  if (!user) {
    window.location.href = "/supplier-login.html";
    return;
  }

  const token = await user.getIdTokenResult(true);

  if (token.claims.role !== "admin") {
    alert("You are not an admin");
    await auth.signOut();
    return;
  }

  // ✅ ADMIN ACCESS GRANTED
  console.log("ADMIN LOGGED IN");
  loadAdminDashboard();
});
