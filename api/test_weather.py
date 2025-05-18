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

# === Test Case 4: Check if icon loads ===
city_input = driver.find_element(By.ID, "cityInput")
city_input.clear()
city_input.send_keys("Delhi")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)

icon = driver.find_element(By.TAG_NAME, "img")
assert "openweathermap.org/img/wn/" in icon.get_attribute("src")
print("✅ Test 4 Passed: Weather icon loaded")

# === Test Case 5: Check city and country ===
city_input.clear()
city_input.send_keys("New York")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)

heading = driver.find_element(By.TAG_NAME, "h2").text
assert "New York" in heading
assert "," in heading  # e.g. "New York, US"
print("✅ Test 5 Passed: City and country displayed")

# === Test Case 6: Humidity and pressure values ===
city_input.clear()
city_input.send_keys("Tokyo")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)

text = driver.find_element(By.ID, "result").text
assert "Humidity:" in text and "Pressure:" in text
print("✅ Test 6 Passed: Humidity and Pressure shown")

# === Test Case 7: Loading message replaced ===
city_input.clear()
city_input.send_keys("Paris")
driver.find_element(By.TAG_NAME, "button").click()

loading_text = driver.find_element(By.ID, "result").text
assert "Loading..." in loading_text

time.sleep(2)
new_text = driver.find_element(By.ID, "result").text
assert "Loading..." not in new_text
print("✅ Test 7 Passed: Loading message cleared")

# Close the browser
driver.quit()
