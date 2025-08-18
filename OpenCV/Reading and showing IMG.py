
import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("strawberry.png"))
greyimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", greyimg)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)