# This project is to automate web scripting for Siteimprove User Management
# Last Updated: August 5th, 2020 
# stteo@ucsc.edu

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print ("program begins")

PATH = "/Users/ttwsam/Documents/WebDriver/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://campusdirectory.ucsc.edu/cd_simple") 
print (driver.title)

search_box = driver.find_element_by_id("keyword")
print ("program is working up to getting website")

user_list = ["stteo@ucsc.edu", "tasilva@ucsc.edu", "alyehuan@ucsc.edu"]

for user in user_list:
    print('Siteimprove User ID (' + user + ') testing')
    search_box.send_keys(user)
    search_box.send_keys(Keys.RETURN)

    search_box = driver.find_element_by_id("keyword") #have to redeclare the element again for some reason 
    search_box.clear()
    
time.sleep(10)
print ("end of program")
driver.quit() 