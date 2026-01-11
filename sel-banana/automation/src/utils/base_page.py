import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasePage: 
    #every page's parent - god parent of all UI interactions. 

    def __init__(self, driver): 
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def find_element(self,locator): 
        #find one element and then wait for it
        try: 
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f'Found element: {locator}')
            return element
        except TimeoutException: 
            self.logger.error(f'element not found: {locator}')
            raise 

    def click(self, locator): 
            #click the fricking element
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
            time.sleep(1)

            element.click()
            self.logger.info(f'clicked: {locator}')

    def type_text(self, locator, text): 
        #typing to the least
        element = self.find_element(locator)
        element.clear()
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        for char in text: 
            if char != '_':
                actions.send_keys(char)
                actions.pause(0.05)
        
        actions.perform()

        self.logger.info(f'typed into {locator}: {text[:20]}....')

    def get_text(self, locator): 
        #extract text. for assertions
        element = self.find_element(locator)
        return element.text

    def take_screenshot(self, name): 
        #basically backup logs
        filename = f'reports/screenshot_{name}.png'
        self.driver.save_screenshot(filename)
        self.logger.info(f'screenshot saved: {filename}')
        return filename

    def wait_for_alert(self): 
        #wait for popups
        self.wait.until(EC.alert_is_present())
        return self.driver.switch_to.alert


        
