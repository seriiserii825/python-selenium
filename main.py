import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

search_text = input("Enter the text to search: ")

service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://www.google.com")

timeout = 1

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# time.sleep(timeout)
input_element.clear()
input_element.send_keys(search_text)
# time.sleep(timeout)
input_element.send_keys(Keys.RETURN)

link = driver.find_element(By.PARTIAL_LINK_TEXT, search_text)
# time.sleep(timeout)
link.click()
time.sleep(300)

driver.quit()
