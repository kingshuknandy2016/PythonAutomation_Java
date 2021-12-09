
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID,'password').send_keys('secret_sauce')
driver.find_element(By.ID,'login-button').click()
time.sleep(5)

driver.close()
driver.quit()

