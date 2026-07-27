import requests
import json

API_KEY = "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs"
PROJECT_ID = "apd-globaltrade-prod"
EMAIL = "demo@apdglobaltrade.com"
PASSWORD = "Demo1234"

print("1. Creating User in Firebase Auth...")
auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
res = requests.post(auth_url, json={"email": EMAIL, "password": PASSWORD, "returnSecureToken": True})

if res.status_code == 200:
    uid = res.json()["localId"]
    print(f"User created with UID: {uid}")
elif "EMAIL_EXISTS" in res.text:
    print("User already exists. Logging in to get UID...")
    login_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    l_res = requests.post(login_url, json={"email": EMAIL, "password": PASSWORD, "returnSecureToken": True})
    uid = l_res.json()["localId"]
    print(f"Logged in. UID: {uid}")
else:
    print("Error:", res.text)
    exit(1)

print("2. Setting up Firestore Document for Demo Account...")
doc_url = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/suppliers/{uid}"
doc_data = {
    "fields": {
        "companyName": {"stringValue": "Demo Supplier Ltd."},
        "email": {"stringValue": EMAIL},
        "status": {"stringValue": "approved"},
        "plan": {"stringValue": "platinum"},
        "totalCredits": {"integerValue": 9999},
        "unlocksUsed": {"integerValue": 0},
        "allowedCategories": {
            "arrayValue": {
                "values": [{"stringValue": "all"}]
            }
        },
        "role": {"stringValue": "supplier"}
    }
}

# The REST API for Firestore uses PATCH to create/update with documentId specified in URL if we append ?updateMask... but it's easier to use the create endpoint or just use requests.patch
res_fs = requests.patch(doc_url, json=doc_data)
if res_fs.status_code == 200:
    print("Demo account successfully configured in Firestore!")
else:
    print("Error writing to Firestore:", res_fs.text)
