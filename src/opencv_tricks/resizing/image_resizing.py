import cv2 
import matplotlib.pyplot as plt

image = cv2.imread("../../images/lena.jpg")
# the first parameter 100 is for width and the second 400 is for height
resizedImage = cv2.resize(image,(100,400))

cv2.imshow("Resized Image", resizedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
