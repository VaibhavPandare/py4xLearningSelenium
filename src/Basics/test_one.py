from selenium import webdriver

def test_page_source_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data

def test_page_source_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data

def test_page_source_edge():
        driver = webdriver.Edge()
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        page_source_data = driver.page_source
        assert "CURA Healthcare Service" in page_source_data