import time

from pages.change_password_page import ChangePasswordPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
import pytest

from utilities.test_data import TestData


@pytest.mark.usefixtures('initialize_driver')
class TestChangePassword(BaseTest):

    def test_changing_password(self, initialize_driver):
        driver = initialize_driver
        login_page = LoginPage(driver)
        change_password_page = ChangePasswordPage(driver)
        # login into the account
        my_account = login_page.log_into_application(
            TestData.email, TestData.password)
        time.sleep(1)
        # click on the right menu on the password button
        my_account.click_right_menu_page("Password")
        time.sleep(1)
        # tru to change the password with non-identical passwords
        change_password_page.change_password('lalala','blabla')
        time.sleep(1)
        expected_error_message = "Password confirmation does not match password!"
        actual = change_password_page.get_confirmation_error_message()
        assert actual == expected_error_message
