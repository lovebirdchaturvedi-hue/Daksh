import sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['index.html', 'membership.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"\n=== {fname} ===")
    for i, line in enumerate(lines):
        if 'suresh' in line.lower() or 'patel' in line.lower():
            print(f'Line {i+1}: {line.rstrip()[:150]}')
