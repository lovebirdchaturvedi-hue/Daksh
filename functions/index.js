const { onCall } = require("firebase-functions/v2/https");
const { onDocumentCreated } = require("firebase-functions/v2/firestore");
const admin = require("firebase-admin");

admin.initializeApp();

exports.testCallable = onCall(async () => {
  return { status: "ok" };
});

exports.testFirestore = onDocumentCreated(
  "test/{docId}",
  async (event) => {
    console.log("Firestore trigger fired");
  }
);
