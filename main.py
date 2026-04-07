import os
import cv2
import numpy as np

folder_path = "images"

image_extensions = [".jpg", ".jpeg", ".png", ".webp"]

for file in os.listdir(folder_path):
    if any(file.lower().endswith(ext) for ext in image_extensions):

        path = os.path.join(folder_path, file)
        
        with open(path, "rb") as f:
            data = np.frombuffer(f.read(), dtype=np.uint8)

        img = cv2.imdecode(data, cv2.IMREAD_COLOR)

        if img is None:
            print("読み込み失敗:", file)
        else:
            print("OK:", file, img.shape)