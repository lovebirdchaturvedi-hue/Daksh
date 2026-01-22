const { onCall } = require("firebase-functions/v2/https");
const admin = require("firebase-admin");

admin.initializeApp();

exports.setAdmin = onCall(async (request) => {
  const email = request.data.email;
  if (!email) throw new Error("Email required");

  const user = await admin.auth().getUserByEmail(email);

  await admin.auth().setCustomUserClaims(user.uid, {
    admin: true
  });

  return { success: true };
});
