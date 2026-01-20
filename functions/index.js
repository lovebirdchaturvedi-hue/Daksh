const { onCall } = require("firebase-functions/v2/https");
const { onDocumentCreated } = require("firebase-functions/v2/firestore");
const admin = require("firebase-admin");

admin.initializeApp();

/**
 * 1️⃣ CREATE ADMIN USER (CALLABLE)
 */
exports.createAdminUser = onCall(async (request) => {
  const callerUid = request.auth?.uid;
  if (!callerUid) throw new Error("Not authenticated");

  const adminDoc = await admin.firestore().collection("admins").doc(callerUid).get();
  if (!adminDoc.exists) throw new Error("Not authorized");

  const { email, password } = request.data;
  if (!email || !password) throw new Error("Email & password required");

  const user = await admin.auth().createUser({ email, password });

  await admin.firestore().collection("admins").doc(user.uid).set({
    email,
    role: "admin",
    createdAt: admin.firestore.FieldValue.serverTimestamp()
  });

  return { success: true };
});

/**
 * 2️⃣ FIRESTORE TRIGGER – SUPPLIER SIGNUP
 */
exports.notifyNewSupplier = onDocumentCreated(
  "suppliers/{supplierId}",
  async (event) => {
    const data = event.data?.data();
    if (!data) return;

    console.log("New supplier registered:", data.email || "unknown");
  }
);
