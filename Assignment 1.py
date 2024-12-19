from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Step 1: Setup WebDriver (Chrome)
driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# Open the URL
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
time.sleep(2)
print("Step 1: Opened the URL")

# Step 2: Count number of Radio buttons and Checkboxes and print

# Select BMW Radio Button
bmw_radio_button = driver.find_element(By.ID, "bmwradio")
bmw_radio_button.click()
time.sleep(2)

# Select Benz Radio Button
benz_radio_button = driver.find_element(By.ID, "benzradio")
benz_radio_button.click()
time.sleep(2)

# Select Honda Radio Button
honda_radio_button = driver.find_element(By.ID, "hondaradio")
honda_radio_button.click()
time.sleep(2)

# Select BMW Checkbox
bmw_checkbox = driver.find_element(By.ID, "bmwcheck")
bmw_checkbox.click()
time.sleep(2)

# Select Benz Checkbox
benz_checkbox = driver.find_element(By.ID, "benzcheck")
benz_checkbox.click()
time.sleep(2)

# Select Honda Checkbox
honda_checkbox = driver.find_element(By.ID, "hondacheck")
honda_checkbox.click()
time.sleep(2)

# Find all radio buttons and checkboxes
radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and not(ancestor::div[contains(@style,'display:none')])]")

# Print the number of radio buttons
print(f"Number of radio buttons: {len(radio_buttons)}")
print(f"Number of checkboxes: {len(checkboxes)}")

# Screenshot for Step 2
driver.save_screenshot("step2_radio_checkboxes.png")

# Step 3: Move hand over on "Mouse Hover" and click "Reload"
hover_element = driver.find_element(By.ID, "mousehover")
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(1)

reload_button = driver.find_element(By.XPATH, "//a[contains(text(),'Reload')]")
reload_button.click()
time.sleep(5)
driver.save_screenshot("step3_mouse_hover_reload.png")

# Step 4: Enter "Selenium Python" in Editbox and validate both alerts
edit_box = driver.find_element(By.ID, "name")
edit_box.send_keys("Selenium Python")
time.sleep(1)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)

# Validate alert
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
time.sleep(1)

# Confirm alert
edit_box = driver.find_element(By.ID, "name")
edit_box.send_keys("Selenium Python")
time.sleep(1)
driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()

# Screenshot for Step 4
driver.save_screenshot("step4_alert_handling.png")

# Step 5: Print Page Title, Source Length, and take a screenshot
print("Page Title:", driver.title)
print("Page Source Length:", len(driver.page_source))
driver.save_screenshot("step5_page_details.png")

# Step 6: Validate the title
assert "Practice Page" in driver.title, "Title does not match!"
print("Title validation successful.")

# Step 7: Click Terms and Conditions and Sign In
driver.find_element(By.XPATH, '//*[@id="page"]/div[3]/div/div/div[1]/div/div[2]/ul/li[4]/a').click()
time.sleep(1)
driver.save_screenshot("step7_terms_conditions.png")

driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a').click()
time.sleep(2)

# Step 8: Enter credentials and Sign in
email_box = driver.find_element(By.ID, "email")
password_box = driver.find_element(By.ID, "login-password")
email_box.send_keys("satwikkatamaraju@gmail.com")
password_box.send_keys("wNGVn6@9xDytBDy")
driver.find_element(By.ID, "login").click()
time.sleep(2)

driver.save_screenshot("step8_sign_in.png")

# Step 9: Close the browser
driver.quit()
print("Test script completed successfully.")

