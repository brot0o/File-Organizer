from PIL import Image, ImageFilter

# Always use a 'with' block to ensure the file handle closes properly
with Image.open(r"C:\Users\André\Downloads\python\fileorganizer\File-Organizer\destination_folder\data\passage.jpg") as img:
    print(f"Format: {img.format} | Size: {img.size} | Mode: {img.mode}")

    img.thumbnail((800, 800))

    blurred = img.filter(ImageFilter.GaussianBlur(radius=2))

    # Save as a new PNG file
    blurred.save("passage_edited.png")