import ocr 
import browser
import time

import numpy as np 

from settings import BOUNDS 

if __name__ == "__main__":
    b = browser.Browser()
    b.goToMap()

    oldPos = np.zeros(3)
    newPos = np.zeros(3)

    # Check every second for a new position 
    while True:
        time.sleep(1)
        img_data = ocr.get_image(BOUNDS)

        try:
            newPos = ocr.find_digits(img_data)
        except:
            continue

        # Update the map if any of the coordinates differ by 5
        if (np.abs(newPos - oldPos) > 5).any():
            oldPos = np.copy(newPos)
            b.findLocation(newPos[0], newPos[2])

