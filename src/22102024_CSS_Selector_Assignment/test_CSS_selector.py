import time
from functools import reduce
from lib2to3.pgen2 import driver
from symbol import return_stmt
from cleantext import clean

from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest


@allure.title("Get all the titles and prices")
@allure.description("User is able to view all the titles and prices")
def test_titles_prices():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    search_box = driver.find_element(By.CLASS_NAME, "ui-autocomplete-input")
    search_box.send_keys("Macmini")
    search_button = driver.find_element(By.ID, "gh-btn")
    search_button.click()

    #Created the empty list and added all the items titles using append and printed them in list
    item_titles = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    list_b=[]
    for i in item_titles:
     list_b.append(i.text)
    print(list_b)

    # Created the empty list and added all the items prices using append and printed them in list
    item_prices = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    list_a = []
    for j in item_prices:
     list_a.append(j.text)
    print(list_a)

    #This will print the items name and items price side by side
    for x,y in zip (list_b,list_a):
        print(x,y, sep='\t\t')

    # This remove the blank strings in list
    while ("" in list_a):
        list_a.remove("")
    print("Modified list is :",str(list_a))

   #item_values=[s.lstrip("$")for s in list_a]
    #print(item_values)


