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
print ("program begins and setup starts")
df = pd.read_csv('users-list.csv')
PATH = "/Users/ttwsam/Documents/WebDriver/chromedriver"
driver = webdriver.Chrome(PATH)
print (driver.title + "setup complete")

driver.get("https://campusdirectory.ucsc.edu/cd_simple") 
search_box = driver.find_element_by_id("keyword")
print ("got website and search box")

# ITERATE THROUGH LIST
for index, row in df.iterrows():
    current_user = row['Email']
    search_box.send_keys(current_user)
    search_box.send_keys(Keys.RETURN)

    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="directoryContent"]/h3[2]'))
    )

    if ((element.text) == "1 record matched your search request.")
        print('Siteimprove User ID (' + current_user + ') is found in UCSC campus database')
    else: 
        print('Testing for Siteimprove User ID (' + current_user + ')')

    search_box = driver.find_element_by_id("keyword") #have to redeclare the element again for some reason 
    search_box.clear()

# BREAKDOWN 
time.sleep(5)
print ("end of program")
driver.quit() 