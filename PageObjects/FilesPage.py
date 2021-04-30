import selenium
from selenium.common.exceptions import NoSuchElementException

from PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By

from PageObjects.GalleryPage import IMAGE_PREVIEW_X, IMAGE_PREVIEW_CHECKBOX_X, UPLOAD_BUTTON_ID

ADD_BTN_ID = 'ru.mts.twomem:id/emptyAction'
ADD_SML_BTN_ID = 'ru.mts.twomem:id/curtainSecondAction'

OPEN_CERTAIN_BTN_ID = 'ru.mts.twomem:id/curtainFirstAction'

# TYPES_MENU
ALL = 'ru.mts.twomem:id/all'
DOC = 'ru.mts.twomem:id/documents'
PHOTO = 'ru.mts.twomem:id/photo'
VIDEO = 'ru.mts.twomem:id/video'
AUDIO = 'ru.mts.twomem:id/audio'
LINKS = 'ru.mts.twomem:id/links'
ARCHIVE = 'ru.mts.twomem:id/archive'
FOLDERS = 'ru.mts.twomem:id/folders'

#PHOTO_MENU
SHARE_BTN_ID = "ru.mts.twomem:id/share"
DOWNLOAD_BTN_ID = "ru.mts.twomem:id/download"
DELETE_BTN_ID = "ru.mts.twomem:id/delete"
MORT_BTN_ID = "ru.mts.twomem:id/more"


MEDIA_BTN_X = "//*[@resource-id='ru.mts.twomem:id/title'][@text='Медиа из галереи']"
FILE_BTN_X = "//*[@resource-id='ru.mts.twomem:id/title'][@text='Файл']"
FOLDER_BTN_X = "//*[@resource-id='ru.mts.twomem:id/title'][@text='Папку']"

GALLERY_CLS_BTN_X = '//android.widget.ImageButton[@content-desc="Navigate up"]'

GALLERY_NAME_INPUT = "ru.mts.twomem:id/textinput_placeholder"
CREATE_FOLDER_BTN_X = "//*[@text='Создать']"
FOLDER_TITLE_ID = 'ru.mts.twomem:id/titleCurtain'
MENU_BTN_ID = 'ru.mts.twomem:id/fileActions'
FOLDER_MENU_DEL_BTN_X = "//*[@text='Удалить']"

FOLDER_POPUP_ACCEPT_BTN_ID = 'ru.mts.twomem:id/positiveButton'
FOLDER_POPUP_CANCEL_BTN_ID = 'ru.mts.twomem:id/cancelButton'

ACCEPT_BTN_ID = 'com.android.packageinstaller:id/permission_allow_button'
DENY_BTN_ID = 'com.android.packageinstaller:id/permission_deny_button'

FOLDER_NAME_X_TMP = "//*[@text='']"

FILES_CLASS_NAMES = 'android.widget.LinearLayout'
FILES_TITLE_ID = 'android:id/title'
FILE_NAME_ID = 'ru.mts.twomem:id/fileName'

ARROW_BACK_BTN = 'ru.mts.twomem:id/homeIndicator'



# MENUS
MAIN_MENU_DIC = {
    'media': MEDIA_BTN_X,
    'file': FILE_BTN_X,
    'folder': FOLDER_BTN_X
}
FILE_TYPE_DIC = {
    'all': ALL,
    'doc': DOC,
    'photo': PHOTO,
    'video': VIDEO,
    'audio': AUDIO,
    'links': LINKS,
    'archive': ARCHIVE,
    'folders': FOLDERS
}


class FilesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def btn(self):
        self.find_element((By.ID, ADD_BTN_ID), time=15).click()

    def back(self):
        self.find_element((By.ID, ARROW_BACK_BTN), time=15).click()

    def switch(self, menu_id):
        self.find_element((By.ID, ADD_BTN_ID), time=15).click()
        self.find_element((By.XPATH, MAIN_MENU_DIC[menu_id]), time=15).click()

    def switch_small(self, menu_id):
        self.find_element((By.ID, ADD_SML_BTN_ID), time=15).click()
        self.find_element((By.XPATH, MAIN_MENU_DIC[menu_id]), time=15).click()

    def switch_file_type(self, menu_id):
        self.find_element((By.ID, FILE_TYPE_DIC[menu_id]), time=15).click()

    def create_folder(self, folder_name):
        self.main_menu()
        # self.find_element((By.ID, ADD_BTN_ID), time=15).click()
        self.find_element((By.XPATH, MAIN_MENU_DIC['folder']), time=15).click()
        self.find_element((By.ID, GALLERY_NAME_INPUT), time=15).send_keys(folder_name)
        self.find_element((By.XPATH, CREATE_FOLDER_BTN_X), time=15).click()
        return self.find_element((By.ID, FOLDER_TITLE_ID), time=15).get_attribute('text')

    def delete_from_context_menu(self):
        self.find_element((By.ID, MENU_BTN_ID), time=15).click()
        self.find_element((By.XPATH, FOLDER_MENU_DEL_BTN_X), time=15).click()
        self.find_element((By.ID, FOLDER_POPUP_ACCEPT_BTN_ID), time=15).click()

    def delete_by_name(self, file_name):
        self.find_element((By.XPATH, f"//*[@text='{file_name}']"), time=15).click()
        self.find_element((By.ID, DELETE_BTN_ID), time=15).click()
        self.find_element((By.ID, FOLDER_POPUP_ACCEPT_BTN_ID), time=15).click()
        self.assert_element_disappear((By.XPATH, f"//*[@text='{file_name}']"), time=15)

    def main_menu(self):
        try:
            self.find_element((By.ID, ADD_BTN_ID), time=3).click()
        except selenium.common.exceptions.TimeoutException:
            self.find_element((By.ID, ADD_SML_BTN_ID), time=3).click()

    def add_media(self):
        self.main_menu()
        # self.find_element((By.ID, ADD_BTN_ID), time=15).click()
        self.find_element((By.XPATH, MAIN_MENU_DIC['media']), time=15).click()
        self.find_element((By.ID, ACCEPT_BTN_ID), time=15).click()
        self.find_element((By.XPATH, "//*[@text='Все фото']"), time=15).click()
        self.find_element((By.XPATH, IMAGE_PREVIEW_X), time=15).click()
        check = self.find_element((By.XPATH, IMAGE_PREVIEW_CHECKBOX_X), time=25)
        assert check.get_attribute("checked")
        self.find_element((By.ID, UPLOAD_BUTTON_ID), time=15).click()

    def add_file(self, file_name):
        self.main_menu()
        # self.find_element((By.ID, ADD_BTN_ID), time=15).click()
        self.find_element((By.XPATH, MAIN_MENU_DIC['file']), time=15).click()
        self.find_element((By.XPATH, f"//*[@text='{file_name}']"), time=15).click()
        return self.find_element((By.ID, FILE_NAME_ID), time=15).get_attribute('text')
