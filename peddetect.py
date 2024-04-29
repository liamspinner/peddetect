import cv2
import imutils


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture('rtsp://162.191.11.144:8000')


while cap.isOpened():
    ret, image=cap.read()
    if ret:
        image = imutils.resize(image,
                               width=min(1000, image.shape[0]))
        (regions, _) = hog.detectMultiScale(image,
                                            winStride=(4, 4),
                                            padding=(10, 10),
                                            scale=1.05)
        for (x, y, w, h) in regions:
                cv2.rectangle(image, (x, y),
                              (x + w, y + h),
                              (0, 0, 255), 2)
        cv2.imshow("Image", image)
        if cv2.waitkey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()

cv2.destroyAllWindows()
