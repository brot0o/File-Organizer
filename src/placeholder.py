# folder placeholder 
from pathlib import Path

new_dataset = Path("destination_folder/data/new.csv")

print(new_dataset.exists()) # Check if the new dataset exists

new_dataset.parent.mkdir(parents=True, exist_ok=True)  # Ensure parent directory exists
new_dataset.touch()  # Create the new dataset if it doesn't exist (or update its timestamp if it does)
new_dataset.touch() # Create the new dataset if it doesn't exist

print(new_dataset.exists()) # Check if the new dataset exists

# The touch method is originally meant for updating a file's modification time, so it can be used on existing files as well.