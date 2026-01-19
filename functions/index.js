const { onRequest } = require("firebase-functions/v2/https");
const admin = require("firebase-admin");

admin.initializeApp();

/* 🔍 TEST FUNCTION */
exports.testPing = onRequest((req, res) => {
  res.send("PING OK");
});

/*
⚠️ NOTE ABOUT PASSWORD RESET:

Admin should NEVER see or set passwords.
Supplier must reset via Firebase Auth email flow.

This function is intentionally minimal for safety.
*/
