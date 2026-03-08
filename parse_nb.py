import json
with open('eda.ipynb') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        print(f"\n--- Cell {i} ---")
        print(''.join(cell.get('source', [])))
        print("Outputs:")
        for out in cell.get('outputs', []):
            if 'text/plain' in out.get('data', {}):
                print(''.join(out['data']['text/plain']))
            if out.get('name') == 'stdout':
                print(''.join(out.get('text', [])))
