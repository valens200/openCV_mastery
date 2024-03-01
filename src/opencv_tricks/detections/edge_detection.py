import cv2
import matplotlib.pyplot as plt


loadedImage = cv2.imread("../../images/m.png")
edges = cv2.Canny(loadedImage,50,150)

plt.imshow(edges, cmap="gray")
plt.title("The edges of the image")
plt.show()