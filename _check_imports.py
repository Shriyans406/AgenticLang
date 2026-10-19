import json

with open('YTRAG/notebook/pdf_loader.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for i, c in enumerate(nb['cells']):
    if c['cell_type'] == 'code':
        src = ''.join(c['source'])
        if 'SentenceTransformer' in src:
            print(f'Cell {i} (id={c.get("id")}): HAS SentenceTransformer')
        if 'from sentence_transformers' in src:
            print(f'Cell {i}: HAS import SentenceTransformer')
        if 'from typing import' in src:
            print(f'Cell {i}: HAS typing import')
        if 'from typing import List' in src:
            print(f'Cell {i}: HAS List import')