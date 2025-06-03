import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://blueline.md/contacte/")
driver.implicitly_wait(10)
button = driver.find_element(By.CSS_SELECTOR,".contacts__btns ._popup-link")
print(f"button: {button}")
button.click()

input_name = driver.find_element(By.CSS_SELECTOR, ".form input[name='your-name']")

# Wait until the input value becomes "test"
WebDriverWait(driver, 10).until(
    lambda d: input_name.get_attribute("value") == "test"
)

if input_name.get_attribute("value") == "test":
    print("Input name is set to 'test'")

time.sleep(500)
