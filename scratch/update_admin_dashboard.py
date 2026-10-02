import codecs

with codecs.open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update the table headers
header_target = "<th>Status</th>"
new_header = "<th>Status</th>\n<th>Compliance (T&C)</th>"
text = text.replace(header_target, new_header)

# 2. Update the HTML output string inside renderUsers
# Looking at the original string:
# <td><b>${s.status || "pending"}</b></td>
# <td style="font-size:12px;">${planName}</td>
old_html_output = """<td><b>${s.status || "pending"}</b></td>
          <td style="font-size:12px;">${planName}</td>"""

new_html_output = """<td><b>${s.status || "pending"}</b></td>
          <td>${s.tcSigned ? '<span style="background:#16a34a; color:white; padding:3px 6px; border-radius:4px; font-size:10px; font-weight:bold;">SIGNED</span>' : '<span style="background:#ef4444; color:white; padding:3px 6px; border-radius:4px; font-size:10px; font-weight:bold;">PENDING</span>'}</td>
          <td style="font-size:12px;">${planName}</td>"""

text = text.replace(old_html_output, new_html_output)

# 3. We also need to update colspan in loading/empty messages from 12 to 13
text = text.replace("colspan='12'", "colspan='13'")

with codecs.open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated admin.html successfully.")
