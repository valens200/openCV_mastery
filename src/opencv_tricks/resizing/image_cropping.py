import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../../images/lena.jpg")

# the first parameter is the range of rows  [ from 0  to 299 ] towhile the second parameter is the range of columns [ from 200 to 399]
croppedImage = image[0:300, 200:400]

convertedImage = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
plt.imshow(convertedImage, cmap="gray")
plt.title("Cropped image")
plt.show()
# cv2.imshow("Cropped image",croppedImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()