import os

file_path = 'supplier-dashboard.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The corrupted block is from line index 130 to 324 (inclusive)
new_lines = lines[:130] + lines[325:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Removed 195 corrupted lines. New line count: {len(new_lines)}")
