import {
  auth,
  signInWithEmailAndPassword
} from "./firebase-init.js";

document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = emailInput.value;
  const password = passwordInput.value;

  try {
    await signInWithEmailAndPassword(auth, email, password);
    window.location.href = "/supplier-dashboard.html";
  } catch (err) {
    alert(err.message);
  }
});
