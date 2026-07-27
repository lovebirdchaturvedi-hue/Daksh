const admin = require('firebase-admin');
const fs = require('fs');

const serviceAccount = JSON.parse(fs.readFileSync('C:\\Users\\DELL\\Downloads\\Daksh\\serviceAccountKey.jason.txt', 'utf8'));

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  projectId: 'apd-globaltrade-prod'
});

const db = admin.firestore();

const countries = ['USA', 'UK', 'Germany', 'France', 'UAE', 'Saudi Arabia', 'Australia', 'Canada', 'Singapore', 'Japan', 'South Korea', 'Netherlands'];
const ports = ['Jebel Ali', 'Rotterdam', 'Hamburg', 'Los Angeles', 'Singapore Port', 'Sydney', 'London Gateway', 'Yokohama', 'Busan'];
const packaging = ['25kg Bags', '50kg Bags', 'Bulk', 'Jumbo Bags'];

function randomChoice(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

function generateRandomDate(start, end) {
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
}

async function uploadCMHuskPowderRFQs() {
    const rfqsCollection = db.collection('rfqs');
    let batch = db.batch();
    let batchCount = 0;
    let totalUploaded = 0;

    const endDate = new Date();
    const startDate = new Date();
    startDate.setDate(startDate.getDate() - 60); // Random dates in the last 60 days

    for (let i = 0; i < 100; i++) {
        const docRef = rfqsCollection.doc();
        const rfqData = {
            product: 'CM Husk Powder',
            buyerName: `Verified Importer #${Math.floor(Math.random() * 90000) + 10000}`,
            country: randomChoice(countries),
            quantity: `${Math.floor(Math.random() * 50) + 10} MT`,
            packaging: randomChoice(packaging),
            portOfDestination: randomChoice(ports),
            status: 'Active',
            createdAt: admin.firestore.Timestamp.fromDate(generateRandomDate(startDate, endDate)),
            targetPrice: 'Negotiable',
            source: 'Synthetic Injection'
        };

        batch.set(docRef, rfqData);
        batchCount++;

        if (batchCount >= 50) {
            await batch.commit();
            totalUploaded += batchCount;
            console.log(`Committed ${totalUploaded} RFQs...`);
            batch = db.batch();
            batchCount = 0;
        }
    }

    if (batchCount > 0) {
        await batch.commit();
        totalUploaded += batchCount;
        console.log(`Committed ${totalUploaded} RFQs...`);
    }

    console.log("Successfully uploaded 100 CM Husk Powder RFQs.");
}

uploadCMHuskPowderRFQs().then(() => process.exit(0)).catch(console.error);
