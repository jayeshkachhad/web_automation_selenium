import csv
from bs4 import BeautifulSoup
import requests
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import base64

driver = webdriver.Chrome()
actions = ActionChains(driver)
url = 'https://www.flipkart.com/woodland-men-outdoors-shoes/p/itmf3xk3t97y9gge?pid=SHOEBGZFSZGXHWCK&lid=LSTSHOEBGZFSZGXHWCKNTJRZR&marketplace=FLIPKART&q=woodland+shoes&store=osp%2Fcil%2Fe1f&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&fm=search-autosuggest&iid=33c43afb-3c7b-4f4b-ad60-ab895f761ba9.SHOEBGZFSZGXHWCK.SEARCH&ppt=sp&ppn=sp&ssid=6avflxkk680000001727719933891&qH=e5e6651393ac2c38'

driver.get(url)
driver.maximize_window()
time.sleep(20)

url_push = 'https://www.pushsafer.com/api'
post_fields = {
	"t" : 'Alert',
	"m" : 'Price Drop',
	"s" : 11,
	"v" : 3,
	"i" : 33,
	"c" : '#FF0000',
	"d" : 'a',
	"u" : 'https://www.pushsafer.com',
	"ut" : 'Open Pushsafer',
	"k" : '6bXm7ePPLStqqnzhLXrh',
	# "p" : 'data:image/jpeg;base64,'+str(image1.decode('ascii')),
	# "p2" : 'data:image/png;base64,'+str(image2.decode('ascii')),
	}


try:
    for i in range(2000):
        driver.get(url)
        time.sleep(10)
        name = driver.find_element(By.XPATH, "//span[@class='VU-ZEz']").text
        price  = driver.find_element(By.XPATH, "//div[@class='Nx9bqj CxhGGd']").text
        result = name, " = ", price
        print(result)
        price = price.replace("₹", "")
        price = price.replace(",", "")
        price_int = int(price)
        print(time.ctime())

        if price_int < 800 :
            print("Price Drop")
            request = Request(url_push, urlencode(post_fields).encode())
        else:
            continue

except:
    print("Error")
