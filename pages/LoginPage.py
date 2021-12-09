from coreComponents.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')
        self.username_field = driver.find_element(By.ID, 'user-name')
        self.password_field = driver.find_element(By.ID, 'password')
        self.submit_btn = driver.find_element(By.ID, 'login-button')

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.submit_btn.click()
        time.sleep(2)
