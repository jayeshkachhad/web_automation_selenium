import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# url = 'https://www.google.com'
url = 'https://watchseries8.to/'

driver.get(url)
time.sleep(5)

# search_box = driver.find_element(by=By.ID, "APjFqb")
search_box = driver.find_element_by_id("APjFqb")
# search_box = driver.find_element(by=By.CSS_SELECTOR, 'div.is-button')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()