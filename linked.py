import csv
import time
import pickle
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import base64

driver = webdriver.Chrome()
actions = ActionChains(driver)
# url = 'https://www.flipkart.com/woodland-men-outdoors-shoes/p/itmf3xk3t97y9gge?pid=SHOEBGZFSZGXHWCK&lid=LSTSHOEBGZFSZGXHWCKNTJRZR&marketplace=FLIPKART&q=woodland+shoes&store=osp%2Fcil%2Fe1f&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&fm=search-autosuggest&iid=33c43afb-3c7b-4f4b-ad60-ab895f761ba9.SHOEBGZFSZGXHWCK.SEARCH&ppt=sp&ppn=sp&ssid=6avflxkk680000001727719933891&qH=e5e6651393ac2c38'
url = 'https://www.linkedin.com/feed/'

driver.get(url)
driver.maximize_window()
# time.sleep(2)

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
time.sleep(2)
# driver.get(url)

# time.sleep(5)

driver.get("https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAADtzXmgB4Z1DZ9Z3VBnlZEOpusBFccLGtIE%22%5D&network=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&sid=bYA")
time.sleep(5)

for i in range(22):
    driver.find_element(By.CSS_SELECTOR, "button[id='ember227'] svg").click()
    time.sleep(2)

# time.sleep(10)
