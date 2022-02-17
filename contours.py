import cv2 as cv
import numpy as np

img=cv.imread('Fotos/oaxaca.jpg')
cv.imshow('Oaxaca', img)

blank=np.zeros(img.shape, dtype='uint8')
cv.imshow('BLank', blank)


#Se convierte primero la imagen en gris
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#se defenfoca la imagen para reducir los bordes en el siguiente metodo
#blur= cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#Se usa la funcion de canny para 
#canny=cv.Canny(blur,125,175)# el segundo y tercer parametro son los valores de umbral 
#cv.imshow('Canny edges', canny)

ret, thresh=cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


'''Este metodo devuelve el numero de contornos que encontro en la imagen guardada en canny
'''
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contornos encontrados!')

#para dibujar los contornos de la imagen en una imagen nueva
cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('Contours Drawn', blank )


cv.waitKey(0)