import os
import subprocess

videos = [
    "Testimonial Franch.mp4",
    "Testimonial Chiienese.mp4",
    "Testimonial Nigeria.mp4",
    "Gujrati Testimonial.mp4"
]

for vid in videos:
    input_path = f"assets/videos/{vid}"
    output_path = f"assets/videos/clean_{vid}"
    
    # Crop from bottom-right by keeping the top-left (x=0, y=0)
    # Crop 120px from right, 100px from bottom
    # We use crop=iw-120:ih-100:0:0
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-filter:v", "crop=iw-120:ih-100:0:0",
        "-c:a", "copy",
        output_path
    ]
    
    print(f"Cropping {vid}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Replace original with cleaned
    if os.path.exists(output_path):
        os.replace(output_path, input_path)
        print(f"Replaced {vid} with cropped version.")

print("Done cropping all 4 videos!")
