import json

p = 'YTRAG/agenticrag/1-agenticrag.ipynb'
nb = json.load(open(p, encoding='utf-8'))
errors = []
for i, c in enumerate(nb['cells']):
    if c['cell_type'] != 'code':
        continue
    src = ''.join(c['source'])
    if not src.strip():
        continue
    try:
        compile(src, f'<agenticrag cell {i}>', 'exec')
    except Exception as e:
        errors.append((i, str(e)))
        print(f'cell {i}: ERROR {e}')
print('ERRORS:', len(errors))
