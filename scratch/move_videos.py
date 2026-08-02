with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the blocks via string boundaries so it's precise.
start_marker = "<!-- HIGHLIGHTED GLOBAL CLIENT VIDEO TESTIMONIALS (TOP POSITION) -->"
end_marker = "</section>"

start_idx = content.find(start_marker)
# Find the next </section> after the start_marker
end_idx = content.find(end_marker, start_idx) + len(end_marker)

# Extract the block
video_section = content[start_idx:end_idx]

# Remove it from its original position
content_without_video = content[:start_idx] + content[end_idx:]

# Find the Google Reviews section in the new content
google_marker = "<!-- GOOGLE VERIFIED REVIEWS SECTION -->"
google_idx = content_without_video.find(google_marker)

if google_idx != -1:
    # Insert the video section just before the Google reviews
    new_content = content_without_video[:google_idx] + video_section + "\n\n  " + content_without_video[google_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: Moved Video Testimonials above Google Reviews.")
else:
    print("ERROR: Could not find Google Reviews section.")
