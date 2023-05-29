from ultralytics import YOLO
import cv2 as cv

model = YOLO('./datasets/best.pt')

capture = cv.VideoCapture(0)

while True:
   _, frame = capture.read()
   result = model.predict(frame, conf=0.6)
   cv.imshow('frame', result[0].plot())
   if cv.waitKey(1) == ord('q'):
      break

cap.release()
cv.destroyAllWindows()