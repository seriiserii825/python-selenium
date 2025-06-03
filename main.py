import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://blueline.md")
driver.implicitly_wait(10)
button = driver.find_element(By.CSS_SELECTOR,".btn-scroll")
print(f"button: {button}")
button.click()
time.sleep(5)  # Wait for the page to load after clicking the button
