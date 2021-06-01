## Este codigo fue desarrollado por Brayan Munoz Mora cualquier consulta
## comunicarse al correo brayanmunozmora16@gmail.com.
## Aca se anaden las funciones principales para capturar los videos, tomar snapshots
## asi como unir fuentes de videos de un folder en especifico.

import cv2 as cv
import os
import time

## Variables globales
width = 640
height = 480

## Mediante esta funcion se pretende obtener todas aquellas fuentes de video
## que se pueden abrir de los recursos de video (camaras) disponibles en el sistema.
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

## Aca podemos grabar un video desde un fuente (camID), el video se va a almacenar en la ruta
## que se especifique en videoName, y la duracion de grabacion se pasa en el parametro 
## duration (el cual esta en segundos).
def recordVideo(videoName, camID, duration, width = 640, height = 480, fps = 10.0):
	source = cv.VideoCapture(camID)

	fourcc = cv.VideoWriter_fourcc(*'XVID')
	out = cv.VideoWriter(videoName + '.avi', fourcc, fps, (width,height))
	
	if source.isOpened():
		_, frame = source.read()
	current = time.time()
	while (time.time() - current) < duration:
		out.write(frame)
		_, frame = source.read()
  
		if cv.waitKey(1) == ord('q'):
			break
	source.release()

## Esta funcion toma una imagen de la fuente especificada (camID), y se almacena en la ruta provista en el
## parametro imageName.
def takePicture (camID, imageName):
	source = cv.VideoCapture(camID)
	_,frame = source.read()
	source.release() 
	if _ and frame is not None:
		cv.imwrite(imageName, frame)
  
## Con esta funcion se genera la mezcla del video final, aca los videos estan almacenados con un un formato id_formato.avi,
## el id corresponde al orden en el que fue grabado, es por esta razon que la mezcla se realiza en base a ese orden.
## En este caso rootSources es la ruta del folder en donde se encuentran todos los videos, y dest es la ruta en donde se guardara
## el video mezclado final, en este caso unicamente se pasa el nombre de como se quiere guardar, ya que el video se guarda en la misma
## ruta que los videos separados.
def generateVideo (rootSources, dest, width = 640, height = 480, fps = 10.0):
    videoFiles = [n for n in os.listdir(rootSources) if n[-4:] == '.avi']
    index = 0
    
    source = cv.VideoCapture(rootSources + videoFiles[0])
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(rootSources + dest + '.avi', fourcc, fps, (width,height))
    
    # Empezamos el proceso para unir los videos
    while (source.isOpened()):
        ret, frame = source.read()
        if frame is None:
            index += 1
            if index >= len(videoFiles):
                break
            source = cv.VideoCapture(rootSources + videoFiles[index])
            ret, frame = source.read()
        out.write(frame)
    source.release()
    out.release()
    print("End")
    
## Codigo de ejemplo
recordVideo("BrayanMunozMora_Prof_LiceoCoronado", 0, 5)
recordVideo("BrayanMunozMora_Prof_LiceoCoronado", 2, 5)
recordVideo("BrayanMunozMora_Prof_LiceoCoronado", 4, 5)
#generateVideo("Videos\Estudiante_Prof_Institucion\Corrida2/", "videoExample")
		
