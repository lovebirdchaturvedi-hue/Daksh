import cv2
import numpy as np
import os
import subprocess

video_dir = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\assets\videos"
src_path = os.path.join(video_dir, "APD GLOBAL BUSINESS 2.mp4")

cap = cv2.VideoCapture(src_path)
fps = cap.get(cv2.CAP_PROP_FPS) or 25
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

temp_out = os.path.join(video_dir, "temp_apd2.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(temp_out, fourcc, fps, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to YUV / Gray / HSV to separate background noise/watermark from bright graphics
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Threshold: dark background pixels (< 45 brightness) will be replaced with pure #020617 navy
    # Bright text/graphics (> 45 brightness) will be preserved 100%
    bg_mask = (gray < 40).astype(float)
    bg_mask = cv2.GaussianBlur(bg_mask, (9, 9), 0)
    bg_mask_3d = np.repeat(bg_mask[:, :, np.newaxis], 3, axis=2)
    
    # Create pure dark navy background BGR (23, 6, 2)
    pure_bg = np.zeros_like(frame)
    pure_bg[:, :] = [23, 6, 2]
    
    composite = (frame.astype(float) * (1.0 - bg_mask_3d) + pure_bg.astype(float) * bg_mask_3d).astype(np.uint8)
    
    out.write(composite)

cap.release()
out.release()

final_out = os.path.join(video_dir, "APD_GLOBAL_BUSINESS_2_Pure_Clean.mp4")
cmd = [
    "ffmpeg", "-y", "-i", temp_out, "-i", src_path,
    "-map", "0:v:0", "-map", "1:a:0?",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "fast",
    "-c:a", "copy", "-movflags", "+faststart",
    final_out
]
subprocess.run(cmd, check=True)
print("SUCCESS: Created APD_GLOBAL_BUSINESS_2_Pure_Clean.mp4 with pure navy background!")
