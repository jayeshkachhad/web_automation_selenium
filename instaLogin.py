import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
actions = ActionChains(driver)
url = 'https://www.instagram.com/'
time.sleep(1)

driver.get(url)
driver.maximize_window()

time.sleep(5)
cookies = pickle.load(open("insta_cookies.pkl", "rb"))

for cookie in cookies:
    cookie['domain'] = ""
    driver.add_cookie(cookie)
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(e)

driver.get(url)
time.sleep(5)

# driver.find_element(By.CSS_SELECTOR, "class[]")  //class="_a9-- _ap36 _a9_1"
try:
    driver.find_element(By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']").click()
except:
    print("error level 1")
    pass
try:
    time.sleep(2)
    driver.get("https://www.instagram.com/himmatnagar_live/")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a[href='/himmatnagar_live/followers/']").click()
except:
    print("error level 2")
    pass


# _ap3a _aaco _aacw _aacx _aad7 _aade
try:
    soem = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(37) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
except:
    print("error level 3")
    print(soem)
    pass


time.sleep(50)
