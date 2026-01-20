/**
 * ======================================
 * Firebase Functions – TEST VERSION
 * Project: apd-globaltrade-prod
 * Purpose: Verify functions deploy correctly
 * ======================================
 */

const { onCall } = require("firebase-functions/v2/https");
const { onDocumentCreated } = require("firebase-functions/v2/firestore");
const admin = require("firebase-admin");

// Initialize Firebase Admin SDK
admin.initializeApp();

/**
 * 1️⃣ TEST CALLABLE FUNCTION
 * This proves callable v2 functions deploy
 */
exports.testCallable = onCall(async () => {
  return { status: "ok", message: "Callable function working" };
});

/**
 * 2️⃣ TEST FIRESTORE TRIGGER
 * This proves Firestore v2 triggers deploy
 */
exports.testFirestore = onDocumentCreated(
  "test/{docId}",
  async (event) => {
    console.log("Firestore trigger fired for doc:", event.data?.id);
  }
);
