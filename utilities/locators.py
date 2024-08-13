from selenium.webdriver.common.by import By


class ChangePasswordLocatorFields:
    password_field = (By.ID, "input-password")
    confirm_password_field = (By.ID, "input-confirm")
    continue_button = (By.XPATH, "//input[@value='Continue']")
    confirmation_error_message = (By.CSS_SELECTOR, '#content .text-danger')
    # Another option: (By.XPATH, "//div[@class='text-danger']")
