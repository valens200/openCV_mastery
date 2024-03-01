import cv2

image = cv2.imread("../../../images/m.png")

# import haar cascade model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# haar scade
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
for(x,y,w,h) in faces:
    cv2.recatangle(image, (x,y),( x + w , y + h), (255,0,0),2)

cv2.imshow("Faces detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()