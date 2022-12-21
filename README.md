# tableau-shape-extract

Under the hood tableau workbooks are XML so `beautifulsoup4` can 
be used to extract shapes. [Inspiration](https://www.clearlyandsimply.com/clearly_and_simply/2014/05/extract-custom-shapes-from-a-tableau-workbook.html)

## Setup

```shell
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```python
# extract.py
from extract import main

main('path/to/workbook.twb')
```
