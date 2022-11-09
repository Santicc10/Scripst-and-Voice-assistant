from tkinter import Button
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
web_element = driver.find_element(By.NAME, 'q')
web_element.send_keys("Grupos del mundial" + Keys.ENTER)
time.sleep(10)
driver.quit()






