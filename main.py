import os

folder_path = "images"  # ←ここにフォルダ名

files = os.listdir(folder_path)

for file in files:
    print(file)