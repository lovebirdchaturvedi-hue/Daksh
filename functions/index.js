const { onCall } = require("firebase-functions/v2/https");
const admin = require("firebase-admin");

admin.initializeApp();

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
