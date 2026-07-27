const fetch = require('node-fetch'); // or native fetch if Node 18+

async function testUltramsg() {
    const instance = "instance168990";
    const token = "yx9xaxy5k1nbqjat";
    const to = "+919266418868";
    const body = "Test from APD Server";

    const url = `https://api.ultramsg.com/${instance}/messages/chat`;
    const params = new URLSearchParams({
        'token': token,
        'to': to,
        'body': body,
        'priority': '10'
    });

    console.log("Sending request to:", url);
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: params
        });
        
        console.log("Status:", response.status);
        const data = await response.json();
        console.log("Response:", JSON.stringify(data, null, 2));
    } catch (e) {
        console.error("Error:", e);
    }
}

testUltramsg();
