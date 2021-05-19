import cv2 as cv
import threading as th
import sys
import time

width = 288
height = 352
def checkCameras ():
	index = 0
	arr = {}
	for i in range(10):
		cap = cv.VideoCapture(i)
		
		if cap.read()[0]:
			arr[str(i)] = True
			cap.release()
	print(arr)
	return arr
		
def camPreview(previewName, camID, ti):
	#cv.namedWindow(previewName)
	cam = cv.VideoCapture(camID)

	fourcc = cv.VideoWriter_fourcc(*'XVID')
	out = cv.VideoWriter('out_' + previewName + '.avi', fourcc, 10.0, (640,480))
	
	if cam.isOpened():
		rval, frame = cam.read()
	else:
		rval = False
	current = time.time()
	while (time.time() - current) < ti:
		#cv.imshow(previewName, frame)
		out.write(frame)
		rval, frame = cam.read()
		if cv.waitKey(1) == ord('q'):
			break
	#cv.destroyWindow(previewName)
	cam.release()

def takePreviewImage (source, name):
	cap = cv.VideoCapture(source)
	
	_,frame = cap.read()
	cap.release() #releasing camera immediately after capturing picture
	if _ and frame is not None:
		cv.imwrite(name, frame)



		
		
