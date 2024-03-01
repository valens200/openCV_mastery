import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../../../images/lena.jpg")

# () holds the size of the kernel while -2 is the standard deviation
# The more standard deviation => less blur
# large kennel size results into more extensize bluring
blurredImage = cv2.GaussianBlur(image,(39,91),-2)

cv2.imshow("Blured image", blurredImage)
cv2.waitKey(0)
cv2.destroyAllWindows()