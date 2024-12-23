import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        return driver
    else:
        driver = webdriver.Edge()
        return driver

def pytest_addoption(parser):
    # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")