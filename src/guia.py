from pathlib import Path

base_path = Path("/home/user")
data_dir = Path("data")
cwd = Path.cwd()
imagefile = Path("imagem2.jpg")
# Combining multiple paths
file_path = base_path / data_dir / "readables.txt"  



print(file_path)
print(cwd)
print(f'Here is the complete image file: {imagefile.name}')
print(f'that calls {imagefile.stem}') # can be usefull to convert files to different formats
print(f'that is a {imagefile.suffix}')
print(f'{file_path.parts}') # split its components
print(f'{list(file_path.parents)}') # list its parent directories

for entry in cwd.iterdir():
   if entry.is_dir():
      print(entry.name, "is a directory")

for entry in cwd.iterdir():
   if entry.is_file():
      print(entry.suffix)

print(f'{imagefile.exists()}') # .exist check if a path exists, returns True or False
print(f'{cwd.exists()}') # .exist check if a path exists, returns True or False