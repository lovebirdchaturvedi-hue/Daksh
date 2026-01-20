onAuthStateChanged(auth, async (user) => {
  if (!user) {
    window.location.href = "/login.html";
    return;
  }

  const token = await user.getIdTokenResult(true);

  if (!token.claims.admin) {
    alert("Access denied");
    window.location.href = "/";
    return;
  }

  document.body.style.display = "block";
  loadSuppliers();
});
