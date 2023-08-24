import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture(params= [("Credencetest@test.com","Credence@123"),
    ("Credencetest@test.com1","Credence@123"),
    ("Credencetest@test.com","Credence@1231"),
    ("Credencetest@test.com1","Credence@1231"),
                         ("ashleshazambare@gmail.com", "Neha@7276")])
def getDataForLogin(request):
    return request.param

@pytest.fixture(scope="class")
def setup1():
    print("i am executing before")
    yield
    print(" I am executing at last")


def pytest_addoption(parser):
    parser.addoption("--browser_name", action = "store", default = "chrome")

@pytest.fixture
def cross_browser(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome()

    elif browser_name == "Firefox":
        driver = webdriver.Firefox()

    elif browser_name == "IE":
        driver = webdriver.Ie()

    else:
        Options = webdriver.ChromeOptions()
        Options.add_argument("headless")
        driver = webdriver.Chrome(options= Options)

    driver.maximize_window()
    return driver








