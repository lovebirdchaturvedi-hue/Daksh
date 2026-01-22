import { initializeApp } from
"https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";

import { getAuth } from
"https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const firebaseConfig = {
  apiKey: "XXXX",
  authDomain: "apd-global-trade.firebaseapp.com",
  projectId: "apd-global-trade",
  appId: "XXXX"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
