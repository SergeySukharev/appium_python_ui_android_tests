import selenium
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from PageObjects.BaseApp import BasePage

ACCEPT_BTN_ID = 'com.android.packageinstaller:id/permission_allow_button'
UPLOAD_BUTTON_ID = "ru.mts.twomem:id/enter"
UPLOAD_BUTTON_2_ID = 'ru.mts.twomem:id/emptyAction'
SUCESS_BAGE_X = "//*[@text='Загрузка завершена']"

LEFT_MENU_BTN_ID = 'ru.mts.twomem:id/curtainLeftMenuContent'
LEFT_MENU_REFRESH_BTN_X = "//*[@resource-id='ru.mts.twomem:id/title'][@text='Обновить копию']"
LEFT_MENU_DOWNLOAD_TO_DEVICE_BTN_X = "//*[@resource-id='ru.mts.twomem:id/title'][@text='Скачать контакты на устройство']"
LEFT_MENU_DELETE_BTN_X = "//*[@resource-id='ru.mts.twomem:id/title'][@text='Удалить копию']"
ACCEPT_DELETE_BTN_ID = 'ru.mts.twomem:id/positiveButton'

SEARCH_BTN_ID = 'ru.mts.twomem:id/curtainRightMenuContent'
SEARCH_BAR_ID = 'ru.mts.twomem:id/searchEditText'
SEARCH_CANCEL_BTN_ID = 'ru.mts.twomem:id/cancelSearch'

SEARCH_RESULT_X = "//*[@resource-id='ru.mts.twomem:id/itemContainer'][@text='Память устройства']"

"""Contacts menu"""
TITLE_ID = 'ru.mts.twomem:id/contactName'


def create_xpath_from_name(contact_name):
    return f"//*[@resource-id='ru.mts.twomem:id/contactName'][@text='{contact_name}']"


class ContactsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def create_back_of_contacts(self):
        try:
            self.find_element((By.ID, UPLOAD_BUTTON_ID), time=3).click()
        except selenium.common.exceptions.TimeoutException:
            self.find_element((By.ID, UPLOAD_BUTTON_2_ID), time=3).click()

        self.find_element((By.ID, ACCEPT_BTN_ID), time=15).click()
        # self.find_element((By.ID, UPLOAD_BUTTON_ID), time=15).click()
        self.find_element((By.XPATH, SUCESS_BAGE_X), time=15)

    def delete_contacts(self):
        self.find_element((By.ID, LEFT_MENU_BTN_ID), time=15).click()
        self.find_element((By.XPATH, LEFT_MENU_DELETE_BTN_X), time=15).click()
        self.find_element((By.ID, ACCEPT_DELETE_BTN_ID), time=15).click()

    def find_by_name(self, contact_name):
        self.find_element((By.ID, SEARCH_BTN_ID), time=15).click()
        self.find_element((By.ID, SEARCH_BAR_ID), time=15).send_keys(contact_name)
        self.find_element((By.XPATH, create_xpath_from_name(contact_name))
                          , time=15)
        self.find_element((By.ID, SEARCH_CANCEL_BTN_ID), time=15).click()

    def swipe_till_contact(self, contact_name):
        counter = 100
        size = self.driver.get_window_size()
        x = int(size['width'] / 2)
        start_y = int(size['height'] * 0.6)
        end_y = int(size['height'] * 0.2)
        actions = TouchAction(self.driver)
        while counter != 0:
            counter -= 1
            actions.press(x=x, y=start_y)
            actions.wait(150)
            actions.move_to(x=x, y=end_y)
            actions.release()
            actions.perform()
            footer = self.driver.find_elements_by_xpath(create_xpath_from_name(contact_name))
            if footer:
                break
