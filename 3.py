import cv2
import imutils
import numpy


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


image=cv2.imread("img.png")


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
cv2.waitkey(0)
#if cv2.waitkey(25) & 0xFF == ord('q'):
    #break
#cap.release()

cv2.destroyAllWindows()
