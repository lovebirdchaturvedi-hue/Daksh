const fs = require('fs');
const file = 'C:/Users/DELL/.gemini/antigravity/playground/vacant-ride/daksh_repo/admin.html';
let content = fs.readFileSync(file, 'utf8');

// 1. Increase timeout to 8 seconds
content = content.replace('reject(new Error("Firebase Query Timeout - Connection Blocked or Hanging!")), 2000', 'reject(new Error("Firebase Query Timeout - Connection Blocked or Hanging!")), 8000');

// 2. Fix innerHTML O(N^2) DOM freeze
const oldForEach = `    snap.forEach(d => {
      const s = d.data();`;

const newForEach = `    let htmlOutput = "";
    snap.forEach(d => {
      const s = d.data();`;
      
content = content.replace(oldForEach, newForEach);

// Replace tbody.innerHTML += with htmlOutput +=
content = content.replace(/tbody\.innerHTML \+= `/g, 'htmlOutput += `');

// Assign htmlOutput to tbody after loop
const endLoop = `    });

  } catch (err) {`;
const newEndLoop = `    });
    
    tbody.innerHTML = htmlOutput;

  } catch (err) {`;
content = content.replace(endLoop, newEndLoop);

fs.writeFileSync(file, content);
console.log('Fixed DOM freezing issue');
