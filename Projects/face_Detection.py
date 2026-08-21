#############   WELCOME TO YOLO FACE DETECTION   #############
import cv2
import urllib.request
from pathlib import Path
from ultralytics import YOLO


MODEL_PATH = Path("face_model.pt")

MODEL_URL = (
    "https://github.com/lindevs/yolov8-face/"
    "releases/latest/download/yolov8n-face-lindevs.pt"
)

if not MODEL_PATH.exists():
    print("Downloading face detection model...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print("Model downloaded successfully!")


model = YOLO(str(MODEL_PATH))


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam!")
    exit()



while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(
        frame,
        conf=0.5,
        verbose=False
    )

    for box in results[0].boxes:

        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )

        confidence = float(box.conf[0])

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        text = f"Face {confidence:.2f}"

        cv2.putText(
            frame,
            text,
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )



    cv2.imshow(
        "YOLO Face Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()

print("===========================================================")
print("Face detection stopped. Goodbye!")