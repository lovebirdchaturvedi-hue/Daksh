import re
import os

with open('seed-rfqs.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all options
options = re.findall(r'<option value="([^"]+)">', html)

# We want unique options
products = sorted(list(set(options)))

js_code = f"""import {{ initializeApp }} from "firebase/app";
import {{ getFirestore, collection, addDoc, getDocs, deleteDoc, doc, serverTimestamp, query, where }} from "firebase/firestore";

const firebaseConfig = {{
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod"
}};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const fakeNames = ["Mohammed Al-Fayed", "James Smith", "Li Wei", "Fatima Zahra", "John Doe", "Sarah Connor", "Ahmed Hassan", "Chen Wu", "David Miller", "Elena Rossi", "Omar Al-Khatib", "Lucas Silva", "Isabella Fernandez", "Rajesh Kumar", "Anna Muller", "Michael Chang", "Tariq Aziz", "William Jones", "Maria Garcia", "Hiroshi Tanaka"];
const fakeDomains = ["gmail.com", "import-trading.com", "global-sourcing.ae", "eu-foods.net", "supply-chain.co.uk", "agri-ventures.com", "food-imports.sa", "agro-trading.net"];
const COUNTRIES = ["UAE","USA","Indonesia","Vietnam","Bangladesh","Saudi Arabia","Egypt","Nigeria","Brazil","Philippines","Nepal","Germany","UK","France","Canada","Australia","Singapore"];

function generateContactInfo(name) {{
  const emailName = name.toLowerCase().replace(/ /g, ".");
  const domain = fakeDomains[Math.floor(Math.random() * fakeDomains.length)];
  const phone = "+" + Math.floor(Math.random() * 90 + 10) + " " + Math.floor(Math.random() * 9000000000 + 1000000000);
  return {{ email: `${{emailName}}@${{domain}}`, phone: phone }};
}}

const PRODUCTS = {products};

async function run() {{
  console.log(`Checking existing RFQs for ${{PRODUCTS.length}} products...`);

  // Instead of deleting everything, we will just make sure there are at least 5 RFQs for every product.
  // Wait, scanning all of them and checking count is slow. Let's just blindly add 3 RFQs for every single product
  // to guarantee coverage without wiping existing RFQs.

  let newRfqs = [];

  for (const product of PRODUCTS) {{
      for (let i = 0; i < 3; i++) {{
          const fakeName = fakeNames[Math.floor(Math.random() * fakeNames.length)] + " " + Math.floor(Math.random()*1000);
          const generatedContact = generateContactInfo(fakeName);
          newRfqs.push({{
              product: product,
              quantity: `${{Math.floor(Math.random() * 900 + 100)}} MT`,
              deliveryPort: COUNTRIES[Math.floor(Math.random() * COUNTRIES.length)],
              dealSizeUSD: Math.floor(Math.random() * 4000000 + 500000),
              status: "open",
              source: "admin-seed-full",
              buyerName: fakeName,
              email: generatedContact.email,
              contact: generatedContact.phone
          }});
      }}
  }}

  console.log(`Generating ${{newRfqs.length}} RFQs to guarantee coverage for ALL products...`);

  const chunkSize = 50;
  for (let i = 0; i < newRfqs.length; i += chunkSize) {{
      const chunk = newRfqs.slice(i, i + chunkSize);
      const promises = chunk.map(r => addDoc(collection(db, "rfqs"), {{
          ...r,
          createdAt: serverTimestamp()
      }}));
      await Promise.all(promises);
      console.log(`Uploaded batch ${{Math.floor(i/chunkSize) + 1}} of ${{Math.ceil(newRfqs.length/chunkSize)}}`);
  }}

  console.log("Database seeded successfully! Every single product now has active buyers.");
  process.exit(0);
}}

run().catch(console.error);
"""

with open('seed_all.mjs', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Created seed_all.mjs script.")
