import sys
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'mobile-trade-ticker' in line and '<div' in line:
        for j in range(i-2, i+15):
            if j < len(lines):
                sys.stdout.buffer.write(lines[j].encode('utf-8'))
        break
