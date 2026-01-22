const { onCall } = require("firebase-functions/v2/https");
const admin = require("firebase-admin");

// Initialize Firebase Admin SDK ONCE
admin.initializeApp();

// Callable function to set admin role
exports.setAdmin = onCall(async (request) => {
  const email = request.data.email;

  if (!email) {
    throw new Error("Email is required");
  }

  // Get user by email
  const user = await admin.auth().getUserByEmail(email);

  // Set custom admin claim
  await admin.auth().setCustomUserClaims(user.uid, {
    admin: true
  });

  return {
    success: true,
    message: `Admin role assigned to ${email}`
  };
});
