import cv2
import numpy as np
ix=0
iy=0
def nothing(x):
    pass
img1=cv2.imread('1.jpg')
def mouse_cordinates(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
            tolerancia = 2
            connectivity = 4
            flags = connectivity
            global ix
            global iy
            ix=x
            iy=y
            r=cv2.getTrackbarPos('R','image')
            g=cv2.getTrackbarPos('G','image')
            b=cv2.getTrackbarPos('B','image')
            cv2.floodFill(img1, None, (ix,iy), (b, g, r), (tolerancia,) * 3, (tolerancia,) * 3, flags)
            print ix,iy
            cv2.imshow('image',img1)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)


cv2.setMouseCallback('image',mouse_cordinates)
cv2.imshow('image',img1)
while(1):
    if cv2.waitKey(0)==27:
        break
cv2.destroyAllWindows()
