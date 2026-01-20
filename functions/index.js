/**
 * APD Global Trade – Firebase Functions
 * - Approve supplier (HTTP v2)
 * - Email admin on new supplier registration
 */

const { onRequest } = require("firebase-functions/v2/https");
const { onDocumentCreated } = require("firebase-functions/v2/firestore");
const admin = require("firebase-admin");
const nodemailer = require("nodemailer");

admin.initializeApp();

/* ===============================
   1️⃣ APPROVE SUPPLIER (HTTP)
   =============================== */
exports.approveSupplier = onRequest(async (req, res) => {
  try {
    const supplierId = req.query.supplierId;

    if (!supplierId) {
      return res.status(400).json({ error: "supplierId required" });
    }

    const supplierRef = admin
      .firestore()
      .collection("suppliers")
      .doc(supplierId);

    const snap = await supplierRef.get();

    if (!snap.exists) {
      return res.status(404).json({ error: "Supplier not found" });
    }

    await supplierRef.update({
      approved: true,
      approvedAt: admin.firestore.FieldValue.serverTimestamp(),
    });

    res.json({ success: true });
  } catch (error) {
    console.error("approveSupplier error:", error);
    res.status(500).json({ error: error.message });
  }
});

/* =========================================
   2️⃣ EMAIL ADMIN WHEN SUPPLIER REGISTERS
   ========================================= */

// Read env config
const config = JSON.parse(process.env.FIREBASE_CONFIG || "{}");

const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: config.email_user,
    pass: config.email_pass,
  },
});

exports.notifyAdminOnSupplierRegister = onDocumentCreated(
  "suppliers/{supplierId}",
  async (event) => {
    try {
      const data = event.data?.data();
      if (!data) return;

      const mailOptions = {
        from: `"APD Global Trade" <${config.email_user}>`,
        to: config.email_admin,
        subject: "🆕 New Supplier Registration",
        html: `
          <h2>New Supplier Registered</h2>
          <p><b>Company:</b> ${data.companyName || "N/A"}</p>
          <p><b>Email:</b> ${data.email || "N/A"}</p>
          <p><b>Country:</b> ${data.country || "N/A"}</p>
          <p><b>Status:</b> Pending Approval</p>
        `,
      };

      await transporter.sendMail(mailOptions);
    } catch (err) {
      console.error("Email notification failed:", err);
    }
  }
);
