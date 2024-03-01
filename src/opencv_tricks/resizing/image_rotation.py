import cv2
import matplotlib.pyplot as plt


loadedImage = cv2.imread("../../images/lena.jpg")

cols , rows = loadedImage.shape[:2]
rotationMatrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45,1)
rotatedImage = cv2.warpAffine(loadedImage,rotationMatrix,(cols,rows))

cv2.imshow("Rotated Lena image", rotatedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

























# # calculate the number of rows and columns of the image
# rows, cols = loadedImage.shape[:2]

# # calculate the the rotational matrix to be used
# rotationMatrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45,2)
# # the actual rotation.
# rotatedImage = cv2.warpAffine(loadedImage, rotationMatrix,(cols,rows))