from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class Browser():
    def __init__(self):
        self._b = webdriver.Chrome()
    
    def goToMap(self):
        self._b.get("https://dayz.ginfo.gg/chernarusplus/")

    def findLocation(self, x, y):
        if type(x) != str:
            x = str(x) 
        if type(y) != str:
            y = str(y)
            
        try:
            city_search = self._b.find_element_by_id("citysearch")
            city_search.clear()
            city_search.send_keys(f'{x} {y}')
            city_search.send_keys(Keys.ENTER)
        except:
            pass 

    def tryRemoveAds(self):
        try:
            self._b.execute_async_script(
                "document.getElementsByClassName('leaderboard')[0].remove();"
            )
            return True 
        except: 
            return False 

    def tryRemoveCookiesMsg(self):
        try:
            self._b.execute_async_script(
                "document.body.firstChild.remove();"
            )
            return True 
        except:
            return False
