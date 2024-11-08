import pickle
import time
from webbrowser import Chrome
from selenium.webdriver.chrome.options import Options

import selenium.webdriver

driver = selenium.webdriver.Chrome()
chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

driver.get("https://web.telegram.org/")
time.sleep(50)

pickle.dump(driver.get_cookies(), open("/telegram_cookies.pkl", "wb"))

time.sleep(5)