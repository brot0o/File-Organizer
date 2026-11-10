from pathlib import Path

file = Path("very_new_object.txt")

file.write_text("very new sample text")  # Write text to the file, overwriting any existing content

print(f'1-{file.read_text()}')  # Read the content of the file and return it

# the problem here is that the method write_text() overwrites the existing content of the file. 
# if you want to append text to the file instead of overwriting it, you can use the open() function with the 'a' mode (append mode). 
# here's how you can do it:

open("very_new_object.txt", "a").write("\nadditional sample text")  # Append text to the file
print(f'2-{file.read_text()}')  # Read the content of the file and return it


# or we can use read_text() and write_text() methods to read and write text to files...

old_text = file.read_text() + "\n"
final_text = old_text + "third additional sample text"

file.write_text(old_text + final_text)  # Write the combined text back to the file

print(f'3-{file.read_text()}')  # Read the content of the file and return it