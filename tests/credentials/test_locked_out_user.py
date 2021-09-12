import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.credentials.LoginPage import LoginPage
from utilities.datareader.test_reader import get_locked_out_credentials


class TestLockedOutUser:
    driver: WebDriver
    login_page: LoginPage

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_locked_out_user(self, credentials):
        self.login_page.go_to_index()
        self.login_page.login(credentials.get("username"), credentials.get("password"))
        assert self.login_page.error_message_is_displayed

    def init_pages(self):
        self.login_page = LoginPage(self.driver)

    @pytest.fixture(params=get_locked_out_credentials())
    def credentials(self, request):
        return request.param
