/**
 * ======================================
 * APD Global Trade – Firebase Functions
 * (ALL v2 – SAFE & FUTURE PROOF)
 * ======================================
 */

const { onCall } = require("firebase-functions/v2/https");
const { onDocumentCreated } = require("firebase-functions/v2/firestore");
const admin = require("firebase-admin");
const nodemailer = require("nodemailer");

admin.initializeApp();

/* ======================================================
   1️⃣ CREATE ADMIN USER (CALLABLE – v2)
   ====================================================== */
exports.createAdminUser = onCall(async (request) => {
  const callerUid = request.auth?.uid;
  if (!callerUid) {
    throw new Error("Not authenticated");
  }

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

  const user = await admin.auth().createUser({
    email,
    password
  });

  await admin.firestore().collection("admins").doc(user.uid).set({
    email,
    role: "admin",
    createdAt: admin.firestore.FieldValue.serverTimestamp()
  });

  return { success: true };
});


/* ======================================================
   2️⃣ EMAIL TRANSPORT (TEMP – SENDGRID LATER)
   ====================================================== */
const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: "lovebird.chaturvedi@gmail.com",
    pass: "ybqrsemuigudhtxl"
  }
});


/* ======================================================
   3️⃣ NOTIFY ADMIN ON SUPPLIER SIGNUP (FIRESTORE v2)
   ====================================================== */
exports.notifyNewSupplier = onDocumentCreated(
  "suppliers/{supplierId}",
  async (event) => {

    const data = event.data?.data();
    if (!data) return;

    const mailOptions = {
      from: "APD Global Trade <lovebird.chaturvedi@gmail.com>",
      to: "admin@apdglobaltrade.com",
      subject: "🆕 New Supplier Registration – APD Global Trade",
      html: `
        <h2>New Supplier Signed Up</h2>
        <p><b>Name:</b> ${data.name || "-"}</p>
        <p><b>Company:</b> ${data.company || "-"}</p>
        <p><b>Email:</b> ${data.email || "-"}</p>
        <p><b>Country:</b> ${data.country || "-"}</p>
        <p><b>Phone:</b> ${data.phone || "-"}</p>
        <p><b>Time:</b> ${new Date().toLocaleString()}</p>
      `
    };

    try {
      await transporter.sendMail(mailOptions);
    } catch (err) {
      console.error("Email failed:", err.message);
    }
  }
);
