from bs4 import BeautifulSoup
import base64
import os
import pathlib


def main(workbook_path: str):
    """

    :param workbook_path: string
        /path/to/workbook.twb
    :return: None
    """
    fp = pathlib.Path(workbook_path)
    assert fp.suffix == '.twb', f"workbook must be *.twb file, you passed {fp.suffix}"
    with open(fp, 'r') as f:
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


if __name__ == '__main__':
    main('path/to/workbook.twb')
