repo = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo"

with open(repo + r"\admin.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update plan names and prices in admin.html

# Old 3-month plan references
content = content.replace("'Growth Program (3 Months)'", "'Professional Pass (3 Months)'")
content = content.replace('"Growth Program (3 Months)"', '"Professional Pass (3 Months)"')
content = content.replace("Growth Program", "Professional Pass")
content = content.replace("19999", "29500")
content = content.replace("19,999", "29,500")
content = content.replace("$249", "$349")

# Old 6-month plan references
content = content.replace("'Institutional Elite (6 Months)'", "'Institutional Elite (6 Months)'")
content = content.replace("51000", "75000")
content = content.replace("51,000", "75,000")
content = content.replace("$599", "$799")

# Old 12-month plan references
content = content.replace("119000", "149000")
content = content.replace("1,19,000", "1,49,000")
content = content.replace("119,000", "149,000")
content = content.replace("$999", "$1,499")

with open(repo + r"\admin.html", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: admin.html plan names and prices updated!")
