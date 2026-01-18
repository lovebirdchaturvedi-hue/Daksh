document.addEventListener("DOMContentLoaded", () => {
  const contacts = document.querySelectorAll(".buyer-contact");
  const plan = document.body.dataset.plan;
  const role = document.body.dataset.role;

  contacts.forEach(el => {
    if (role === "admin" || plan === "gold" || plan === "platinum") {
      el.style.display = "block";
    } else {
      el.style.display = "block";
      el.innerHTML = "🔒 Upgrade to Gold or Platinum to view buyer contact";
    }
  });
});
