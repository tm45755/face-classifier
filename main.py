import os

folder_path = "images"

image_extensions = [".jpg", ".jpeg", ".png", ".webp"]

files = os.listdir(folder_path)

for file in files:
    if any(file.lower().endswith(ext) for ext in image_extensions):
        print(file)