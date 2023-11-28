import pytest
from selenium import webdriver

#variavel global
driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():
#     Setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

# run no test que será executado
    yield

# teardown
    driver.quit()