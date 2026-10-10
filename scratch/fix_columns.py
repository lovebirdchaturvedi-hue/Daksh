import codecs
import re

with codecs.open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'(<td><b>\$\{s\.status \|\| "pending"\}</b></td>)\s*<td style="font-size:12px;">\$\{planName\}</td>'
replacement = r'\1\n          <td>${s.tcSigned ? \'<span style="background:#16a34a; color:white; padding:3px 6px; border-radius:4px; font-size:10px; font-weight:bold;">SIGNED</span>\' : \'<span style="background:#ef4444; color:white; padding:3px 6px; border-radius:4px; font-size:10px; font-weight:bold;">PENDING</span>\'}</td>\n          <td style="font-size:12px;">${planName}</td>'

text = re.sub(pattern, replacement, text)

text = text.replace('limit(50)', 'limit(500)')

with codecs.open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed admin table columns and set limit to 500")
