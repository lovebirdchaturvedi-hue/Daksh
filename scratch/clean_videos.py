import os
import subprocess

video_dir = r"C:\Users\DELL\Downloads\Daksh\Testimonials"
out_dir = os.path.join(video_dir, "Cleaned_Videos")
os.makedirs(out_dir, exist_ok=True)

tasks = [
    ("APD GLOBAL BUSINESS 2.mp4", "crop=in_w:in_h-60:0:0", "APD_GLOBAL_BUSINESS_2_Clean.mp4"),
    ("APD GLOBAL BUSINESS 3.mp4", "crop=in_w:in_h-70:0:0", "APD_GLOBAL_BUSINESS_3_Clean.mp4"),
    ("APD GLOBAL BUSINESS 4.mp4", "crop=in_w:in_h-60:0:0", "APD_GLOBAL_BUSINESS_4_Clean.mp4"),
    ("Membership Best 2.mp4", "crop=in_w:in_h-70:0:0", "Membership_Best_2_Clean.mp4"),
]

for src_name, vf, dst_name in tasks:
    src = os.path.join(video_dir, src_name)
    dst = os.path.join(out_dir, dst_name)
    cmd = ["ffmpeg", "-y", "-i", src, "-vf", vf, "-c:a", "copy", dst]
    print(f"Cleaning {src_name} -> {dst_name}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"SUCCESS: {dst_name} ({os.path.getsize(dst)} bytes)")
    else:
        print(f"ERROR: {res.stderr}")
