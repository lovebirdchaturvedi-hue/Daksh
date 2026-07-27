
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const serviceAccount = JSON.parse(fs.readFileSync('C:\\Users\\DELL\\Downloads\\Daksh\\serviceAccountKey.jason.txt', 'utf8'));

// Initialize with service account credentials
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  projectId: 'apd-globaltrade-prod'
});

const db = admin.firestore();

const LEADS_PATH = 'C:\\Users\\DELL\\Downloads\\Daksh\\IMPORTERS_2026.json';

function extractProduct(name) {
    const n = name.toLowerCase();
    if (n.includes('sugar')) return 'Industrial Sugar';
    if (n.includes('rice')) return 'Long Grain Rice';
    if (n.includes('potato')) return 'Potatoes';
    if (n.includes('oil')) return 'Edible Oil';
    if (n.includes('corn')) return 'Yellow Maize (Corn)';
    if (n.includes('spice')) return 'Indian Spices';
    if (n.includes('vegetable') || n.includes('vegitable')) return 'Fresh Vegetables';
    if (n.includes('wheat')) return 'Wheat Grain';
    if (n.includes('pulse') || n.includes('dal')) return 'Pulses/Lentils';
    if (n.includes('fruit')) return 'Fresh Fruits';
    if (n.includes('garlic')) return 'Fresh Garlic';
    if (n.includes('onion')) return 'Red Onions';
    return 'Trade Inquiry';
}

function extractCountry(name) {
    const n = name.toLowerCase();
    if (n.includes('india') || n.includes('+91')) return 'India';
    if (n.includes('nepal')) return 'Nepal';
    if (n.includes('mexico')) return 'Mexico';
    if (n.includes('uk')) return 'United Kingdom';
    if (n.includes('usa')) return 'USA';
    if (n.includes('uae') || n.includes('dubai')) return 'UAE';
    if (n.includes('vietnam')) return 'Vietnam';
    if (n.includes('kenya')) return 'Kenya';
    if (n.includes('thailand')) return 'Thailand';
    return 'Global';
}

async function upload() {
    console.log('🚀 Loading leads from JSON...');
    const rawData = fs.readFileSync(LEADS_PATH);
    const leads = JSON.parse(rawData);
    
    console.log(`📊 Found ${leads.length} leads. Starting batch upload...`);
    
    let count = 0;
    let batch = db.batch();
    
    for (const lead of leads) {
        const product = extractProduct(lead.name);
        const country = extractCountry(lead.name);
        
        const docRef = db.collection('rfqs').doc();
        batch.set(docRef, {
            product: product,
            quantity: 'Institutional Volume',
            destination: country,
            company: lead.name.split(',')[0].substring(0, 50), // Clean up name
            phone: lead.phone,
            status: 'open',
            source: 'importers_2026_bulk',
            createdAt: admin.firestore.FieldValue.serverTimestamp()
        });
        
        count++;
        
        if (count % 500 === 0) {
            await batch.commit();
            console.log(`✅ Uploaded ${count} leads...`);
            batch = db.batch();
        }
        
        // Safety: Only upload 2,000 for now to avoid overloading or hitting limits
        if (count >= 2000) break;
    }
    
    if (count % 500 !== 0) {
        await batch.commit();
    }
    
    console.log(`🎉 Successfully uploaded ${count} leads to APD Global Trade!`);
}

upload().catch(err => console.error('❌ Fatal Error:', err));
