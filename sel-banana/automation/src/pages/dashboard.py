from selenium.webdriver.common.by import By
from src.utils.base_page import BasePage

class DashboardPage(BasePage): 
    WELCOME_MESSAGE = (By.ID, 'flash')
    PRODUCTS_TABLE = (By.ID, "logout")

    def __init__(self, driver): 
        super().__init__(driver)

    def get_welcome_text(self): 
        return self.get_text(self.WELCOME_MESSAGE)

    def logout(self): 
        self.click(self.LOGOUT_BUTTON)
        self.logger.info(" Logged out")
