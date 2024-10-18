from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_verify_login():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    make_appointment=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment.click()
    current_url=driver.current_url
    assert current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    username=driver.find_element(By.ID,"txt-username")
    username.click()
    username.send_keys("John Doe")
    password=driver.find_element(By.ID,"txt-password")
    password.click()
    password.send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID,"btn-login").click()

    sleep(10)

