document.addEventListener("DOMContentLoaded", () => {
  /*
    These values must be injected server-side or
    via Firebase auth logic before page load.
    Example:
    <body data-plan="free" data-status="pending">
  */

  const plan = document.body.dataset.plan;      // free | gold | platinum
  const status = document.body.dataset.status;  // pending | approved

  const canViewContact =
    status === "approved" &&
    (plan === "gold" || plan === "platinum");

  document.querySelectorAll(".rfq-card").forEach(card => {
    const buyerContact = card.querySelector(".buyer-contact");
    const lockMessage = card.querySelector(".lock-message");

    if (!buyerContact || !lockMessage) return;

    if (canViewContact) {
      // ✅ Approved & paid supplier
      buyerContact.style.display = "block";
      lockMessage.style.display = "none";
    } else {
      // 🔒 Free / unapproved supplier
      buyerContact.style.display = "none";
      lockMessage.style.display = "block";
    }
  });
});
