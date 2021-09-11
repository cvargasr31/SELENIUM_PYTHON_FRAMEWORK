import pytest

from pageobjects.credentials.LoginPage import LoginPage
from pageobjects.topmenu.TopMenuPage import TopMenuPage


@pytest.mark.regression
@pytest.mark.smoke
class TestLogout:
    login_page: LoginPage
    top_menu_page: TopMenuPage

    def test_logout(self):
        self.login_page.go_to_index()
        self.login_page.login("standard_user", "secret_sauce")

        self.top_menu_page.logout()

        assert self.login_page.verify_page_is_displayed() is True

    def init_pages(self):
        self.login_page = LoginPage(self.driver)
        self.top_menu_page = TopMenuPage(self.driver)