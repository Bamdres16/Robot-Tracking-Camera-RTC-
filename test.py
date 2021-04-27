import cv2 as cv
import threading as th
import sys

class camThread (th.Thread):
	def __init__(self, previewName, camID):
		th.Thread.__init__(self)
		self.previewName = previewName
		self.camID = camID
	def run(self):
		print("Starting " + self.previewName)
		camPreview(self.previewName, self.camID)
		
def camPreview(previewName, camID):
	cv.namedWindow(previewName)
	cam = cv.VideoCapture(camID)
	fourcc = cv.VideoWriter_fourcc(*'XVID')
	out = cv.VideoWriter('out_' + previewName + '.avi', fourcc, 10.0, (640,480))
	
	if cam.isOpened():
		rval, frame = cam.read()
	else:
		rval = False
	
	while rval:
		#cv.imshow(previewName, frame)
		out.write(frame)
		rval, frame = cam.read()
		if cv.waitKey(1) == ord('q'):
			break
	cv.destroyWindow(previewName)
	cam.release()

camID = int(sys.argv[1])
thread1 = camThread('Source'+str(camID), camID)

thread1.start()


		
		
