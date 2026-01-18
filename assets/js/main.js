// MAIN GLOBAL JS

document.addEventListener("DOMContentLoaded", function () {
  console.log("APD Global Trade loaded successfully");

  // Demo lock alert
  document.body.addEventListener("click", function (e) {
    if (e.target.classList.contains("btn-lock")) {
      alert("Please purchase membership to unlock buyer details.");
    }
  });
});
