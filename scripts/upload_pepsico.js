
const admin = require('firebase-admin');

// Initialize with default credentials from the CLI
admin.initializeApp({
  projectId: 'apd-globaltrade-prod'
});

const db = admin.firestore();

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
  console.log('🚀 Starting upload of PepsiCo RFQs...');
  const batch = db.batch();
  
  WORLDWIDE_PEPSICO_BUYERS.forEach(rfq => {
    const docRef = db.collection('rfqs').doc();
    batch.set(docRef, {
      ...rfq,
      createdAt: admin.firestore.FieldValue.serverTimestamp()
    });
  });

  try {
    await batch.commit();
    console.log('✅ Successfully uploaded all PepsiCo RFQs to Firestore!');
  } catch (error) {
    console.error('❌ Upload failed:', error);
  }
}

upload();
