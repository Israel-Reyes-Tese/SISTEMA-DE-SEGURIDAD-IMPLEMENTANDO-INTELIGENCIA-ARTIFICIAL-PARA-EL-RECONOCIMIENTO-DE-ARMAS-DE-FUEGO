from django.shortcuts import render
from django.http import StreamingHttpResponse
from ultralytics import YOLO

import cv2
from PIL import Image as im

from .models import *
from datetime import datetime

import numpy as np
from io import BytesIO
from PIL import Image
#
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile

# Create your views here.
def detect_objects(request):
    return render(request,'index.html')

def tiene_datos(tensor):
    return tensor.nelement() > 0

def transformar_array_en_imagen(array):
    imagen = Image.fromarray(array, 'RGB')
    imagen_bytes = BytesIO()
    imagen.save(imagen_bytes, format='JPEG')
    imagen_bytes = imagen_bytes.getvalue()
    return imagen_bytes

def stream():
        # Leer nuestro modelo
     # objeto_deteccion_app/model_s/runs/detect/train/weights/best.pt
    # objeto_deteccion_app/modelos/best.pt
    model = YOLO("objeto_deteccion_app/model_s/runs/detect/train3/weights/best.pt")
    model.fuse()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to capture image")
            break
        # Leemos resultados
        resultados = model.predict(frame, imgsz = 640, conf = 0.7)

        # Mostramos resultados
        anotaciones = resultados[0].plot()


        print("Armas de fuego boxes ", resultados[0].boxes.cls)
        print("Armas de fuego boxes ", type(resultados[0].boxes.cls))
        print("Armas de fuego datos ", tiene_datos(resultados[0].boxes.cls))

        # Verifica si se detecta un arma de fuego
        # Guardar el registro en la base de datos
        # Estructura de datos para almacenar información sobre las detecciones
        informacion_detecciones = []
        fecha_actual = datetime.now()
        timestamp = str(fecha_actual).replace(":","_")
        #print("Datos importantes", resultados[0].__dict__)  # Imprime los atributos del objeto
        #print("Frame", frame)  # Imprime los atributos del objeto
        if tiene_datos(resultados[0].boxes.cls):
            print("Tiene datos a guardar")
            bounding_box = resultados[0].boxes.data[0]
            boxes = resultados[0].boxes.cpu().numpy()

            print("bounding_box", bounding_box)
            print("bounding_box 1", bounding_box[0], bounding_box[3])
            nombre = f"files/images/armas_fuego/Arma de fuego{timestamp}.jpg"
            path_modificado = f"/images/armas_fuego/Arma de fuego{timestamp}.jpg"
            cv2.imwrite(nombre, frame)
            print(f"Captura de pantalla tomada: {nombre}")
            print(f"Se modifca el path de pantalla tomada: {nombre}")
            proba_conf = boxes.conf[0]
            clase_obj = boxes.cls[0]
            DetectedObject.objects.create(etiqueta=f"Arma de fuego {fecha_actual}",probabilidad=proba_conf,clase=clase_obj, imagen=path_modificado, x=bounding_box[0], y=bounding_box[1], w = bounding_box[2], h = bounding_box[3])
            # Valores extras
            print("resultados xyxy ",boxes.xyxy)
            print("resultados conf",boxes.conf)
            print("resultados clase",boxes.cls)

        else:
            print("No hay datos a guardar")
                


        image_bytes = cv2.imencode('.jpg', anotaciones)[1].tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')
          
        # Cerrar nuestro programa
        if cv2.waitKey(1) == 27:
            break 
    
    cap.release()
    cv2.destroyAllWindows()    

def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')    

