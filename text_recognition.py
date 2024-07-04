import cv2
import pytesseract

# read image
im = cv2.imread('./testimg.jpg')

# configurations
config = ('-l eng --oem 1 --psm 3')

# pytesseract
text = pytesseract.image_to_string(im, config=config)

# print and save text
with open('output.txt', 'w') as f:
    f.write(text)

print(text)
