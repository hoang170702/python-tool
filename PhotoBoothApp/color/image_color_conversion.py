import cv2
from PIL import Image


def to_pil_image(frame):

    # OpenCV → RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # RGB → PIL Image
    pil_img = Image.fromarray(frame_rgb)
    return pil_img
