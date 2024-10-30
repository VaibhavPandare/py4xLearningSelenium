import time

from selenium import webdriver
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Actions")
@allure.description("Verify click and hold")

def test_verify_actions_spicejet():
    driver=webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()
    #WebDriverWait(driver=driver,timeout=5).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']")))
    from_city=driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']")
    time.sleep(5)
    actions=ActionChains(driver)
    actions.move_to_element(from_city).click().send_keys("DEL").perform()
    time.sleep(10)