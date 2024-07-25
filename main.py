import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Hello World")

time.sleep(10)

driver.quit()
