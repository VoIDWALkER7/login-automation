from selenium.webdriver.common.by import By
from src.utils.base_page import BasePage

class LoginPage(BasePage): 
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="submit-login"]')
    ERROR_MESSAGE = (By.ID, "flash")

    def __init__(self, driver): 
        super().__init__(driver)
        self.logger.info('LoginPage initialized')

    def login(self, username, password):
        '''The main flow'''
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.logger.info(f'Login attempt: {username}')

    def get_error_message(self): 
        '''for failed job'''
        return self.get_text(self.ERROR_MESSAGE)

