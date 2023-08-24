import selenium
from selenium.webdriver.common.by import By

class Dashboard:
    btn_dropdown_xpath = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    link_logout_linktext = (By.LINK_TEXT, "Logout")

    def __int__(self, setup):
        self.driver = setup

    def click_on_logout(self):
        self.driver.find_element(self.btn_dropdown_xpath).click()
        self.driver.find_element(self.link_logout_linktext).click()



