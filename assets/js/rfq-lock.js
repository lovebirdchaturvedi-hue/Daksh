document.addEventListener("DOMContentLoaded", () => {
  const plan = document.body.dataset.plan;
  const status = document.body.dataset.status;

  document.querySelectorAll(".buyer-contact").forEach(el => {
    if (
      status === "approved" &&
      (plan === "gold" || plan === "platinum")
    ) {
      el.style.display = "block";
    } else {
      el.style.display = "block";
      el.innerHTML = "🔒 Upgrade to Gold / Platinum to view buyer contact";
    }
  });
});
