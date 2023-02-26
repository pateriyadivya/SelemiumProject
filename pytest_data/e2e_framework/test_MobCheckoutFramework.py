# End to end application for product checkout from angular webpage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.usefixture("setup") # Calling setup fixture which has to initialize the chrome object
class TestMobileCheckout: # Class name must start with Test
    def test_e2e(self,setup): # All the code must be wrapped in function for the framework, self is mandatory arg in class' method

        # In class to refer its object, self is mandatory to use
        self.driver.get("https://rahulshettyacademy.com/angularpractice/") 

        # Creating CSS_Selector from attribute href = a[href*='shop']
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # mobiles = self.driver.find_elements(By.XPATH, "//app-card-list[@class='row']/app-card")

        mobiles = self.driver.find_elements(By.XPATH, "//app-card-list[@class='row']/app-card/div")

        for mobile in mobiles:
            if mobile.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
                mobile.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='primary']").click()

        assert self.driver.find_element(By.XPATH, "//div[@class='media']/div/h4").text == "Blackberry" # Applicable when there is only one product in th cart
        # Else use the find_elements method and see if the desired product in available in the list

        expected_price = "50000"
        assert expected_price in self.driver.find_element(By.XPATH, "//td[@class='text-right']/h3").text
        self.driver.find_element(By.CSS_SELECTOR, "button[class*=success]").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[class*=touched]").send_keys("ind")
        # time.sleep(5)
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        countries = self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']/label").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[class*=success]").click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[value='submit']").click()

        desired_message = "Success"
        assert desired_message in self.driver.find_element(By.CSS_SELECTOR, "div[class*=alert]").text
