import cv2
import pytesseract

# Path to Tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Load the image using OpenCV
image = cv2.imread('image.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to preprocess the image (adjust the threshold values as needed)
_, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Perform OCR using Tesseract
extracted_text = pytesseract.image_to_string(threshold_image)

# Print the extracted text
print(extracted_text)
