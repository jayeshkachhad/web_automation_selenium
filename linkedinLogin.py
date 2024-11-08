import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
actions = ActionChains(driver)
url = 'https://www.linkedin.com/feed/'
time.sleep(1)

driver.get(url)
driver.maximize_window()

time.sleep(5)
cookies = pickle.load(open("cookies_linkedin.pkl", "rb"))

for cookie in cookies:
    cookie['domain'] = ""
    driver.add_cookie(cookie)
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(e)

driver.get(url)
time.sleep(50)
