import os
import re
import codecs

tawk_script = """
<!--Start of Tawk.to Script-->
<script type="text/javascript">
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/6abfcc62beb8e034c00dd833/1k3ujcoou';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();
</script>
<!--End of Tawk.to Script-->
"""

directory = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo"

tidio_style_regex = r'<style>\s*/\*\s*Force Tidio.*?</style>'
tidio_script_auto = r'<script id="tidio-auto-open">.*?</script>'
tidio_script_src = r'<script src="//code\.tidio\.co/.*?" async></script>'

files_updated = 0

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        try:
            with codecs.open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Wipe Tidio
            content = re.sub(tidio_style_regex, '', content, flags=re.IGNORECASE | re.DOTALL)
            content = re.sub(tidio_script_auto, '', content, flags=re.IGNORECASE | re.DOTALL)
            content = re.sub(tidio_script_src, '', content, flags=re.IGNORECASE | re.DOTALL)
            
            # Inject Tawk.to before </body> if not present
            if "embed.tawk.to" not in content and "</body>" in content:
                content = content.replace("</body>", tawk_script + "\n</body>")
            
            if content != original_content:
                with codecs.open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {filename}")
                files_updated += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"Successfully replaced chat widget in {files_updated} HTML files.")
