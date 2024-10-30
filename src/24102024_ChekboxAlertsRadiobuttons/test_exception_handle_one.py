import time
from time import sleep

from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


@allure.title("svg")
@allure.description("Verify svg")

def test_exception_handle():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    time.sleep(5)