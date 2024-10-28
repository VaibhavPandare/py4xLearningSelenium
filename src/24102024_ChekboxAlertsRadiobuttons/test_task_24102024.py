import time


from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_buttonandcheckbox():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    radio_button=driver.find_element(By.ID,"sex-1")
    radio_button.click()
    radio_button_one = driver.find_element(By.ID, "exp-2")
    radio_button_one.click()
    checkbox = driver.find_element(By.ID, "profession-1")
    checkbox.click()
    time.sleep(5)