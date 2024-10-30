import time

from selenium import webdriver
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@allure.title("Action P3")
@allure.description("Verify Click and Hold and Drop")
def test_verify_action_keywords():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #dragable
    element_to_hold=driver.find_element(By.ID,"draggable")

    #Key Down
    actions=ActionChains(driver)
    actions.click_and_hold(on_element=element_to_hold).perform()
    time.sleep(5)

    #Element on which to drop
    element_on_to_drop=driver.find_element(By.ID,"droppable")
    ActionChains(driver).drag_and_drop(element_to_hold,element_on_to_drop).perform()
    time.sleep(10)
