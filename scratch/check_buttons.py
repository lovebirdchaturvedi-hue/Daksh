import sys
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'Live Order' in line and '<a' in line:
        sys.stdout.buffer.write(f'Line {i+1}: '.encode('utf-8'))
        sys.stdout.buffer.write(line.strip().encode('utf-8'))
        sys.stdout.buffer.write(b'\n')
