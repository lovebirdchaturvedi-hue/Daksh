/**
 * APD Global Trade – Firebase Functions
 * - Approve supplier (HTTP)
 * - Email admin when supplier registers (Firestore trigger)
 */

const { onRequest } = require("firebase-functions/v2/https");
const { onDocumentCreated } = require("firebase-functions/v2/firestore");
const functions = require("firebase-functions");
const admin = require("firebase-admin");
const nodemailer = require("nodemailer");

admin.initializeApp();

/* ===============================
   APPROVE SUPPLIER (HTTP)
   =============================== */
exports.approveSupplier = onRequest(async (req, res) => {
  try {
    const supplierId = req.query.supplierId;

    if (!supplierId) {
      return res.status(400).json({ error: "supplierId required" });
    }

    const ref = admin.firestore().collection("suppliers").doc(supplierId);
    const snap = await ref.get();

    if (!snap.exists) {
      return res.status(404).json({ error: "Supplier not found" });
    }

    await ref.update({
      approved: true,
      approvedAt: admin.firestore.FieldValue.serverTimestamp(),
    });

    res.json({ success: true });
  } catch (err) {
    console.error("approveSupplier error:", err);
    res.status(500).json({ error: err.message });
  }
});

/* =========================================
   EMAIL ADMIN ON SUPPLIER REGISTER (v2)
   ========================================= */

const emailConfig = functions.config().email;

const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: emailConfig.user,
    pass: emailConfig.pass,
  },
});

exports.notifyAdminOnSupplierRegister = onDocumentCreated(
  "suppliers/{supplierId}",
  async (event) => {
    const data = event.data?.data();
    if (!data) return;

    const mailOptions = {
      from: `"APD Global Trade" <${emailConfig.user}>`,
      to: emailConfig.admin,
      subject: "🆕 New Supplier Registration",
      html: `
        <h2>New Supplier Registered</h2>
        <p><b>Company:</b> ${data.companyName || "N/A"}</p>
        <p><b>Email:</b> ${data.email || "N/A"}</p>
        <p><b>Country:</b> ${data.country || "N/A"}</p>
        <p>Status: Pending Approval</p>
      `,
    };

    await transporter.sendMail(mailOptions);
  }
);
