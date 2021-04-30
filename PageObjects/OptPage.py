from selenium.webdriver.common.by import By
import time

from PageObjects.BaseApp import BasePage

ACCEPT_BTN_ID = 'com.android.packageinstaller:id/permission_allow_button'
DENY_BTN_ID = 'com.android.packageinstaller:id/permission_deny_button'

MEMORY_BAGE_X = "//*[@resource-id='ru.mts.twomem:id/diagramTitle'][@text='Память устройства']"
SIZE_BAGE_X = "//*[@resource-id='ru.mts.twomem:id/diagramTitle'][@text='Объём облака']"
BUCKET_VIDGET_ID = 'ru.mts.twomem:id/incBucketContainer'

CURTAIN_ID = 'ru.mts.twomem:id/screenContainer'


class OptPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def accept_system(self):
        self.find_element((By.ID, ACCEPT_BTN_ID), time=15).click()
        # self.find_element((By.ID, CURTAIN_ID), time=15).click()

    def bages(self):
        time.sleep(10)
        self.find_element((By.XPATH, MEMORY_BAGE_X), time=15).click()
        time.sleep(10)
        self.find_element((By.XPATH, SIZE_BAGE_X), time=15).click()
        time.sleep(10)
        self.find_element((By.ID, BUCKET_VIDGET_ID), time=15).click()
        time.sleep(10)


