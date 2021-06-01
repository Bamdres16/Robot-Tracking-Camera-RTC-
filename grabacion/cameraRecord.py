# Este codigo fue desarrollado por Brayan Munoz Mora cualquier consulta
# comunicarse al correo brayanmunozmora16@gmail.com.
# Aca se anaden las funciones principales para capturar los videos, tomar snapshots
# asi como unir fuentes de videos de un folder en especifico.

import cv2 as cv
import os
import time
from datetime import datetime

# Variables globales
rootPathVideos = "Videos/"

# Mediante esta funcion se pretende obtener todas aquellas fuentes de video
# que se pueden abrir de los recursos de video (camaras) disponibles en el sistema.


def checkCameras():
	index = 0
	arr = {}
	for i in range(10):
	    cap = cv.VideoCapture(i)

	    if cap.read()[0]:
		    arr[str(i)] = True
		    cap.release()
	print(arr)
	return arr

# Aca podemos grabar un video desde un fuente (camID), el video se va a almacenar en la ruta
# que se especifique en videoName, y la duracion de grabacion se pasa en el parametro
# duration (el cual esta en segundos).


def recordVideo(videoName, camID, duration, width=640, height=480, fps=10.0):
    now = datetime.now()
    today = str(now.strftime("%d-%m-%Y"))
    filePath = rootPathVideos + videoName + "/" + today
    source = cv.VideoCapture(camID)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    
    videoIndex = len([n for n in os.listdir(filePath) if n[0] != 'f'])
    out = cv.VideoWriter(filePath + "/" + str(videoIndex) + "_" + today + '.avi', fourcc, fps, (width, height))
    if source.isOpened():
        _, frame = source.read()
    current = time.time()
    while (time.time() - current) < duration:
        out.write(frame)
        _, frame = source.read()
        if cv.waitKey(1) == ord('q'):
            break
    source.release()
    print("Video created in", filePath)

# Esta funcion toma una imagen de la fuente especificada (camID), y se almacena en la ruta provista en el
# parametro imageName.
def takePicture (camID, imageName):
	source = cv.VideoCapture(camID)
	_,frame = source.read()
	source.release() 
	if _ and frame is not None:
		cv.imwrite(imageName, frame)
  
# Con esta funcion se genera la mezcla del video final, aca los videos estan almacenados con un un formato id_formato.avi,
# el id corresponde al orden en el que fue grabado, es por esta razon que la mezcla se realiza en base a ese orden.
# En este caso rootSources es la ruta del folder en donde se encuentran todos los videos, y dest es la ruta en donde se guardara
# el video mezclado final, en este caso unicamente se pasa el nombre de como se quiere guardar, ya que el video se guarda en la misma
# ruta que los videos separados.
def generateVideo (rootSources, width = 640, height = 480, fps = 10.0):
    now = datetime.now()
    today = str(now.strftime("%d-%m-%Y"))
    filePath = rootPathVideos + rootSources
    videoFiles = [n for n in os.listdir(filePath) if (n[-4:] == '.avi') and (n[0] != "f")]
    print(videoFiles)
   
    index = 0
    
    source = cv.VideoCapture(filePath + "/" + videoFiles[0])
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(filePath + "/" + "f_" + today + '.avi', fourcc, fps, (width,height))
    
    # Empezamos el proceso para unir los videos
    while (source.isOpened()):
        ret, frame = source.read()
        if frame is None:
            index += 1
            if index >= len(videoFiles):
                break
            source = cv.VideoCapture(filePath + "/" + videoFiles[index])
            ret, frame = source.read()
        out.write(frame)
    source.release()
    out.release()
    print("End")
    
# Codigo de ejemplo
''' recordVideo("BrayanMunozMora_Prof_LiceoCoronado", 0, 1)
recordVideo("BrayanMunozMora_Prof_LiceoCoronado", 0, 1)
recordVideo("BrayanMunozMora_Prof_LiceoCoronado", 0, 1)
recordVideo("BrayanMunozMora_Prof_LiceoCoronado", 0, 1)
generateVideo("BrayanMunozMora_Prof_LiceoCoronado/01-06-2021") '''
		
