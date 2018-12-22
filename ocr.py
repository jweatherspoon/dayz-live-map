
import matplotlib.pyplot as plt 
import numpy as np 
import pytesseract 
import cv2 
import time 
from PIL import ImageGrab
import string 

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract"

BOUNDS = (1700, 90, 1860, 105)
REMOVE_CHARS = '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
TRAN_TABLE = dict.fromkeys(map(ord, REMOVE_CHARS), None)

def crop_position(img_data):
    COLS = [1700,1860]
    ROWS = [90,105]
    return np.array([row[COLS[0]:COLS[1]] for row in img_data[ROWS[0]:ROWS[1]]])

def process_image(img_data):
    threshold = 90 
    bw_img = (img_data[:,:,:2] > threshold).all(axis=2)
    return bw_img

def find_digits(position_img):
    # For now, save the image to file and then use tesseract to extract the text
    fname = "bw_position_cropped.png"
    plt.imsave(fname, position_img, cmap='gray')
    text = pytesseract.image_to_string(fname)
    text = text.translate(TRAN_TABLE)

    positions = np.array(text.split(' '))
    return positions

if __name__ == "__main__":
    pos = None
    while True:
        # Get a screenshot every 10 seconds
        im = ImageGrab.grab(BOUNDS)
        img_data = np.array(im)
        # Process it
        # cropped = crop_position(img_data)
        # bw = process_image(img_data)
        # bw = img_data
        # Print the location of the player 
        try:
            pos = find_digits(img_data)
            print(pos)
        except Exception as e:
            print("Failed to find position from image data")
            print(e)
        time.sleep(1)


# data = cv2.imread('screenshot.jpg')
# cropped = crop_position(data)
# bw = process_image(cropped)
# pos = find_digits(bw)
