with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "<!-- HIGHLIGHTED GLOBAL CLIENT VIDEO TESTIMONIALS (TOP POSITION) -->"
end_marker = "</section>"

start_idx = content.find(start_marker)
if start_idx == -1:
    print("Could not find start marker.")
    exit(1)
    
end_idx = content.find(end_marker, start_idx) + len(end_marker)

# Extract the block
video_section = content[start_idx:end_idx]

# Remove it from its original position
content_without_video = content[:start_idx] + content[end_idx:]

# Find the insertion point (after the TradingView Widget's </section>)
insert_marker = "  </section>\n\n"
insert_idx = content_without_video.find(insert_marker, content_without_video.find('<!-- TradingView Widget END -->'))

if insert_idx != -1:
    insert_idx += len(insert_marker)
    new_content = content_without_video[:insert_idx] + video_section + "\n\n" + content_without_video[insert_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: Moved Testimonials back to top.")
else:
    print("ERROR: Could not find insertion point.")
