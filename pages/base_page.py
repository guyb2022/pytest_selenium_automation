from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    """
    The purpose of a basepage is to contain methods common to all page objects

    """
    def __init__(self, driver):
        self.driver = driver

    def find(self,locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def click_menu_page(self, path, element_page_name):
        self.click(self.page(path, element_page_name))

    def page(self, path, page_element_name):
        return By.XPATH, path + page_element_name + "']"
