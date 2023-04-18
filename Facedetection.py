import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(2)
detector = FaceDetector()
arduino = SerialObject('/dev/ttyUSB0')

while True:
    success, img = cap.read()
    img, bBoxes = detector.findFaces(img)

    if bBoxes:
        arduino.sendData([1, 0])
    else:
        arduino.sendData([0, 1])

    cv2.imshow("Video", img)
    cv2.waitKey(1)
