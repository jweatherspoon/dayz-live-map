
import matplotlib.pyplot as plt 
import numpy as np 
import pytesseract 
import cv2 

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

    positions = np.array(text.split(' ')).astype(float)
    return positions

# data = cv2.imread('screenshot.jpg')
# cropped = crop_position(data)
# bw = process_image(cropped)
# pos = find_digits(bw)
