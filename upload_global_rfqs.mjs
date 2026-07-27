import admin from 'firebase-admin';
import fs from 'fs';
import csv from 'csv-parser';

// Initialize Firebase Admin (assuming default application credentials or GOOGLE_APPLICATION_CREDENTIALS)
if (!admin.apps.length) {
    admin.initializeApp();
}

const db = admin.firestore();
const collectionName = 'global_rfqs';

/**
 * Extracts certification tier based on keywords.
 */
function determineCertificationTier(text) {
    if (!text) return "Unspecified";
    const lower = text.toLowerCase();
    if (lower.includes('organic') || lower.includes('non-gmo') || lower.includes('bio') || lower.includes('natural') || lower.includes('eco')) {
        return "Organic/Non-GMO";
    }
    return "Conventional";
}

/**
 * Normalizes regions based on country.
 */
function getRegion(countryName) {
    if (!countryName) return "Global / Other";
    const country = countryName.toUpperCase().trim();
    
    const gulf_countries = ["UAE", "SAUDI ARABIA", "QATAR", "OMAN", "BAHRAIN", "KUWAIT", "DUBAI"];
    const euro_countries = ["UNITED KINGDOM", "UK", "GERMANY", "FRANCE", "NETHERLANDS", "ITALY", "SPAIN", "POLAND"];
    const africa_countries = ["SOUTH AFRICA", "NIGERIA", "EGYPT", "KENYA", "GHANA", "MOROCCO", "ALGERIA"];

    if (country.includes("USA") || country.includes("UNITED STATES") || country.includes("CANADA")) {
        return "USA / North America";
    } else if (gulf_countries.some(g => country.includes(g))) {
        return "Gulf Region";
    } else if (euro_countries.some(e => country.includes(e))) {
        return "European Union / UK";
    } else if (africa_countries.some(a => country.includes(a))) {
        return "Africa";
    } else {
        return "Global / Other";
    }
}

async function uploadData(filePath) {
    console.log(`🚀 Starting ingestion of ${filePath} into '${collectionName}'...`);
    const results = [];

    // Parse the CSV file
    fs.createReadStream(filePath)
        .pipe(csv())
        .on('data', (data) => results.push(data))
        .on('end', async () => {
            console.log(`Parsed ${results.length} rows. Uploading to Firestore...`);
            
            let uploadedCount = 0;
            const batchSize = 500;
            let batch = db.batch();
            let batchCount = 0;

            for (const row of results) {
                // Dynamically map from whatever columns the Web Scraper outputted
                const commodity = row['Product Name'] || row['Commodity'] || 'Unknown Commodity';
                const buyer_country = row['Buyer Country'] || row['Country'] || 'Unknown Country';
                const raw_inquiry_text = row['Inquiry Description'] || row['Inquiry/RFQ'] || '';
                const source_url = row['Source URL'] || row['URL'] || 'Manual Scraper';
                
                const company_name = row['Company Name'] || 'Unknown / Confidential';
                
                // Format directly into the requested NoSQL schema
                const document = {
                    commodity: commodity,
                    region: row['Region'] || getRegion(buyer_country),
                    buyer_country: buyer_country,
                    certification_tier: determineCertificationTier(raw_inquiry_text),
                    raw_inquiry_text: raw_inquiry_text,
                    source_url: source_url,
                    contact_enrichment: {
                        company_name: company_name,
                        linkedin_profile_url: row['LinkedIn Profile URL'] || "",
                        target_decision_maker: "Procurement / Sourcing Manager",
                        enrichment_status: "PENDING"
                    },
                    system_metadata: {
                        ingested_by: "Antigravity_MCP_Pipeline",
                        created_at: admin.firestore.FieldValue.serverTimestamp(),
                        is_active_lead: true
                    }
                };

                const docRef = db.collection(collectionName).doc();
                batch.set(docRef, document);
                batchCount++;
                uploadedCount++;

                // Commit batch when size limit is reached
                if (batchCount === batchSize) {
                    await batch.commit();
                    console.log(`Committed batch of ${batchSize} records.`);
                    batch = db.batch();
                    batchCount = 0;
                }
            }

            // Commit any remaining documents in the final batch
            if (batchCount > 0) {
                await batch.commit();
                console.log(`Committed final batch of ${batchCount} records.`);
            }

            console.log(`✅ Successfully ingested ${uploadedCount} real RFQ records into Firestore!`);
            process.exit(0);
        });
}

// Execute with passed filename
const args = process.argv.slice(2);
if (args.length === 0) {
    console.error("Please provide the path to your CSV file. Example: node upload_global_rfqs.mjs my_scraped_data.csv");
    process.exit(1);
}

uploadData(args[0]);
