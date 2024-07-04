import cv2
import pytesseract
from PIL import Image

# read image
im = cv2.imread('upscale-text-image-1.jpg')

# convert the image from BGR (OpenCV format) to RGB (PIL format)
im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# convert the numpy array to a PIL image
pil_image = Image.fromarray(im_rgb)

# configurations
config = ('-l eng --oem 1 --psm 3')

# pytesseract
text = pytesseract.image_to_string(pil_image, config=config)

# print and save text
with open('output.txt', 'w') as f:
    f.write(text)

print(text)
