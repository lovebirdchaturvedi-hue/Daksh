import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix ELITE TRADE CYCLE
old_trade_cycle = 'display: flex; justify-content: center; gap: 40px; margin: 40px 0; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px;'
new_trade_cycle = 'display: flex; justify-content: center; gap: 15px; margin: 40px 0; font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; flex-wrap: wrap; padding: 0 10px; box-sizing: border-box;'
content = content.replace(old_trade_cycle, new_trade_cycle)

# Fix INSTITUTIONAL NETWORK SHIELDS
old_shields = 'display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; margin-top: 20px;'
new_shields = 'display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; margin-top: 20px; padding: 0 10px; box-sizing: border-box;'
content = content.replace(old_shields, new_shields)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated inline styles for RFQ Signal and Shields to prevent horizontal overflow.")
