import json
import nbformat
from nbclient import NotebookClient

NB = 'notebook/pdf_loader.ipynb'

cell1 = """import os
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path"""

cell2 = '''def process_all_pdfs(pdf_directory):
    all_documents=[]
    pdf_dir=Path(pdf_directory)

    pdf_files=list(pdf_dir.glob("**/*.pdf"))

    print(f"Found {len(pdf_files)} PDF files to process")

    for pdf_file in pdf_files:
        print(f"\\nProcessing: {pdf_file.name}")
        try:
            loader=PyPDFLoader(str(pdf_file))
            documents=loader.load()

            for doc in documents:
                doc.metadata['source_file']=pdf_file.name
                doc.metadata['file_type']='pdf'

            all_documents.extend(documents)
            print(f"Loaded {len(all_documents)} pages")

        except Exception as e:
            print(f"Error: {e}")

    print(f"\\nTotal documents loaded: {len(all_documents)}")
    return all_documents

data_dir = Path("../data")
if not data_dir.exists():
    data_dir = Path("data")

all_pdf_documents= process_all_pdfs(str(data_dir))'''

cell3 = "all_pdf_documents"

# --- fix the notebook file ---
nb = nbformat.read(NB, as_version=4)
while len(nb.cells) < 3:
    nb.cells.append(nbformat.v4.new_code_cell(''))

nb.cells[0].source = cell1
nb.cells[1].source = cell2
nb.cells[2].source = cell3
for c in nb.cells:
    if c.cell_type == 'code':
        c.outputs = []
        c.execution_count = None

nbformat.write(nb, NB)
print('FIXED FILE ON DISK\n')

# --- execute with a real ipykernel, cwd = notebook/ ---
nb = nbformat.read(NB, as_version=4)
client = NotebookClient(
    nb,
    timeout=180,
    kernel_name='python3',
    resources={'metadata': {'path': 'notebook'}},
)
client.execute()

# --- print every cell output to console ---
for i, c in enumerate(nb.cells):
    if c.cell_type != 'code':
        continue
    print(f'===== CELL {i} SOURCE =====')
    print(c.source)
    print(f'----- CELL {i} OUTPUT -----')
    for out in c.outputs:
        if out.output_type == 'stream':
            print(out.text, end='')
        elif out.output_type == 'execute_result':
            print(out['data'].get('text/plain', ''))
        elif out.output_type == 'error':
            print('ERROR:', out.ename, out.evalue)
            print('\n'.join(out.traceback))
    print()

# --- save executed outputs INTO the notebook file ---
nbformat.write(nb, NB)
print('EXECUTED OUTPUTS SAVED INTO notebook/pdf_loader.ipynb')
