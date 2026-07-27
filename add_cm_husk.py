import os

file_path = 'register-supplier.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target_str = '<label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="CJ Uniworld" style="width: 18px; height: 18px; accent-color: var(--gold);"> CJ Uniworld</label>'
insert_str = '\n          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="CM Husk Powder" style="width: 18px; height: 18px; accent-color: var(--gold);"> CM Husk Powder</label>'

if "CM Husk Powder" not in content:
    content = content.replace(target_str, target_str + insert_str)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added CM Husk Powder to register-supplier.html")
else:
    print("CM Husk Powder already exists in register-supplier.html")
