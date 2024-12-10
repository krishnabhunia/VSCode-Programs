from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()
# Replace with your Facebook credentials
FB_EMAIL = os.getenv("FB_USERNAME")
FB_PASSWORD = os.getenv("FB_PASSCODE")

# Path to ChromeDriver
CHROMEDRIVER_PATH = "C:\Program Files\Google\Chrome\Application"

# Initialize WebDriver
driver = webdriver.Chrome(CHROMEDRIVER_PATH)

try:
    # Navigate to Facebook login page
    driver.get("https://www.facebook.com/login")

    # Log in to Facebook
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")
    login_button = driver.find_element(By.NAME, "login")

    email_input.send_keys(FB_EMAIL)
    password_input.send_keys(FB_PASSWORD)
    login_button.click()

    # Wait for the page to load
    time.sleep(5)

    # Navigate to friends page
    driver.get("https://www.facebook.com/me/friends")

    # Wait for the friends page to load
    time.sleep(5)

    # Extract friend names
    friends = driver.find_elements(By.XPATH, "//a[contains(@href, 'friend_id')]")
    friend_names = [friend.text for friend in friends if friend.text]

    print("Friends List:")
    print(friend_names)

finally:
    # Close the browser
    driver.quit()
