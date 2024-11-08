import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
act = ActionChains(driver)

url = "https://goodporn.to/search/Naughty-America/"

driver.get(url)
driver.maximize_window()
time.sleep(1)

# blist = driver.find_elements(By.TAG_NAME, 'a')
# for i in range(len(blist)):
#     print(blist[i].get_attribute('href'))

vids = driver.find_elements(By.CSS_SELECTOR, "div[class='thumb-link']")


for v in vids:
    links = v.get_attribute('innerHTML')
    print(links)


time.sleep(2)