import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
actions = ActionChains(driver)
url = 'https://web.whatsapp.com/'

driver.get(url)
driver.maximize_window()
time.sleep(25)

cookies = driver.get_cookies()
pickle.dump(cookies, open('cookies.pkl', 'wb'))

# driver.find_element(By.CSS_SELECTOR, "span[data-icon='new-chat-outline']").click()
# time.sleep(5)

# driver.find_element(By.CSS_SELECTOR, "span[title='G. post  A A PATEL']").click()
# driver.find_element(By.XPATH, "//span[@title='G. post  A A PATEL']")
# driver.find_element(By.CSS_SELECTOR, "div[title='Search input textbox'] p[class='selectable-text copyable-text iq0m558w g0rxnol2']").send_keys("9624105441")
# driver.find_element(By.CSS_SELECTOR, "div[class='_ai07 _ai01 _akmh'] p[class='selectable-text copyable-text x15bjb6t x1n2onr6']").send_keys("9624105441")
# time.sleep(2)
# actions.send_keys(Keys.ENTER)
time.sleep(10)





# actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
