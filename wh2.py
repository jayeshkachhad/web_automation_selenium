import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from openpyxl import load_workbook

wb = load_workbook('contacts.xlsx')
ws = wb.active

driver = webdriver.Chrome()
actions = ActionChains(driver)
url = 'https://web.whatsapp.com/'

driver.get(url)
driver.maximize_window()
time.sleep(15)

driver.find_element(By.CSS_SELECTOR, ".selectable-text.copyable-text.x15bjb6t.x1n2onr6").send_keys("7818922430")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "div[class='x1n2onr6']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//div[@class='_ak8h']").click()
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(1)
actions.send_keys(Keys.ENTER)
time.sleep(1.5)

