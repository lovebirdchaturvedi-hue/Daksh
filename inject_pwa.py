import os

files_to_update = ["supplier-login.html", "supplier-dashboard.html", "supplier-rfqs.html"]

pwa_head = """<link rel="manifest" href="/manifest.json">
</head>"""

pwa_body = """
<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js').then(reg => {
        console.log('SW registered!', reg);
      }).catch(err => console.log('SW reg failed', err));
    });
  }
</script>
</body>"""

for file in files_to_update:
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "<link rel=\"manifest\"" not in content:
            content = content.replace("</head>", pwa_head)
            content = content.replace("</body>", pwa_body)
            
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
        print(f"Updated {file}")

print("All PWA tags injected successfully.")
