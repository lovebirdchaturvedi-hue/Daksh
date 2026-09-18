import re

with open('membership.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will find the grid container for Professional Pass.
# It starts with `<div style="display: grid; grid-template-columns:` and goes down for a while.
# Let's search for "Choose Your Access Level" or similar?
# Let's grep for "Professional Pass" and see the lines around it to construct the regex.
