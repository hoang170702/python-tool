import cv2

def open_camera() :
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Can't open camera")
        exit(1)

    print("Open camera successfully, press q to exit")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't read frame")
            break
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
