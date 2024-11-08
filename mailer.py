import time

from pushbullet import pushbullet
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from openpyxl.styles import Font
from pushbullet import Pushbullet


API_KEY = "o.QVhTjKwCECLRDhVEUPR8PJNhrIAgxipO"
pb = Pushbullet(API_KEY)

