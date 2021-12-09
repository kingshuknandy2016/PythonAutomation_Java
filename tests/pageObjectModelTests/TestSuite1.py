from coreComponents.BaseTest import BaseTest
from pages.LoginPage import LoginPage


class TestSuite1(BaseTest):

    def test_login_valid(self):
        self.objectLogin = LoginPage(self.driver)
        self.objectLogin.login('standard_user','secret_sauce')