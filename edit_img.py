import sys
import os
from PIL import Image, ImageDraw, ImageFont

image_path = r"C:\Users\DELL\.gemini\antigravity\brain\04a4cabb-5e34-4e91-9255-a6d9256e8085\media__1782898476434.png"
out_path = r"C:\Users\DELL\Downloads\apd_global_trade_dashboard.png"

try:
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Coordinates to cover "Ashish Chaturvedi"
    # Assuming standard 1080p screenshot, the text is at top left, after a hamburger menu.
    # We will cover x from 40 to 300, y from 10 to 45. (We can adjust if needed).
    # Background color is white.
    draw.rectangle([45, 10, 350, 40], fill="white")
    
    # Try to load a standard font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        try:
            font = ImageFont.truetype("segoeui.ttf", 20)
        except:
            font = ImageFont.load_default()
            
    # Draw new text
    # The text is bold and dark gray/black
    draw.text((45, 15), "APD GLOBAL TRADE", fill=(30, 30, 30), font=font)
    
    img.save(out_path)
    print("Successfully saved to", out_path)
except Exception as e:
    print("Error:", e)
