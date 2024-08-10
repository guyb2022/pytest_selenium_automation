from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    email_address_field = (By.XPATH, "//div[@class='form-group']//input[@id='input-email']")
    # Another option: (By.ID, "input-email")
    password_field = (By.XPATH, "//div[@class='form-group']//input[@id='input-password']")
    # Another option: (By.ID, "input-password")
    login_button = (By.XPATH, "//div[@id='content']//input[@value='Login']")
    warning_messages = (By.CSS_SELECTOR, '#account-login .alert-danger')
    # Another option: (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")