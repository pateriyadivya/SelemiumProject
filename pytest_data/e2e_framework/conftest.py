import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Introducing command line options
# Here we will expect the user to give a command line input in case they wish to invoke a specific browser

def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store", default="chrome") # browser_name is the key that should be written in CLI along with its desired value


@pytest.fixture(scope="class")
def setup(request): # Using request arg allow us to send driver as an object to methods calling this fixtures
    Browser = request.config.getoption("browser_name") #Here we assign the I/P by the user into the Browser variable

    if Browser == "chrome":
        service_obj = Service("C:/Users/divya/Downloads/chromedriver_win32/chromedriver.exe")
        #If the browser closes automatically, below is how to sustain
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        #DriverObj is intermediation bw our system and chrome
        driver = webdriver.Chrome(service=service_obj)
    elif Browser == "firefox":
        print("Please add the respective executable path here!!!")

    driver.implicitly_wait(5)
    request.cls.driver = driver # sending driver object to a class which calls the fixture

    yield
    driver.close()