import cv2 as cv
from cv2 import imread
from cv2 import imshow

img=imread('Fotos/oaxaca.jpg')
cv.imshow('Oaxaca', img)

#averaging
average=cv.blur(img,(3,3))
cv.imshow('Average', average)

#Gaussian blur
gauss=cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gauss)

#Median blur 
median= cv.medianBlur(img,3)
cv.imshow('Median blur', median)

#bilateral
bilateral=cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)