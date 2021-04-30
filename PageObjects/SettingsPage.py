from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from PageObjects.BaseApp import BasePage

PHONE_BTN_ID = 'ru.mts.twomem:id/phone'
ALL_APPS_BTN_ID = 'ru.mts.twomem:id/allApps'
TARIF_IND_BTN_ID = 'ru.mts.twomem:id/tariffIndicator'

HIGH_RATING_BTN_ID = 'ru.mts.twomem:id/highRating'
LOW_RATING_BTN_ID = 'ru.mts.twomem:id/lowRating'

DEBUG_BTN_ID = 'ru.mts.twomem:id/debug'

TEXT = ['Поделиться приложением', 'О приложении', 'Поддержка', 'Возможности приложения', 'Настройки']


class SettingsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll(self):
        self.driver.execute_script("mobile: scroll", {"direction": "down"})


    def swipe_down(self):
        actions = TouchAction(self.driver)
        actions.press(x=720,y=1920)
        actions.wait(100)
        actions.move_to(x=720, y=820)
        actions.release()
        actions.perform()
        self.find_element((By.ID, DEBUG_BTN_ID),time=15)



