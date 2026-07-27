
const axios = require('axios');

const PROJECT_ID = 'apd-globaltrade-prod';
const COLLECTION = 'rfqs';

const WORLDWIDE_PEPSICO_BUYERS = [
  { name: "PepsiCo Global Procurement (USA)", product: "Industrial Sugar S-30", quantity: "50,000 MT", deliveryPort: "New York", dealSizeUSD: 12500000, status: "open", source: "admin-seed" },
  { name: "PepsiCo Mexico (Sabritas)", product: "Atlantic Potatoes (PepsiCo Grade)", quantity: "20,000 MT", deliveryPort: "Veracruz", dealSizeUSD: 5500000, status: "open", source: "admin-seed" },
  { name: "PepsiCo UK (Walkers)", product: "Potato Flakes", quantity: "5,000 MT", deliveryPort: "Liverpool", dealSizeUSD: 1200000, status: "open", source: "admin-seed" },
  { name: "Varun Beverages Nepal (Pepsi Bottler)", product: "Industrial Sugar S-30", quantity: "1,000 MT", deliveryPort: "Birgunj", dealSizeUSD: 850000, status: "open", source: "admin-seed" },
  { name: "CG Corp Global (Wai Wai/Kwik's)", product: "Atlantic Potatoes (PepsiCo Grade)", quantity: "500 MT", deliveryPort: "Biratnagar", dealSizeUSD: 450000, status: "open", source: "admin-seed" },
  { name: "PepsiCo India (Gurgaon Hub)", product: "Extrusion Corn (Maize)", quantity: "10,000 MT", deliveryPort: "Kandla", dealSizeUSD: 2800000, status: "open", source: "admin-seed" },
  { name: "Yashoda Foods (Current)", product: "Refined Sunflower Oil (Bulk)", quantity: "200 MT", deliveryPort: "Bhairahawa", dealSizeUSD: 320000, status: "open", source: "admin-seed" }
];

async function upload() {
  console.log('🚀 Starting REST upload of PepsiCo RFQs...');
  
  for (const rfq of WORLDWIDE_PEPSICO_BUYERS) {
    try {
      const url = `https://firestore.googleapis.com/v1/projects/${PROJECT_ID}/databases/(default)/documents/${COLLECTION}`;
      
      const payload = {
        fields: {
          product: { stringValue: rfq.product },
          quantity: { stringValue: rfq.quantity },
          deliveryPort: { stringValue: rfq.deliveryPort },
          dealSizeUSD: { integerValue: rfq.dealSizeUSD.toString() },
          status: { stringValue: rfq.status },
          source: { stringValue: rfq.source },
          buyerName: { stringValue: rfq.name },
          createdAt: { timestampValue: new Date().toISOString() }
        }
      };

      await axios.post(url, payload);
      console.log(`✅ Uploaded: ${rfq.name}`);
    } catch (error) {
      console.error(`❌ Failed: ${rfq.name}`, error.response ? error.response.data : error.message);
    }
  }
  console.log('🏁 Finished upload process.');
}

upload();
