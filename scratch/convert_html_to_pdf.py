import os
import subprocess
import glob

downloads_dir = r"C:\Users\DELL\Downloads"

browser_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
]

browser_cmd = None
for bp in browser_paths:
    if os.path.exists(bp):
        browser_cmd = bp
        break

print(f"Using browser: {browser_cmd}")

html_files = glob.glob(os.path.join(downloads_dir, "*.html"))
for hf in html_files:
    if "BL_" in hf or "draft" in hf:
        pdf_path = hf[:-5] + ".pdf"
        file_url = "file:///" + os.path.abspath(hf).replace("\\", "/")
        cmd = [
            browser_cmd,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            file_url
        ]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"Success: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
        except Exception as e:
            print(f"Error converting {hf}: {e}")
