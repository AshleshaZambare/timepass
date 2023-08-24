import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Test_Login:
    def test_login_page_title(self, setup):
        self.driver = setup
        self.driver.get("https://automation.credence.in")

        if self.driver.title == "CredKart":
            self.driver.save_screenshot("Screenshots\\" + "page_title.PNG")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("Screenshots\\" + "page_title.PNG")
            self.driver.close()
            assert False


    def test_login(self, setup):
        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
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


