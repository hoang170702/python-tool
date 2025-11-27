import os.path
import time
from datetime import datetime

import cv2

from PhotoBoothApp.color.image_color_conversion import to_pil_image


def open_camera() :
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Can't open camera")
        exit(1)

    print("Press 'SPACE' to capture an image, 'ESC' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't read frame")
            break
        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)
        if key == 27 :
            break
        if key == 32 :
            file_path = generate_image_path()
            capture_save_image(file_path, frame)
            print("Saved:", file_path)

            # ===== TEST CHUYỂN MÀU PIL =====
            pil_img = to_pil_image(frame)
            test_path = file_path.replace(".jpg", "_pil.jpg")
            pil_img.save(test_path)
            print("Saved PIL test:", test_path)
            # ===============================


def generate_image_path():
    base_dir = os.path.dirname(os.path.abspath( __file__))

    date_forder = datetime.now().strftime("%Y-%m-%d")

    static_captures = os.path.abspath(
        os.path.join(base_dir, "..", "static", "captures", date_forder)
    )

    os.makedirs(static_captures, exist_ok=True)

    file_name = f"capture_{int(time.time())}.jpg"

    return os.path.join(static_captures, file_name)



def capture_save_image(image_path, frame):
    cv2.imwrite(image_path, frame)
