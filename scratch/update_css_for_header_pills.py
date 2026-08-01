import os

css_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\assets\css\premium.css"

responsive_css = """

/* TOP HEADER 3D PILL BUTTONS RESPONSIVE STYLING */
.top-pill-actions-container {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-left: 15px;
    margin-right: 15px;
    flex-wrap: nowrap;
}

@media (max-width: 1200px) {
    .top-pill-actions-container {
        overflow-x: auto;
        padding-bottom: 4px;
        max-width: 100%;
        -webkit-overflow-scrolling: touch;
    }
    .top-pill-actions-container::-webkit-scrollbar {
        display: none;
    }
}
"""

if os.path.exists(css_path):
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(responsive_css)
    print("Appended responsive header pill styles to premium.css!")
