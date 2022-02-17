import cv2 as cv
img = cv.imread('Fotos/oaxaca.jpg')
cv.imshow('Oaxaca', img)

#convertir a escala de grises
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#Imagen con Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)

#Detectar bordes
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny edges', canny)

#Dilatar la imagen (basicamente es aumentar el grosor de los bordes)
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)

#Erosionar imagen (Basicamente es hacer los borde mas delgados)
eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow('Eroded', eroded)

#redimensionar
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

#cropping
cropped = img[50:200, 200:400]
#cv.imshow('Cropped', cropped)


cv.waitKey(0)
