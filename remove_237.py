import os, re, glob

# Regex to find the Africa Desk block in the wa-hub
block_pattern = re.compile(
    r'<a href="https://wa\.me/237658309636".*?class="wa-hub-item">.*?<div class="desk-name">AFRICA DESK</div>.*?</a>',
    re.DOTALL
)

count_blocks_removed = 0
count_numbers_replaced = 0

for file in glob.glob('*.html'):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        encoding_used = 'utf-8'
    except UnicodeDecodeError:
        with open(file, 'r', encoding='utf-16') as f:
            content = f.read()
        encoding_used = 'utf-16'
    
    new_content = content
    
    # Remove the Africa Desk block completely
    if block_pattern.search(new_content):
        new_content = block_pattern.sub('', new_content)
        count_blocks_removed += 1
    
    # Replace any leftover instances of the number (e.g. action buttons) with the main +91 number
    if '237658309636' in new_content:
        new_content = new_content.replace('237658309636', '919266418868')
        count_numbers_replaced += 1
        
    if new_content != content:
        with open(file, 'w', encoding=encoding_used) as f:
            f.write(new_content)
        print(f'Updated {file}')
        
print(f'Blocks removed: {count_blocks_removed}')
print(f'Other numbers replaced: {count_numbers_replaced}')
