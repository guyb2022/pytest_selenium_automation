import time
import pytest
from selenium.common import exceptions

from pages.change_password_page import ChangePasswordPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
from utilities.custom_logger import LogGen


@pytest.mark.usefixtures('initialize_driver')
class TestChangePassword(BaseTest):
    logger = LogGen.loggen("TestChangePassword")

    @pytest.mark.regression
    def test_changing_password(self, initialize_driver):
        self.logger.debug("#" * 10 + " Starting test_changing_password" + "#" * 10)
        driver = initialize_driver
        login_page = LoginPage(driver)
        change_password_page = ChangePasswordPage(driver)
        # login into the account
        my_account = login_page.log_into_application(
            TestData.email, TestData.password)
        time.sleep(1)
        # click on the right menu on the password button
        try:
            my_account.click_right_menu_page("Password")
            driver.save_screenshot(".\\screenshots\\test_changing_password_login_phase.png")
        except:
            self.logger.info("Error while trying to click on Password right menu button")
            self.logger.exception(exceptions)
        finally:
            self.logger.debug("#" * 10 + " Ended Logging Phase test_changing_password " + "#" * 10)
            assert driver.title == "My Account"

        time.sleep(1)
        # try to change the password with non-identical passwords
        expected_error_message = "Password confirmation does not match password!"
        actual = ""
        try:
            change_password_page.change_password('passwordNo1', 'passwordNo2')
            actual = change_password_page.get_confirmation_error_message()
            driver.save_screenshot(".\\screenshots\\test_changing_password.png")
        except:
            self.logger.info("Error while trying to enter two non-Identical Passwords")
            self.logger.exception(exceptions)
        finally:
            self.logger.debug("#" * 10 + " Ended test_changing_password " + "#" * 10)
            assert actual == expected_error_message


