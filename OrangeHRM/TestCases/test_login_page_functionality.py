from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.LoginPage import LoginPage
from PageObjects.Dashboard import Dashboard
from selenium.webdriver.support import expected_conditions as EC
import pytest

class Test_Login_page_fun:
    username = "Admin"
    password = "admin123"

    @pytest.fixture
    def test_verify_title(self):
        LoginPage.set_username(self.username)
        LoginPage.set_password(self.password)
        LoginPage.click_on_login()

        self.driver.find_element(Dashboard.btn_dropdown_xpath)
        my_obj = WebDriverWait(self.driver, 20)

        if my_obj.until(EC.presence_of_element_located(Dashboard.btn_dropdown_xpath)):
            if :
