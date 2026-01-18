const functions = require("firebase-functions");
const admin = require("firebase-admin");

admin.initializeApp();

exports.approveSupplier = functions.https.onRequest(async (req, res) => {
  try {
    const { supplierId } = req.body;

    if (!supplierId) {
      return res.status(400).send("Supplier ID required");
    }

    const db = admin.firestore();
    const supplierRef = db.collection("suppliers").doc(supplierId);
    const supplierSnap = await supplierRef.get();

    if (!supplierSnap.exists) {
      return res.status(404).send("Supplier not found");
    }

    const supplier = supplierSnap.data();

    if (supplier.status === "approved") {
      return res.status(200).send("Already approved");
    }

    const user = await admin.auth().createUser({
      email: supplier.email,
      password: "Temp@12345"
    });

    await admin.auth().setCustomUserClaims(user.uid, {
      role: "supplier"
    });

    await supplierRef.update({
      status: "approved",
      authUid: user.uid,
      approvedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    res.status(200).send("Supplier approved successfully");

  } catch (error) {
    console.error(error);
    res.status(500).send(error.message);
  }
});
