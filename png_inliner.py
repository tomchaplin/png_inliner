import io
import sys
import base64
from bs4 import BeautifulSoup

file = sys.argv[1]

with open(file, "r") as f:
    raw_html = f.read()

soup = BeautifulSoup(raw_html, "html.parser")

for imgTag in soup.find_all("img"):
    src = imgTag["src"]
    is_external = src.startswith("http")
    if is_external:
        continue

    if not src.endswith(".png"):
        continue

    with open(src, "rb") as img_file:
        img_byte_str = base64.b64encode(img_file.read()).decode("utf-8")

    new_src = "data:image/png;base64," + img_byte_str
    imgTag["src"] = new_src

print(soup)
