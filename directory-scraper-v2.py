# This project is to automate web scripting for Siteimprove User Management
# Last Updated: August 5th, 2020 
# stteo@ucsc.edu

# v1 has selenium working to search a user

from selenium import webdriver
from selenium.webdriver.common.keys import Keys ##to use esc/enter/etc keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/ttwsam/Documents/WebDriver/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://campusdirectory.ucsc.edu/cd_simple") #gets website
print (driver.title)

search = driver.find_element_by_id("keyword")
search.send_keys("stteo@ucsc.edu")
search.send_keys(Keys.RETURN)

time.sleep(20)
driver.quit() 
