from PageObjects.AuthPage import AuthPage
from PageObjects.OptPage import OptPage
from PageObjects.MainMenu import MainMenu
from tests.test_gallery import LOGIN, PASSWORD


def test_first(driver):
    auth = AuthPage(driver)
    auth.auth_suing_logo_pass(LOGIN, PASSWORD)
    menu = MainMenu(driver)
    menu.switch('opt')
    opt = OptPage(driver)
    opt.accept_system()
    opt.bages()
