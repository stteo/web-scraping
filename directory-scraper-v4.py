# Version 3 can successfully use import a csv file and iterate through the email row with Selenium

# This project is to automate web scripting for Siteimprove User Management
# Last Updated: August 7th, 2020 
# stteo@ucsc.edu

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# SETUP 
print ("directory-scraper-v4.py - program starts")
df = pd.read_csv('users-list.csv')
PATH = "/Users/ttwsam/Documents/WebDriver/chromedriver"
driver = webdriver.Chrome(PATH)
print (driver.title + "setup complete")

driver.get("https://campusdirectory.ucsc.edu/cd_advanced") 
search_box = driver.find_element_by_name("data[mail][0]")

# ITERATE THROUGH LIST
for index, row in df.iterrows():s
    current_user = row['Email']
    search_box.send_keys(current_user)
    search_box.send_keys(Keys.RETURN)

    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="directoryContent"]/h3[2]'))
    )
    
    print('Name: (' + current_user + '): ' + element.text)
   
    search_box = driver.find_element_by_id("data[mail][0]") #have to redeclare the element again for some reason 
    search_box.clear()

# BREAKDOWN 
time.sleep(5)
print ("directory-scraper-v4.py - program ends")
driver.quit() 