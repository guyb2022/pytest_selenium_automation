from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
import pytest
from utilities.custom_logger import LogGen


@pytest.mark.usefixtures('initialize_driver')
class TestLogin(BaseTest):
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_credentials(self, initialize_driver):
        self.logger.info("#" * 10 + " Starting test_valid_credentials " + "#" * 10)
        driver = initialize_driver
        login_page = LoginPage(driver)
        login_page.log_into_application(
            TestData.email, TestData.password)
        actual_title = login_page.get_title()
        driver.save_screenshot(".\\screenshots\\test_valid_credentials.png")
        assert actual_title == "My Account"
        self.logger.info("#" * 10 + " Ended test_valid_credentials " + "#" * 10)

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip
    def test_invalid_credentials(self, initialize_driver):
        self.logger.info("#" * 10 + " Starting test_invalid_credentials " + "#" * 10)
        driver = initialize_driver
        login_page = LoginPage(driver)
        login_page.log_into_application(
            "Invalid Email", "Invalid Password")
        actual_message = login_page.get_warning_message()
        driver.save_screenshot(".\\screenshots\\test_invalid_credentials.png")
        assert actual_message.__contains__("Warning")
        self.logger.info("#" * 10 + " Ended test_invalid_credentials " + "#" * 10)
