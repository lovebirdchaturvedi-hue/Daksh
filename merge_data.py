import pandas as pd
import numpy as np

print("Merging Buyers...")
old_buyers_path = r'C:\Users\DELL\Downloads\Daksh\REAL BUYERS 2026.xlsx'
new_buyers_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL BUYERS 2026.xlsx'

old_buyers = pd.read_excel(old_buyers_path)
new_buyers = pd.read_excel(new_buyers_path)

merged_buyers = pd.concat([old_buyers, new_buyers], ignore_index=True)

# Replace empty strings with NaN so drop_duplicates logic works well
merged_buyers['Email'] = merged_buyers['Email'].replace(r'^\s*$', np.nan, regex=True)

# Separate the dataframe into rows with and without emails
with_emails = merged_buyers[merged_buyers['Email'].notna()]
without_emails = merged_buyers[merged_buyers['Email'].isna()]

# Deduplicate ONLY the rows that actually have an email
with_emails = with_emails.drop_duplicates(subset=['Email'], keep='first')

# Combine them back together
final_buyers = pd.concat([with_emails, without_emails], ignore_index=True)
final_buyers.to_excel(new_buyers_path, index=False)
print(f"Total Combined Buyers: {len(final_buyers)}")


print("Merging Exporters...")
old_exp_path = r'C:\Users\DELL\Downloads\Daksh\Exporters 2026.xlsx'
new_exp_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL EXPORTERS 2026.xlsx'

old_exp = pd.read_excel(old_exp_path)
new_exp = pd.read_excel(new_exp_path)

merged_exp = pd.concat([old_exp, new_exp], ignore_index=True)
merged_exp['Email'] = merged_exp['Email'].replace(r'^\s*$', np.nan, regex=True)
with_emails_exp = merged_exp[merged_exp['Email'].notna()]
without_emails_exp = merged_exp[merged_exp['Email'].isna()]
with_emails_exp = with_emails_exp.drop_duplicates(subset=['Email'], keep='first')
final_exp = pd.concat([with_emails_exp, without_emails_exp], ignore_index=True)

final_exp.to_excel(new_exp_path, index=False)
print(f"Total Combined Exporters: {len(final_exp)}")
