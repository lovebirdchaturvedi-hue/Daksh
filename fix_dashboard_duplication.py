import os

file_path = 'supplier-dashboard.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find first occurrence of <script type="module">
first_script_idx = -1
for i, line in enumerate(lines):
    if '<script type="module">' in line:
        first_script_idx = i
        break

# Find second occurrence of <script type="module">
second_script_idx = -1
for i in range(first_script_idx + 1, len(lines)):
    if '<script type="module">' in line:
        second_script_idx = i
        break

if first_script_idx != -1 and second_script_idx != -1:
    print(f"Found first script at {first_script_idx} and second at {second_script_idx}")
    
    # We want to keep everything up to first_script_idx (exclusive),
    # and then everything from second_script_idx (inclusive) to the end.
    new_lines = lines[:first_script_idx] + lines[second_script_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully repaired supplier-dashboard.html by removing the corrupted duplicate block.")
else:
    print("Could not find two script tags. File might already be fixed or structure is different.")
