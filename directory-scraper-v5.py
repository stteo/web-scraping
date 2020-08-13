# Version 4 uses campus directory advanced and catches edge cases where 1+ users are found with campus email search

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
import requests
import json 

print ("directory-scraper-v4.py - program starts")

# SETUP SITEIMPROVE API KEY 
api_user = "stteo@ucsc.edu"
api_key = "2d907394ada437a4161b83100d97ad85"
resource = "https://api.siteimprove.com/v2"
url = "https://api.siteimprove.com/v2/settings/users?page=1&page_size=100&query=ucsc.edu"
response = requests.get(url, auth=(api_user, api_key))
account = json.loads(response.text)

if (response.status_code == 200): # verify api key connection
    print("API connection established for user: " + api_user)
else: 
    print("API connection not established for user: " + api_user)

# SETUP SELENIUM WEB SCRAPER
PATH = "/Users/ttwsam/Documents/WebDriver/chromedriver"
driver = webdriver.Chrome(PATH)
print (driver.title + "setup complete")

driver.get("https://campusdirectory.ucsc.edu/cd_advanced") # navigates to campus directory link
email_search_box = driver.find_element_by_name("data[mail][0]") # searches for "campus email" search box by html element name

# SETUP DATA SOURCE (currently using api)
# df = pd.read_csv('users-list.csv')
df = pd.DataFrame(account["items"])
correct_message = ("1 record matched your search request.")
incorrect_message = ("Your search did not return any records")
index_count = 0 

# CHECK USERS AGAINST CAMPUS DIRECTORY
for index, row in df.iterrows():
    current_user = row['email']
    email_search_box.send_keys(current_user)
    email_search_box.send_keys(Keys.RETURN)

    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="directoryContent"]/h3[2]'))
    )

    if (element.text) == (correct_message):
        print('Siteimprove User (' + current_user + '): ' + element.text)
        
    elif (element.text) == (incorrect_message):
        print('Siteimprove User (' + current_user + '): ' + element.text)
    else: 
        print('Siteimprove User (' + current_user + '): ' + element.text)
        name_search_box = driver.find_element_by_name("data[cn][0]")
        name_search_box.send_keys(df["name"].iloc[index_count])
        name_search_box.send_keys(Keys.RETURN)
        element_name_search = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="directoryContent"]/h3[2]'))
        )
        print("     Searching for " + df["name"].iloc[index_count] + " returns: " + element_name_search.text)

    index_count = (index_count + 1) 

    email_search_box = driver.find_element_by_name("data[mail][0]") 
    email_search_box.clear()
    name_search_box = driver.find_element_by_name("data[cn][0]") 
    name_search_box.clear()

# BREAKDOWN 
time.sleep(5)
print ("directory-scraper-v4.py - program ends")
driver.quit() 
