import json

# Read generate_pages.py
with open("generate_pages.py", "r", encoding="utf-8") as f:
    code = f.read()

# Format as notebook lines
lines = [line + "\n" for line in code.split("\n")]
if lines and lines[-1] == "\n":
    lines[-1] = ""
elif lines and lines[-1].endswith("\n"):
    lines[-1] = lines[-1][:-1]

# Load existing notebook
with open("物流HP.ipynb", "r", encoding="utf-8") as f:
    notebook_data = json.load(f)

# Find the cell we want to update (the active generator code cell, which starts with 'import os\n' and is not commented out)
found = False
for cell in notebook_data["cells"]:
    if cell.get("cell_type") == "code":
        source = cell.get("source", [])
        if len(source) > 0 and source[0].startswith("import os"):
            cell["source"] = lines
            found = True
            break

if found:
    with open("物流HP.ipynb", "w", encoding="utf-8") as f:
        json.dump(notebook_data, f, indent=1, ensure_ascii=False)
    print("Successfully synchronized generate_pages.py into 物流HP.ipynb Cell 2!")
else:
    print("Error: Could not find the active generator cell starting with 'import os' in the notebook!")
