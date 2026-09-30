import json
nb = json.load(open('notebook/pdf_loader.ipynb', encoding='utf-8'))
c1 = ''.join(nb['cells'][0]['source'])
c2 = ''.join(nb['cells'][1]['source'])
print('has Path import:', 'from pathlib import Path' in c1)
print("file_type fixed:", "file_type']='pdf'" in c2)
print('last line of cell 2:', repr(c2.rstrip().splitlines()[-1]))
