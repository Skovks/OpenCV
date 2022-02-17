'''Para cambiar entre espacios de colores
Opencv trabaja con el espacio de colores BGR, asi que si deseas desplegar esa imagen en RGB, los colores estaran invertidos'''
import cv2 as cv
import matplotlib.pyplot as plt

img= cv.imread('Fotos/oaxaca.jpg')
cv.imshow('Oaxaca', img)

#plt.imshow(img)
#plt.show()


#Cambiar a escala de grises
#BGR to Grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

#cambiar a saturacion de colores
#BGR to HSV
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('HSV',hsv)

#cambiar a version deslavada
#BGR to l*a*b
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('LAB', lab)

#BGR to RGB
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)

#plt.imshow(rgb)
#plt.show()

#HSV TO BGR
hsv_bgr=cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV ---> BGR', hsv_bgr)


cv.waitKey(0)