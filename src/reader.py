from pathlib import Path

file = Path(r"C:\Users\André\Downloads\python\fileorganizer\File-Organizer\very_new_object.txt")

print(f'1-{file.read_text()}')  # Read the content of the file and print it

nonexistent_file = Path("gibberish.txt")

try:
   contents = nonexistent_file.read_text()
except FileNotFoundError:
   print(f"2-No such thing.")