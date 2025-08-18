from typing import final

import cv2 as cv
import numpy as np

# Lower red range
lower_red = np.array([0, 0, 120])     # allow some green/blue
upper_red = np.array([100, 100, 255]) # allow up to light reds


img = cv.imread('strawberry.png')
mask1 = cv.inRange(img, lower_red, upper_red)
mask_bgr = cv.cvtColor(mask1, cv.COLOR_GRAY2BGR)
mask_bgr[mask1 == 255] = (1,1,238)
finalmask = constant= cv.copyMakeBorder(mask_bgr,10,10,10,10,cv.BORDER_CONSTANT,value=[234,0,12])
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(finalmask,'STRAWBERRY',(0,50), font, 1,(255,255,255),2,cv.LINE_AA)
cv.imshow("Strawberry",finalmask)
k = cv.waitKey(0)