import pytest

from PageObjects.AuthPage import AuthPage
from PageObjects.SettingsPage import SettingsPage
from PageObjects.MainMenu import MainMenu
from tests.test_gallery import LOGIN, PASSWORD

import time


@pytest.fixture(scope='session')
def con_obj(driver):
    auth = AuthPage(driver)
    menu = MainMenu(driver)
    auth.auth_suing_logo_pass(LOGIN, PASSWORD)
    menu.switch('more')
    return SettingsPage(driver)


class TestSettings:

    def test_first(self, con_obj):
        con_obj.scroll()


