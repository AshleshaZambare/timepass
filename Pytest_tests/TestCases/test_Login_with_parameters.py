import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Test_Login_with_parameters:
    def test_login(self, setup, getDataForLogin):
        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(getDataForLogin[0])
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(getDataForLogin[1])
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login TestCase is Passed")
            self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_pass.PNG")
            self.driver.close()

            assert True
        except:
            print("Login TestCase is Failed")
            self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_fail.PNG")
            self.driver.close()
            assert False


