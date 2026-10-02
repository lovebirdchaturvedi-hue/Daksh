import codecs
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    try:
        with codecs.open(file, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()

        original_text = text

        # 1. Fix the Founder Placeholder
        text = text.replace('PHOTO UPLOAD REQUIRED Save your portrait to: assets/images/founder.jpg', 
                            '')
        # Remove the weird red warning style if it's there
        text = re.sub(r'style="[^"]*color:\s*red[^"]*"', '', text)

        # 2. Rename Retail Pricing
        text = text.replace('Get 3 Verified Buyers', 'Standard Compliance Audit')
        text = text.replace('Get 5 Verified Buyers', 'Enterprise Sourcing Portfolio')
        
        # Professionalize subtext
        text = text.replace('Perfect to test our elite buyer network with absolutely zero risk.', 
                            'Entry-level compliance auditing and B2B matching for emerging exporters.')
        text = text.replace('Maximum ROI. Get 5 highly active institutional buyers and scale faster.', 
                            'Comprehensive institutional matching, dedicated account management, and priority routing.')
        
        # 3. Remove Emojis and Alarmist Text
        text = text.replace('🚨', '')
        text = text.replace('🔥', '')
        text = text.replace('🚀', '')
        text = text.replace('⚡', '')
        text = text.replace('LIMITED OFFER', 'PRIORITY ACCESS')
        text = text.replace('LIVE ORDERS', 'ACTIVE RFQs')
        
        # 4. Remove $25 Refundable Deposit logic and hype
        # Specifically targeting create-rfq.html and footers
        deposit_banner = r'<div style="background: rgba\(34, 197, 94, 0\.1\);.*?</div>'
        text = re.sub(deposit_banner, '', text, flags=re.DOTALL)
        
        text = text.replace('Pay $25 Refundable Deposit & Post Live Order', 'Submit Secure B2B RFQ')
        text = text.replace('Pay $25 Refundable Deposit', 'Secure Verification')

        # 5. Standardize Emails
        text = text.replace('info@apdglobaltrade.com', 'sales@apdglobaltrade.com')

        if text != original_text:
            with codecs.open(file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Updated {file}")

    except Exception as e:
        print(f"Error processing {file}: {e}")

print("Phase 1 execution complete.")
