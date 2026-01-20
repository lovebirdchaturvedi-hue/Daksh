/**
 * ================================
 * APD Global Trade – Cloud Functions
 * ================================
 */

const { onCall } = require("firebase-functions/v2/https");
const functions = require("firebase-functions");
const admin = require("firebase-admin");
const nodemailer = require("nodemailer");

// 🔥 Initialize Firebase Admin (ONLY ONCE)
admin.initializeApp();

/* ======================================================
   1️⃣ CREATE ADMIN USER (CALLABLE FUNCTION – v2)
   ====================================================== */
exports.createAdminUser = onCall(async (request) => {
  const callerUid = request.auth?.uid;
  if (!callerUid) {
    throw new Error("Not authenticated");
  }

  // 🔐 Verify caller is admin
  const adminDoc = await admin
    .firestore()
    .collection("admins")
    .doc(callerUid)
    .get();

  if (!adminDoc.exists) {
    throw new Error("Not authorized");
  }

  const { email, password } = request.data;

  if (!email || !password) {
    throw new Error("Email & password required");
  }

  // 👤 Create Firebase Auth user
  const user = await admin.auth().createUser({
    email,
    password
  });

  // 📄 Add to admins collection
  await admin.firestore().collection("admins").doc(user.uid).set({
    email,
    role: "admin",
    createdAt: admin.firestore.FieldValue.serverTimestamp()
  });

  return { success: true };
});


/* ======================================================
   2️⃣ EMAIL CONFIG (USED BY ALL EMAIL FUNCTIONS)
   ====================================================== */
// ⚠️ Use SAME Gmail + App Password as RFQ emails
const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: "lovebird.chaturvedi@gmail.com",
    pass: "ybqrsemuigudhtxl"
  }
});


/* ======================================================
   3️⃣ NOTIFY ADMIN ON NEW SUPPLIER SIGNUP
   ====================================================== */
exports.notifyNewSupplier = functions.firestore
  .document("suppliers/{supplierId}")
  .onCreate(async (snap, context) => {

    const data = snap.data();

    const mailOptions = {
      from: "APD Global Trade <YOUR_EMAIL@gmail.com>",
      to: "YOUR_ADMIN_EMAIL@gmail.com",
      subject: "🆕 New Supplier Registration – APD Global Trade",
      html: `
        <h2>New Supplier Signed Up</h2>
        <hr/>
        <p><strong>Name:</strong> ${data.name || "-"}</p>
        <p><strong>Company:</strong> ${data.company || "-"}</p>
        <p><strong>Email:</strong> ${data.email || "-"}</p>
        <p><strong>Country:</strong> ${data.country || "-"}</p>
        <p><strong>Phone:</strong> ${data.phone || "-"}</p>
        <p><strong>Submitted At:</strong> ${new Date().toLocaleString()}</p>
        <br/>
        <p>Please review this supplier in the Admin Dashboard.</p>
      `
    };

    await transporter.sendMail(mailOptions);
    return null;
  });
