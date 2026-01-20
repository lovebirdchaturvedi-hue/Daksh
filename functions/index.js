/**
 * ======================================
 * APD Global Trade – Firebase Functions
 * ======================================
 */

const { onCall } = require("firebase-functions/v2/https");
const functions = require("firebase-functions/v1");
const admin = require("firebase-admin");
const nodemailer = require("nodemailer");

// 🔥 Initialize Firebase Admin
admin.initializeApp();

/* ======================================================
   1️⃣ CREATE ADMIN USER (CALLABLE FUNCTION)
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
   2️⃣ EMAIL TRANSPORT (TEMP – WILL SWITCH TO SENDGRID)
   ====================================================== */
const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: "lovebird.chaturvedi@gmail.com",
    pass: "ybqrsemuigudhtxl"
  }
});


/* ======================================================
   3️⃣ NOTIFY ADMIN WHEN SUPPLIER SIGNS UP
   ====================================================== */
exports.notifyNewSupplier = functions.firestore
  .document("suppliers/{supplierId}")
  .onCreate(async (snap) => {

    const data = snap.data();

    const mailOptions = {
      from: "APD Global Trade <lovebird.chaturvedi@gmail.com>",
      to: "lovebird.chaturvedi@gmail.com",
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
      console.error("Email send failed:", err.message);
    }

    return null;
  });
