import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
act = ActionChains(driver)

url = "https://www.victoriassecret.in/vs/bras"

driver.get(url)
driver.maximize_window()
time.sleep(1)

# blist = driver.find_elements(By.CSS_SELECTOR, "div[class='pdp-link productTile-name productTile-namecustom']")
blist = driver.find_elements(By.TAG_NAME, 'a')

# print(len(blist))

for i in range(len(blist)):
    print(blist[i].get_attribute('href'))

time.sleep(5)