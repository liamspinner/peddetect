import cv2 # this is openCV, short for Open Source Computer Vision
import imutils # this is a package of conveniece functions to make image processing easier (translation, rotation, resizing, etc)
import os # way of using OS dependent functionality. check python documentation for more

#Here we are initializing the hog for the pedestrian detector
#HOG stands for Histogram of Oriented Gradients
#red this article for more https://learnopencv.com/histogram-of-oriented-gradients/
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture('video1920.mp4')

while cap.isOpened():
	# read video
	ret, image = cap.read()
	if ret:
		image = imutils.resize(image,
							width=min(800, image.shape[1]))

		# detect regions with peds
		(regions, _) = hog.detectMultiScale(image,
											winStride=(4, 4),
											padding=(4, 4),
											scale=1.05)

		# draw regions in img
		for (x, y, w, h) in regions:
			cv2.rectangle(image, (x, y),
						(x+w, y+h),
						(0, 0, 255), 2)

		# display output img
		cv2.imshow("Image", image)

		####imgpath= r'C:\Users\liams\Desktop\Coding new\Ped detection\vidpic.jpg'
		#cv2.imread(image)
		#savefile = vidpic.jpg
		#cv2.imwrite(savefile, image)
                
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()
