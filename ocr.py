
import matplotlib.pyplot as plt 
import numpy as np 

def crop_position(img_data):
    COLS = [1700,1860]
    ROWS = [90,105]
    return np.array([row[COLS[0]:COLS[1]] for row in img_data[ROWS[0]:ROWS[1]]])

data = plt.imread('screenshot.jpg')
cropped = crop_position(data)
plt.imsave('position.png', cropped)