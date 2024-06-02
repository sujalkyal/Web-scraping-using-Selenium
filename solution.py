import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from a .env file
load_dotenv()

# Retrieve credentials from environment variables
username = os.getenv("SAUCEDemo_USERNAME")
password = os.getenv("SAUCEDemo_PASSWORD")

# Ensure credentials are provided
if not username or not password:
    raise ValueError("Username or password not set in environment variables.")

# Set up the Chrome driver
service = Service(executable_path=r"C:\Users\sujal\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

root = "https://www.saucedemo.com/"

try:
    driver.get(root)

    # Input username and password, then attempt login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    try:
        # Check for CAPTCHA presence and handle manually if detected
        captcha_present = False
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]"))
            )
            captcha_present = True
            print("CAPTCHA detected. Please solve the CAPTCHA manually.")
        except:
            pass

        if captcha_present:
            # Wait for user to solve CAPTCHA and reattempt login
            while True:
                try:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
                    )
                    print("CAPTCHA solved and login successful.")
                    break
                except:
                    pass

        # Check for login errors
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        print("Login failed: Incorrect username or password.")
    except:
        # Proceed if login is successful
        print("Login successful.")

        driver.get("https://www.saucedemo.com/inventory.html")

        try:
            # Wait for inventory items to be present and retrieve data
            WebDriverWait(driver, 2).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
            )
            WebDriverWait(driver, 2).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_desc"))
            )

            # Store descriptions of inventory items
            topic_list=driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            text_list = driver.find_elements(By.CLASS_NAME, "inventory_item_desc")
            
            topic_texts = [topic.text for topic in topic_list]
            text_texts = [text.text for text in text_list]

            data={
                "Item": topic_texts,
                "Description": text_texts
            }

            df=pd.DataFrame(data)

            df.to_csv("data_retrieved.csv",index=False)

            print("Data has been retrieved and stored successfully")
        except:
            print("Failed to load inventory items.")
finally:
    # Ensure the browser is closed
    driver.quit()
