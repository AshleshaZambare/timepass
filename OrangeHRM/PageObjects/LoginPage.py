import selenium
from selenium.webdriver.common.by import By


class LoginPage():
    textbox_username_xpath = (By.XPATH, "//input[@name = 'username']")
    textbox_password_xpath = (By.XPATH, "//input[@name = 'password']")
    btn_login_xpath = (By.XPATH, "//button[@type = 'submit']")


    def __init__(self, setup):
        self.driver = setup

    def set_username(self, username):
        self.driver.find_element(self.textbox_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(self.textbox_password_xpath).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(self.btn_login_xpath).click()







