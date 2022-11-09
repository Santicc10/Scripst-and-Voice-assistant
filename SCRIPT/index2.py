from tkinter import Button
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s= Service("C:/Users/chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://www.youtube.com")
searchbox = driver.find_element("xpath", '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
searchbox.send_keys('de tanto chimbear')
searchButton = driver.find_element("xpath", '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button') 
searchButton.click()
time.sleep(30)

driver.quit()