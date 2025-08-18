import cv2 as cv

img1 = cv.imread('strawberry.png')
img2 = cv.imread('strawberry2.png')
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"

dst = cv.addWeighted(img1,0.2,img2,1,0)

cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()