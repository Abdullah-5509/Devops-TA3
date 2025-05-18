from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start the browser
driver = webdriver.Chrome()

# Open your Flask app (make sure it's running locally)
driver.get("http://127.0.0.1:5000")

# === Test Case 1: Valid city ===
city_input = driver.find_element(By.ID, "cityInput")
city_input.clear()
city_input.send_keys("London")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)  # wait for fetch

assert "London" in driver.page_source
print("✅ Test 1 Passed: Valid city")

# === Test Case 2: Invalid city ===
city_input = driver.find_element(By.ID, "cityInput")
city_input.clear()
city_input.send_keys("asdfasdf")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)

assert "Error" in driver.page_source
print("✅ Test 2 Passed: Invalid city")

# === Test Case 3: Empty input ===
city_input = driver.find_element(By.ID, "cityInput")
city_input.clear()
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)

assert "Error" in driver.page_source
print("✅ Test 3 Passed: Empty input")

# Close the browser
driver.quit()
