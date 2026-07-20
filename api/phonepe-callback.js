export default async function handler(req, res) {
  // PhonePe Server-to-Server Webhook Acknowledgment
  if (req.method === 'POST') {
    console.log("PhonePe Webhook Received:", req.body);
    
    // In a full DB setup, you would verify the X-VERIFY checksum here
    // and update the user's membership status in Firebase.
    
    // Always return 200 OK so PhonePe knows we received it
    res.status(200).send('OK');
  } else {
    res.status(405).json({ error: 'Method Not Allowed' });
  }
}
