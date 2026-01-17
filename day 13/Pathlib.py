from pathlib import Path
folder=Path("MyData")
file=folder/"my_path.txt"
if(file):
    print("File is ok...")
else:
    print("Nothing found...")