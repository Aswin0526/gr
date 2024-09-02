import cv2 

img  = cv2.imread('gradient.png',1)

_,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
print(img)
cv2.imshow('gradient',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)

cv2.waitKey(0)
cv2.destroyAllWindows()