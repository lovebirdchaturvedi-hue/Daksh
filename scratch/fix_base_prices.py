import os

index_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

index_html = index_html.replace('₹19,999', '₹59,000')
index_html = index_html.replace('₹84,999', '₹1,68,000')
index_html = index_html.replace('₹1,49,999', '₹2,94,000')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
