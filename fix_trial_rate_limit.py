import re

file_path = 'supplier-dashboard.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update the renderMockLeads call
content = content.replace(
    'renderMockLeads(s.product || "General", user.uid, unlocksUsed, TRIAL_CREDITS);',
    'renderMockLeads(s.product || "General", user.uid, unlocksUsed, TRIAL_CREDITS, s);'
)

# Update the function definition
content = content.replace(
    'async function renderMockLeads(commodity, uid, unlocksUsed, maxCredits) {',
    'async function renderMockLeads(commodity, uid, unlocksUsed, maxCredits, supplierData) {'
)

# Insert the rate limit check inside the button click
target_btn_click = 'if (freeCredits > 0) {'
replacement_btn_click = '''if (freeCredits > 0) {
              const todayStr = new Date().toISOString().split('T')[0];
              if (supplierData && supplierData.lastFreeUnlockDate === todayStr) {
                  alert("You have already unlocked a lead today. Your trial provides 1 free lead per day. Please come back tomorrow or upgrade to Premium for unlimited access.");
                  return;
              }
'''
if replacement_btn_click not in content:
    content = content.replace(target_btn_click, replacement_btn_click, 1)

# Insert the update of lastFreeUnlockDate
target_update = "await updateDoc(doc(db, 'suppliers', uid), { unlocksUsed: increment(1) });"
replacement_update = '''await updateDoc(doc(db, 'suppliers', uid), { 
                      unlocksUsed: increment(1),
                      lastFreeUnlockDate: new Date().toISOString().split('T')[0]
                  });
                  if (supplierData) { supplierData.lastFreeUnlockDate = new Date().toISOString().split('T')[0]; }'''
if replacement_update not in content:
    content = content.replace(target_update, replacement_update)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated supplier-dashboard.html with 1-lead-per-day logic")
