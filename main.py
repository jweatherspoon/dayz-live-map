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

    ads_removed = False
    cookies_msg_removed = False 

    # Check every second for a new position 
    while True:
        time.sleep(1.5)

        # # Try to remove the ads if they haven't been yet
        # if not ads_removed:
        #     ads_removed = b.tryRemoveAds()
        # # Try to remove the cookie msg if it hasn't yet 
        # if not cookies_msg_removed:
        #     cookies_msg_removed = b.tryRemoveCookiesMsg()

        img_data = ocr.get_image(BOUNDS)

        try:
            newPos = ocr.find_digits(img_data)
        except:
            continue

        # Update the map if any of the coordinates differ by 5
        if oldPos.size == 3 and newPos.size == 3:
            if (np.abs(newPos - oldPos) > 25).any():
                oldPos = np.copy(newPos)
                b.findLocation(newPos[0], newPos[2])

