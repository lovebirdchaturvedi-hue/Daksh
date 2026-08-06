import Razorpay from 'razorpay';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    let { amount, currency = 'INR', receipt = 'receipt_' + Date.now() } = req.body;
    
    // Convert to subunits (paise for INR, cents for USD)
    amount = Math.round(amount * 100);

    if (!amount || amount < 100) {
        return res.status(400).json({ error: 'Invalid amount (minimum 1 INR/USD)' });
    }

    const instance = new Razorpay({
      key_id: process.env.RAZORPAY_KEY_ID,
      key_secret: process.env.RAZORPAY_KEY_SECRET,
    });

    const options = {
      amount: amount, // amount in smallest currency unit (paise)
      currency: currency,
      receipt: receipt
    };

    const order = await instance.orders.create(options);
    
    if (!order) {
        return res.status(500).json({ error: 'Failed to create order' });
    }

    return res.status(200).json(order);
  } catch (err) {
    console.error("Razorpay Create Order Error:", err);
    return res.status(500).json({ error: err.message || 'Internal Server Error' });
  }
}
