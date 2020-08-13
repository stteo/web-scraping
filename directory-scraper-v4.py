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

# SETUP 
print ("directory-scraper-v4.py - program starts")
df = pd.read_csv('users-list-testing.csv') # reads csv into pandas dataframe
PATH = "/Users/ttwsam/Documents/WebDriver/chromedriver"
driver = webdriver.Chrome(PATH)
print (driver.title + "setup complete")

driver.get("https://campusdirectory.ucsc.edu/cd_advanced") # open campus directory advanced
email_search_box = driver.find_element_by_name("data[mail][0]") # find "Campus Email" search box 

correct_message = ("1 record matched your search request.")
incorrect_message = ("Your search did not return any records")
index_count = 0

# CHECK USERS AGAINST CAMPUS DIRECTORY
for index, row in df.iterrows():

    # input current_user into "Campus Email" search box
    current_user = row['Email']
    email_search_box.send_keys(current_user)
    email_search_box.send_keys(Keys.RETURN)

    # finds search results and sets to var "element"  
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="directoryContent"]/h3[2]'))
    )

    # print out if user has been found or not
    if (element.text) == (correct_message):
        print('Siteimprove User (' + current_user + '): ' + element.text)
    elif (element.text) == (incorrect_message):
        print('Siteimprove User (' + current_user + '): ' + element.text)
    else: # if 2+ users are found when searching "Campus Email", search again for "Full Name"
        name_search_box = driver.find_element_by_name("data[cn][0]") # find "Full Name" search box
        print('Siteimprove User (' + current_user + '): ' + element.text)
        name_search_box.send_keys(df["Name"].iloc[index_count])
        name_search_box.send_keys(Keys.RETURN)
        element_name_search = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="directoryContent"]/h3[2]'))
        )
        print("     Searching for " + df["Name"].iloc[index_count] + " returns: " + element_name_search.text)
        
        # clear "Full Name" search box 
        name_search_box = driver.find_element_by_name("data[cn][0]") 
        name_search_box.clear()

    # clear "Campus Email" search box 
    email_search_box = driver.find_element_by_name("data[mail][0]") 
    email_search_box.clear()
    
    # advance index_count 
    index_count = (index_count + 1) 

# BREAKDOWN 
time.sleep(5)
print ("directory-scraper-v4.py - program ends")
driver.quit() 

