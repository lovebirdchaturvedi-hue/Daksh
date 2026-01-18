const rfqs = [
  {
    buyer: "Shree Agro Exports",
    country: "India",
    product: "Basmati Rice 1121",
    quantity: "500 MT",
    phone: "+91XXXXXXXXXX",
    email: "buyer@hidden.com"
  },
  {
    buyer: "Global Grain Traders",
    country: "UAE",
    product: "Yellow Maize",
    quantity: "1,200 MT",
    phone: "+971XXXXXXXX",
    email: "buyer@hidden.com"
  },
  {
    buyer: "FreshFarm Foods",
    country: "USA",
    product: "Organic Wheat",
    quantity: "800 MT",
    phone: "+1XXXXXXXXXX",
    email: "buyer@hidden.com"
  }
];

const container = document.getElementById("rfqContainer");

if (container) {
  rfqs.forEach(rfq => {
    const div = document.createElement("div");
    div.className = "rfq-card";
    div.innerHTML = `
      <h3>${rfq.product}</h3>
      <p><strong>Buyer:</strong> ${rfq.buyer}</p>
      <p><strong>Country:</strong> ${rfq.country}</p>
      <p><strong>Quantity:</strong> ${rfq.quantity}</p>
      <p class="locked"><strong>Phone:</strong> 🔒 Locked</p>
      <p class="locked"><strong>Email:</strong> 🔒 Locked</p>
      <button class="btn-lock">Unlock Buyer Details</button>
    `;
    container.appendChild(div);
  });
}
