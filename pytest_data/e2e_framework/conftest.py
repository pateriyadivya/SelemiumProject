import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    #Give path to the browser driver
    service_obj = Service("C:/Users/divya/Downloads/chromedriver_win32/chromedriver.exe")

    #If the browser closes automatically, below is how to sustain
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    #DriverObj is intermediation bw our system and chrome
    driver = webdriver.Chrome(service=service_obj)

    driver.implicitly_wait(5)