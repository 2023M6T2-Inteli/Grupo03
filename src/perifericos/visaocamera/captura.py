import cv2
import numpy as np

#Abre a captura de video da camera
video_capture = cv2.VideoCapture(0)

#Enquanto a captura de video estiver aberta
while video_capture.isOpened():
     #Le a captura de video e guarda a imagem na variável frame
     ret, frame = video_capture.read()

#Mostra a imagem que está sendo guardada na variavel frame em tempo #real
cv2.imshow("image", frame)
cv2.waitKey(0)


#ESCALA DE CINZA
import cv2
import numpy as np
image = cv2.imread("todo/o/caminho/do/diretorio/da/imagem.jpg")
gray = cv2.cvtcolor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Nome que voce quiser dar para a janela", image)
cv2.waitKey(0)