import cv2 as cv

img1 = cv.imread('strawberry.png')
assert img1 is not None, "file could not be read, check with os.path.exists()"
cv.setUseOptimized(True)
e1 = cv.getTickCount()
for i in range(5,100,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )
cv.imshow("Test",img1)
cv.waitKey(0)

# Result I got is 5.7647425 seconds