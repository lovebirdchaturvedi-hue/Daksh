const https = require('https');
https.get('https://apdglobaltrade.com/admin.html', (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    if (data.includes('del(\\'')) {
      console.log('Vercel is serving the BROKEN version! (Single quote escape)');
    } else if (data.includes('del(\\"')) {
      console.log('Vercel is serving the FIXED version! (Double quotes)');
    } else {
      console.log('Cannot find either version. Here is the string near isLegacy:');
      console.log(data.substring(data.indexOf('isLegacy'), data.indexOf('isLegacy') + 200));
    }
  });
}).on('error', (err) => console.error(err));
