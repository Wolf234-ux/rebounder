import os
import base64

base_dir = r"c:\Users\saura\OneDrive\Desktop\rebounder"

# Read style.css
with open(os.path.join(base_dir, "style.css"), "r", encoding="utf-8") as f:
    css_content = f.read()

# Read app.js
with open(os.path.join(base_dir, "app.js"), "r", encoding="utf-8") as f:
    js_content = f.read()

# Encode images to base64
def get_base64_img(rel_path):
    full_path = os.path.join(base_dir, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode("utf-8")
            return f"data:image/jpeg;base64,{encoded}"
    return rel_path

hero_b64 = get_base64_img(os.path.join("assets", "hero_rebounder.jpg"))
dr_b64 = get_base64_img(os.path.join("assets", "dr_gaikwad.jpg"))
senior_b64 = get_base64_img(os.path.join("assets", "senior_routine.jpg"))

# Read index.html template
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Replace style.css link with inline <style>
html = html.replace(
    '<link rel="stylesheet" href="style.css">',
    f'<style>\n{css_content}\n</style>'
)

# Replace app.js script with inline <script>
html = html.replace(
    '<script src="app.js"></script>',
    f'<script>\n{js_content}\n</script>'
)

# Replace image paths with embedded base64 data URIs
html = html.replace('src="assets/hero_rebounder.jpg"', f'src="{hero_b64}"')
html = html.replace('src="assets/dr_gaikwad.jpg"', f'src="{dr_b64}"')
html = html.replace('src="assets/senior_routine.jpg"', f'src="{senior_b64}"')

# Write out self-contained standalone index.html
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully bundled everything into single self-contained index.html!")
