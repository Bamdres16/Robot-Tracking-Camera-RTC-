import cv2 as cv
import threading as th
import sys
import time

width = 288
height = 352
def checkCameras ():
	index = 0
	arr = []
	for i in range(10):
		cap = cv.VideoCapture(i)
		
		if cap.read()[0]:
			arr.append(i)
			cap.release()
	print(arr)
	return arr

class camThread (th.Thread):
	def __init__(self, previewName, camID):
		th.Thread.__init__(self)
		self.previewName = previewName
		self.camID = camID
	def run(self):
		print("Starting " + self.previewName)
		camPreview(self.previewName, self.camID)
		
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

camID = int(sys.argv[1])

camerasAvailable = [camID]

for camID in camerasAvailable:
	camPreview('Source0', 0, 4)
	camPreview('Source2', 2, 5)
	camPreview('Source1', 0, 4)



		
		
