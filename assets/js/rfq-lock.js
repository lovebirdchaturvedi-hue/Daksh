// /assets/js/rfq-lock.js

document.addEventListener("DOMContentLoaded", () => {
  const contacts = document.querySelectorAll(".buyer-contact");

  const plan = document.body.dataset.plan;
  const status = document.body.dataset.status;

  contacts.forEach(el => {
    if (
      status === "approved" &&
      (plan === "gold" || plan === "platinum")
    ) {
      el.style.display = "block";
    } else if (status !== "approved") {
      el.style.display = "block";
      el.innerHTML = "⏳ Your account is under review";
    } else {
      el.style.display = "block";
      el.innerHTML = "🔒 Upgrade to Gold or Platinum to view buyer contact";
    }
  });
});
