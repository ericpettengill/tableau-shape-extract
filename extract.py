from bs4 import BeautifulSoup
import base64
import os

with open(r"path/to/workbook.twb", 'r') as f:
    y = BeautifulSoup(f)

out = {}
for shapes in y.find_all("shapes"):
    for img in shapes.find_all('shape'):
        out.update({
            img.attrs['name']: img.text
        })

for name, content in out.items():
    folder, file = name.split('/')
    print(f"{file}: {os.path.isfile(name)}")

    if not os.path.isdir(folder):
        print(f"making directory {folder}")
        os.mkdir(f"{folder}")

    print(f"writing to file: {name}")
    with open(f"{name.split('.')[0]}.png", 'wb') as f:
        f.write(base64.b64decode(content))
