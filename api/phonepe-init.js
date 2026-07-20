import { StandardCheckoutClient, StandardCheckoutPayRequest, Env } from '@phonepe-pg/pg-sdk-node';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const { amount, planName } = req.body;
    
    const clientId = 'SU2605121559051708821219';
    const clientSecret = '83ca7930-383d-4f0d-a8f1-15a65209cbc4';
    const clientVersion = 1;
    const env = Env.PRODUCTION;

    const client = StandardCheckoutClient.getInstance(clientId, clientSecret, clientVersion, env);
    
    // Generate unique transaction ID
    const merchantOrderId = 'MT' + Date.now() + Math.floor(Math.random() * 1000);
    const amountInPaisa = amount * 100;

    const request = StandardCheckoutPayRequest.builder()
        .merchantOrderId(merchantOrderId)
        .amount(amountInPaisa)
        .redirectUrl('https://apdglobaltrade.com/payment-status.html')
        .build();

    console.log("Initiating PhonePe V2 PG Payment for", planName, "Amount:", amount);

    const response = await client.pay(request);

    if (response && response.redirectUrl) {
      return res.status(200).json({ success: true, url: response.redirectUrl });
    } else {
      return res.status(400).json({ success: false, error: "Gateway mapping error or invalid keys" });
    }
    
  } catch (err) {
    console.error("PhonePe V2 API Error:", err);
    return res.status(500).json({ success: false, error: err.message });
  }
}
