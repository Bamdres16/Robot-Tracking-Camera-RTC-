# Este archivo permite obtener los atributos de camaras de un archivo json
# dado en la interfaz.

import json

# Con esta funcion obtenemos los atributos del identificador de camara y la duracion de grabacion.
def getAtributes (filePath):
    with open(filePath) as json_file:
        data = json.load(json_file)
        return data
    