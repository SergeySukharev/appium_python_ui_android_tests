from PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By

ID_DIC = {
    'gallery': 'ru.mts.twomem:id/media',
    'contacts': 'ru.mts.twomem:id/contacts',
    'files': 'ru.mts.twomem:id/files',
    'opt': 'ru.mts.twomem:id/optimization',
    'more': 'ru.mts.twomem:id/more'
}


class MainMenu(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def switch(self, menu_id):
        self.find_element((By.ID, ID_DIC[menu_id]), time=15).click()
