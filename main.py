import os
import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

folder_path = "images"

image_extensions = [".jpg", ".jpeg", ".png", ".webp"]

# モデル準備
base_options = python.BaseOptions(model_asset_path="blaze_face_short_range.tflite")
options = vision.FaceDetectorOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE
    )

detector = vision.FaceDetector.create_from_options(options)

for file in os.listdir(folder_path):
    if any(file.lower().endswith(ext) for ext in image_extensions):

        path = os.path.join(folder_path, file)
        img = cv2.imread(path)

        if img is None:
            print("読み込み失敗:", file)
            continue

        # OpenCV → MediaPipe形式に変換
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)

        detection_result = detector.detect(mp_image)

        if detection_result.detections:
            print("顔あり:", file)
        else:
            print("顔なし:", file)