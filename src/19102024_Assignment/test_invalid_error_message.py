import time

from selenium import webdriver

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("Verify the error message after wrong username or password")
@allure.description("Verify error message is displayed for invalid username or password")
def test_validation_message():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)  # # Create the Session
    #driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get(" https://app.vwo.com/")
    login_user_name = driver.find_element(By.ID, "login-username")
    login_user_name.send_keys("vaibhav@yahoo.com")
    time.sleep(5)
    login_password = driver.find_element(By.ID, "login-password")
    login_password.send_keys("vaibhav123")
    sign_in_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    sign_in_btn.click()
    time.sleep(5)
    error_message = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message.text)
    assert error_message.text == "Your email, password, IP address or location did not match"
    time.sleep(10)
