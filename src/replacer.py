from pathlib import Path

source_file = Path("new_file.txt")  # file to be moved

destination = Path("destination_folder/new/location") # destination folder to move the file to

destination.mkdir(parents=True, exist_ok=True)  # Create destination folder if it doesn't exist

source_file.replace(destination / source_file.name) #function to move