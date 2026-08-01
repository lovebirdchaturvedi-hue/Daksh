import os
import glob
import subprocess

video_dir = r"C:\Users\DELL\Downloads\Daksh\Testimonials"
cleaned_dir = os.path.join(video_dir, "Cleaned_Videos")
os.makedirs(cleaned_dir, exist_ok=True)

files = glob.glob(os.path.join(video_dir, "*.mp4"))

for src in files:
    fname = os.path.basename(src)
    # Skip already clean videos from previous runs if in source
    if fname.startswith("CLEAN_"):
        continue
        
    dst = os.path.join(cleaned_dir, "CLEAN_" + fname.replace(" ", "_"))
    # Crop bottom 6% off height for watermark removal + faststart for seamless mobile web streaming
    cmd = [
        "ffmpeg", "-y", "-i", src,
        "-vf", "crop=in_w:in_h*0.94:0:0",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "22",
        "-preset", "fast",
        "-movflags", "+faststart",
        dst
    ]
    print(f"Cleaning {fname}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"SUCCESS: CLEAN_{fname} ({os.path.getsize(dst)} bytes)")
    else:
        print(f"ERROR on {fname}: {res.stderr[:300]}")

print("All testimonial and platform videos cleaned and mobile-optimized!")
