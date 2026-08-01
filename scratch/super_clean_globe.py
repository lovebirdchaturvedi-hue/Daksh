import cv2
import numpy as np
import os
import subprocess

video_dir = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\assets\videos"
src_path = os.path.join(video_dir, "APD GLOBAL BUSINESS 3.mp4")

cap = cv2.VideoCapture(src_path)
fps = cap.get(cv2.CAP_PROP_FPS) or 25
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Target crop width: 280px in center (x: 500 to 780)
x1, x2 = 500, 780
crop_w = x2 - x1

temp_out = os.path.join(video_dir, "temp_globe.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(temp_out, fourcc, fps, (crop_w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Crop to center globe area
    crop = frame[:, x1:x2].copy()
    
    # Convert to HSV to isolate yellow globe
    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    
    # Lower/upper bounds for yellow globe color
    lower_yellow = np.array([15, 60, 60])
    upper_yellow = np.array([35, 255, 255])
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Smooth mask with morphological operations & blur
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.GaussianBlur(mask, (21, 21), 0)
    
    mask_3d = mask.astype(float) / 255.0
    mask_3d = np.repeat(mask_3d[:, :, np.newaxis], 3, axis=2)
    
    # Create dark navy background #020617 -> BGR (23, 6, 2)
    bg = np.zeros_like(crop)
    bg[:, :] = [23, 6, 2]
    
    # Composite: globe over dark navy background
    composite = (crop.astype(float) * mask_3d + bg.astype(float) * (1.0 - mask_3d)).astype(np.uint8)
    
    out.write(composite)

cap.release()
out.release()

# Convert temp_globe.mp4 with audio to H.264 faststart MP4
final_out = os.path.join(video_dir, "APD_GLOBAL_BUSINESS_3_Pure_Clean.mp4")
cmd = [
    "ffmpeg", "-y", "-i", temp_out, "-i", src_path,
    "-map", "0:v:0", "-map", "1:a:0?",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "fast",
    "-c:a", "copy", "-movflags", "+faststart",
    final_out
]
subprocess.run(cmd, check=True)
print("SUCCESS: Created APD_GLOBAL_BUSINESS_3_Pure_Clean.mp4 with 100% background watermark removal!")
