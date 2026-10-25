import json

p = 'YTRAG/agenticrag/1-agenticrag.ipynb'
nb = json.load(open(p, encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    print(f'===== CELL {i} ({c["cell_type"]}) =====')
    print(''.join(c['source']))
    if c.get('outputs'):
        for o in c['outputs']:
            if 'text' in o: print('OUTPUT TEXT:', ''.join(o['text']))
            if 'ename' in o: print('OUTPUT ERROR:', o.get('ename'), o.get('evalue'))
            if 'data' in o and 'text/plain' in o['data']: print('OUTPUT DATA:', ''.join(o['data']['text/plain']))
