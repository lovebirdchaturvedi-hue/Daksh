export default async function handler(req, res) {
    // Only allow POST requests
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    const { instance, token, to, body } = req.body;

    if (!instance || !token || !to || !body) {
        return res.status(400).json({ error: 'Missing API credentials or message data.' });
    }

    try {
        // Ultramsg STRICTLY requires the token in the URL, even for POST requests
        const url = `https://api.ultramsg.com/${instance}/messages/chat?token=${token}`;
        
        // Encode payload exactly as Ultramsg requires (without token)
        const params = new URLSearchParams({
            'to': to,
            'body': body,
            'priority': '10'
        });

        // Make the server-to-server request
        const response = await fetch(url, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/x-www-form-urlencoded' 
            },
            body: params
        });

        const data = await response.json();
        
        // Return the exact response back to the CRM
        return res.status(200).json(data);
        
    } catch (error) {
        console.error("Vercel Backend Error:", error);
        return res.status(500).json({ error: error.message });
    }
}
