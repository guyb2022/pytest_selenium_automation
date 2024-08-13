from selenium import webdriver

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
import pytest


@pytest.mark.usefixtures('initialize_driver')
class TestLogin(BaseTest):

    @pytest.mark.usefixtures('initialize_driver')
    def test_valid_credentials(self, initialize_driver):
        driver = initialize_driver
        login_page = LoginPage(driver)
        login_page.log_into_application(
            TestData.email, TestData.password)
        actual_title = login_page.get_title()
        assert actual_title == "My Account"

    @pytest.mark.usefixtures('initialize_driver')
    def test_invalid_credentials(self, initialize_driver):
        driver = initialize_driver
        login_page = LoginPage(driver)
        login_page.log_into_application(
            "Invalid Email", "Invalid Password")
        actual_message = login_page.get_warning_message()
        assert actual_message.__contains__("Warning")
