from PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By


AUTH_ENTER_BUTTON_ID = "ru.mts.twomem:id/enter"
AUTH_PHONE_INPUT_ID = "phoneInput"
AUTH_LOGIN_SUBMIT_BTN_ID = "submit"
AUTH_PASSWORD_INPUT_ID = "password"
ACCEPT_BTN_X = '//android.widget.Button[@content-desc="Подтвердить "]'
AUTH_TARIFF_SCREEN_CLS_BTN_ID = "ru.mts.twomem:id/tariffNext"
AUTH_CLOSE_STORIES_BTN_ID = "ru.mts.twomem:id/close"


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def authUsingLogoPass(self, login, password):
        self.find_element((By.ID, AUTH_ENTER_BUTTON_ID), time=15).click()
        self.find_element((By.ID, AUTH_PHONE_INPUT_ID), time=15).send_keys(login)
        self.find_element((By.ID, AUTH_LOGIN_SUBMIT_BTN_ID), time=15).click()
        self.find_element((By.ID, AUTH_PASSWORD_INPUT_ID), time=15).send_keys(password)
        self.tap_by_coord(206, 845)
        self.find_element((By.XPATH, ACCEPT_BTN_X), time=15).click()
        self.find_element((By.ID, AUTH_TARIFF_SCREEN_CLS_BTN_ID), time=15).click()
        self.find_element((By.ID, AUTH_CLOSE_STORIES_BTN_ID), time=15).click()

