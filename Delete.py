from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Open the website
driver.get("https://www.hollandandbarrett.com/en-au/")
time.sleep(5)
driver.save_screenshot("website_opened.png")

# Step 2: Click on Rewards section
driver.find_element(By.XPATH, "//h3[normalize-space()='Rewards for Life']").click()
time.sleep(5)
driver.save_screenshot("rewards_section.png")

# Step 3: Click on Create Account
driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()
time.sleep(5)
driver.save_screenshot("create_account_option.png")

# Step 4: Fill account creation details
driver.find_element(By.ID, "firstName").send_keys("Upendhar")
driver.find_element(By.NAME, "lastName").send_keys("Ambati")
driver.find_element(By.NAME, "email").send_keys("208r1a05i2cse@gmail.com")
driver.find_element(By.NAME, "confirmEmail").send_keys("208r1a05i2cse@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Lasmaiah@5014")
driver.find_element(By.XPATH, "//label/input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//button/span[normalize-space()='Create Account']").click()
time.sleep(5)
driver.save_screenshot("account_created.png")

# Close the browser
driver.quit()
