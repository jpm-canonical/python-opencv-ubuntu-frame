#!/usr/bin/python3
import os
import cv2

windowName = "myImageWindow"

directory = os.getenv("SNAP", default=os.curdir)
image = cv2.imread(directory+'/grace_hopper.bmp')

cv2.namedWindow(windowName, cv2.WINDOW_GUI_NORMAL)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)

while True:
    cv2.imshow(windowName, image)
    keyCode = cv2.waitKey(1)
    if keyCode == 27:
        print('ESC')
        break
    if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyWindow(windowName)
cv2.destroyAllWindows()
