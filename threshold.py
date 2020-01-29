import cv2 as cv
import numpy as np
img=cv.imread(r'temp.png')
_,th1=cv.threshold(img,130,255,cv.THRESH_BINARY)
_,th2=cv.threshold(img,230,255,cv.THRESH_BINARY_INV)
_,th3=cv.threshold(img,100,255,cv.THRESH_TRUNC)
_,th4=cv.threshold(img,100,255,cv.THRESH_TOZERO)
_,th5=cv.threshold(img,100,255,cv.THRESH_TOZERO_INV)
img1=cv.add(th1,th2)

cv.imshow('image',img)
cv.imshow('thr1',th1)
cv.imshow('thr2',th2)
cv.imshow('thr3',th3)
cv.imshow('th4',th4)
cv.imshow('th5',th5)
cv.imshow('imag',img1)
cv.waitKey(0)
cv.destroyAllWindows()
