import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../../../images/l.png")
image2 = cv2.imread("../../../images/lm.png")
image3 = cv2.imread("../../../images/image2.png")
image4 = cv2.imread("../../../images/r.png")

stitcher = cv2.Stitcher_create()
status, result = stitcher.stitch((image,image2,image3,image4))

if status == cv2.Stitcher_OK:
    croppedImage = result[10:-45, :]
    
    
    cv2.imshow("Cropped image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite("cropped_image.jpg", croppedImage)
else:
    print("Stitching failed")