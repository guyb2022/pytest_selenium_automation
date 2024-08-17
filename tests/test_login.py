from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
import pytest
from utilities.custom_logger import LogGen
from selenium.common import exceptions


@pytest.mark.usefixtures('initialize_driver')
class TestLogin(BaseTest):
    logger = LogGen.loggen("TestLogin")

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip
    def test_valid_credentials(self, initialize_driver):
        self.logger.info("#" * 10 + " Starting test_valid_credentials " + "#" * 10)
        driver = initialize_driver
        login_page = LoginPage(driver)
        actual_title = driver.title
        try:
            login_page.log_into_application(TestData.email, TestData.password)
            actual_title = login_page.get_title()
            driver.save_screenshot(".\\screenshots\\test_valid_credentials.png")
        except:
            self.logger.warning("Error while trying to login")
            self.logger.exception(exceptions)
        finally:
            self.logger.info("#" * 10 + " Ended test_valid_credentials " + "#" * 10)
            assert actual_title == "My Account"

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip
    def test_invalid_credentials(self, initialize_driver):
        self.logger.info("#" * 10 + " Starting test_invalid_credentials " + "#" * 10)
        driver = initialize_driver
        login_page = LoginPage(driver)
        actual_message = ""
        try:
            login_page.log_into_application("Invalid Email", "Invalid Password")
            actual_message = login_page.get_warning_message()
            driver.save_screenshot(".\\screenshots\\test_invalid_credentials.png")
        except:
            self.logger.warning("Error while trying to change Non-Identical passwords")
            self.logger.exception(exceptions)
        finally:
            self.logger.info("#" * 10 + " Ended test_invalid_credentials " + "#" * 10)
            assert actual_message == "Warning: No match for E-Mail Address and/or Password."




