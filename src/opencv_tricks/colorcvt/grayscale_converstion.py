import cv2
import matplotlib.pyplot as plt

imageUrl =  "../../images/lena.jpg"

loadedImage = cv2.imread(imageUrl)
convertedImage = cv2.cvtColor(loadedImage, cv2.COLOR_BGR2GRAY)

plt.imshow(convertedImage, cmap="gray")
plt.title("Gray scaled Image")
plt.show()

