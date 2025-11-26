from utils.funciones import URL, USERNAME, PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login:
    
    _USER_NAME = (By.NAME, "user-name")
    _USER_PASSWORD = (By.NAME,"password")
    BUTTOM = (By.ID,"login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(URL)

    def user(self, username, password):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._USER_NAME)).send_keys(username)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self._USER_PASSWORD)).send_keys(password)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.BUTTOM)).click()