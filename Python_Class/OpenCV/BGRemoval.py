import cv2 as cv

# Load images
img1 = cv.imread('strawberry.png')  # background
img2 = cv.imread('LogoOpenCVLogoOpenCV.png')         # logo
assert img1 is not None and img2 is not None, "Image file could not be read."

# Get dimensions of logo
rows, cols, channels = img2.shape

# Define ROI in background image where the logo will go (top-left corner here)
roi = img1[0:rows, 0:cols]

# Convert logo to grayscale
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# Create mask where logo pixels are white and background is black
ret, mask = cv.threshold(img2gray, 250, 255, cv.THRESH_BINARY_INV)

# Inverse mask (optional if you want to keep background)
mask_inv = cv.bitwise_not(mask)

# Black-out the area of the logo in the ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

# Take only the logo from the logo image
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

# Combine background and logo
dst = cv.add(img1_bg, img2_fg)

# Put combined image back into original
img1[0:rows, 0:cols] = dst

# Show result
cv.imshow('Result', img1)
cv.waitKey(0)
cv.destroyAllWindows()
