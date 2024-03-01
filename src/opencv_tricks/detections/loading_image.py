import cv2
import matplotlib.pyplot as plt


imageUrl =  "../../images/lena.jpg"

image = cv2.imread(imageUrl)

plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title("Image")
plt.show()
