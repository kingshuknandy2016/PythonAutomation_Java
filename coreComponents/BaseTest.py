from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class BaseTest(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        s = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
