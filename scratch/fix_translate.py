import os
import codecs

directory = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo"

broken_script = """<script type="text/javascript">
  , 'google_translate_element');
  }
  </script>"""

fixed_script = """<script type="text/javascript">
  function googleTranslateElementInit() {
    new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
  }
  </script>"""

# Also it could be formatted differently, so let's use regex
import re
broken_pattern = r'<script type="text/javascript">\s*, \'google_translate_element\'\);\s*}\s*</script>'

files_fixed = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with codecs.open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = re.sub(broken_pattern, fixed_script, content)
        
        if new_content != content:
            with codecs.open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_fixed += 1
            print(f"Fixed translate script in {filename}")

print(f"Fixed {files_fixed} files.")
