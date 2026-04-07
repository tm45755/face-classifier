import os
import cv2

folder_path = "images"

image_extensions = [".jpg", ".jpeg", ".png", ".webp"]

for file in os.listdir(folder_path):
    if any(file.lower().endswith(ext) for ext in image_extensions):

        path = os.path.join(folder_path, file)
        img = cv2.imread(path)

        if img is None:
            print("読み込み失敗:", file)
        else:
            print("OK:", file, img.shape)