import codecs
import re
import glob

html_files = glob.glob('*.html')

for file in html_files:
    try:
        with codecs.open(file, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()

        changed = False
        
        # We need to specifically target the trial plan boxes.
        if 'CONFUSED?' in text or 'Get 3 Verified Buyers' in text:
            # 3 BUYERS PLAN replacement
            # Find the block for 3 buyers and its button
            box3_start = text.find('Get 3 Verified Buyers')
            if box3_start != -1:
                box3_end = text.find('trial-box-premium', box3_start)
                if box3_end == -1: box3_end = box3_start + 1500
                
                box3_content = text[box3_start:box3_end]
                new_box3 = box3_content.replace('href="/membership.html"', 'href="/membership.html?plan=3buyers"')
                text = text[:box3_start] + new_box3 + text[box3_end:]
                changed = True

            # 5 BUYERS PLAN replacement
            box5_start = text.find('Get 5 Verified Buyers')
            if box5_start != -1:
                box5_end = box5_start + 1500
                box5_content = text[box5_start:box5_end]
                new_box5 = box5_content.replace('href="/membership.html"', 'href="/membership.html?plan=5buyers"')
                text = text[:box5_start] + new_box5 + text[box5_end:]
                changed = True
                
        if changed:
            with codecs.open(file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Updated links in {file}")
            
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Now, we need to update membership.html to handle ?plan=3buyers and ?plan=5buyers
with codecs.open('membership.html', 'r', encoding='utf-8', errors='ignore') as f:
    mem_text = f.read()

js_insert = """
    window.addEventListener('DOMContentLoaded', () => {
        const urlParams = new URLSearchParams(window.location.search);
        const plan = urlParams.get('plan');
        
        if (plan === '3buyers') {
            setTimeout(() => {
                initiatePayment('3 Verified Buyers Trial', 149, 9999);
                // Dynamically update the main membership heading so they know what they are paying for
                document.querySelector('.membership-header h1').innerHTML = "You're getting <span style='color: #facc15;'>3 Verified Buyers</span>";
                document.querySelector('.membership-header p').innerHTML = "Complete your secure payment below to instantly unlock your institutional buyer contacts.";
            }, 500);
        } else if (plan === '5buyers') {
            setTimeout(() => {
                initiatePayment('5 Verified Buyers Trial', 199, 14900);
                document.querySelector('.membership-header h1').innerHTML = "You're getting <span style='color: #facc15;'>5 Verified Buyers</span>";
                document.querySelector('.membership-header p').innerHTML = "Complete your secure payment below to instantly unlock your institutional buyer contacts.";
            }, 500);
        }
    });
"""

if 'plan === \'3buyers\'' not in mem_text:
    # insert before the closing script tag of the DOMContentLoaded block, or just append before </script> at the bottom.
    idx = mem_text.rfind('</script>')
    mem_text = mem_text[:idx] + js_insert + mem_text[idx:]
    with codecs.open('membership.html', 'w', encoding='utf-8') as f:
        f.write(mem_text)
    print("Injected URL parameter handler into membership.html")

