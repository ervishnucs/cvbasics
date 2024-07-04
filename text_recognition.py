import cv2
import pytesseract

try:
    # read image
    im = cv2.imread('upscale-text-image-1.jpg')
    if im is None:
        raise FileNotFoundError("The image file 'testimg.jpg' was not found.")
    print("Image loaded successfully.")

    # configurations
    config = ('-l eng --oem 1 --psm 3')

    # pytesseract
    text = pytesseract.image_to_string(im, config=config)
    print("Text recognition applied successfully.")

    # save text
    with open('output.txt', 'w') as f:
        f.write(text)
    print("Text saved successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
    raise
