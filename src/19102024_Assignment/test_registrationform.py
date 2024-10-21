import time
from time import sleep

from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By


@allure.title("Verify the registration page")
@allure.description("Verify the user is able to register")
def test_verify_registration_page():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name=driver.find_element(By.XPATH,"//input[@id='input-firstname']")
    first_name.send_keys("vaibhav")
    time.sleep(2)

    last_name = driver.find_element(By.XPATH, "//input[@id='input-lastname']")
    last_name.send_keys("panadare")
    time.sleep(2)

    email = driver.find_element(By.XPATH, "//input[@id='input-email']")
    email.send_keys("vaibhav18@gmail.com")
    time.sleep(2)

    telephone = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    telephone.send_keys("9998765432")
    time.sleep(2)

    password = driver.find_element(By.XPATH, "//input[@id='input-password']")
    password.send_keys("vaibhav16")
    time.sleep(2)

    password_confirm = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
    password_confirm.send_keys("vaibhav16")
    time.sleep(2)

    privacy_chk=driver.find_element(By.NAME,"agree")
    privacy_chk.click()
    time.sleep(2)

    submit_btn=driver.find_element(By.XPATH,"//input[@type='submit']")
    submit_btn.click()

    page_source_data=driver.page_source

    assert "Your Account Has Been Created!" in page_source_data

    time.sleep(10)