import cv2 as cv


img=cv.imread('Fotos/oaxaca.jpg')
cv.imshow('Oaxaca', img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding
threshold,thresh=cv.threshold(gray,150, 255, cv.THRESH_BINARY)
cv.imshow('Simplem Thresholded',thresh)

#Simple Inverse Thresholding
threshold,thresh_inv=cv.threshold(gray,150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simplem Thresholded Inverse',thresh_inv)

#Adaptative Thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11,9)
cv.imshow('Adaptive thresholding',adaptive_thresh)


cv.waitKey(0)
