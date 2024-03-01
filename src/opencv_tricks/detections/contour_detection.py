import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../../../images/lena.jpg")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

contours, _ = cv2.findContours(gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0,255,0), 3)

cv2.imshow("countours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

