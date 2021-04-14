from PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By

GALLERY_ADD_BUTTON_ID = "ru.mts.twomem:id/emptyAction"
GALLERY_ADD_FROM_DEVICE_BTN = "//*[@text='Загрузить из устройства']"
GALLERY_CREATE_ALBUM_BTN = "//*[@text='Создать альбом']"
GALLERY_NAME_INPUT = "ru.mts.twomem:id/textinput_placeholder"
GALLERY_NAME_INPUT_BTN = "//*[@text='Создать']" # "//*[contains(@text,'Создать')]"
ALERT_MESSAGE_ID = "ru.mts.twomem:id/title"
ALBUM_TITLE_ID = "ru.mts.twomem:id/titleCurtain"
ARROW_UP_BTN_ID = "ru.mts.twomem:id/arrow"
FOLDER_MENU_BTN_ID = "ru.mts.twomem:id/curtainFirstAction"
FOLDER_MENU_DEL_BTN_X = "//*[@text='Удалить альбом']"
POP_ACCEPT_BTN_ID = "ru.mts.twomem:id/positiveButton"
POP_ACCEPT_BTN_2_ID = "com.android.packageinstaller:id/permission_allow_button"

ADD_IMAGE_FROM_DEVICE_X = "//*[@text='Из галереи устройства']"
IMAGE_PREVIEW_X = "//*[@resource-id='ru.mts.twomem:id/preview']"
IMAGE_PREVIEW_CHECKBOX_X = "//*[@resource-id='ru.mts.twomem:id/checkbox']"
UPLOAD_BUTTON_ID = "ru.mts.twomem:id/result"
IMAGE_PREVIEW_ID = "ru.mts.twomem:id/preview"
UPLOADED_TITLE_ID = "ru.mts.twomem:id/title"

# image menu
SHARE_BTN_ID = "ru.mts.twomem:id/share"
DOWNLOAD_BTN_ID = "ru.mts.twomem:id/download"
DELETE_BTN_ID = "ru.mts.twomem:id/delete"
MORT_BTN_ID = "ru.mts.twomem:id/more"
DELETE_FROM_GAL_BTN_X = "//*[@text='Удалить из альбома']"
DELETE_TO_TRASH_BTN_X = "//*[@text='Переместить в корзину']"


class GalleryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def try_add_photo_without_album(self):
        self.find_element((By.ID, GALLERY_ADD_BUTTON_ID), time=15).click()
        self.find_element((By.XPATH, GALLERY_ADD_FROM_DEVICE_BTN), time=15).click()
        self.accept_alert()
        return self.find_element((By.ID, ALERT_MESSAGE_ID), time=15)

    def create_album(self, album_name):
        self.find_element((By.ID, GALLERY_ADD_BUTTON_ID), time=15).click()
        self.find_element((By.XPATH, GALLERY_CREATE_ALBUM_BTN), time=15).click()
        self.find_element((By.ID, GALLERY_NAME_INPUT), time=15).send_keys(album_name)
        self.add_allure_scr(GALLERY_NAME_INPUT, 2)
        self.find_element((By.XPATH, GALLERY_NAME_INPUT_BTN), time=25).click()
        self.find_element((By.ID, ALBUM_TITLE_ID), time=15)

    def open_album(self, album_name):
        self.find_element((By.ID, ARROW_UP_BTN_ID), time=15).click()
        self.add_allure_scr(ARROW_UP_BTN_ID, 2)
        self.find_element((By.XPATH, f"//*[@text='{album_name}']/.."), time=25).click()
        self.find_element((By.ID, GALLERY_ADD_BUTTON_ID), time=15)

    def delete_album(self, album_name):
        self.find_element((By.ID, FOLDER_MENU_BTN_ID), time=15).click()
        self.add_allure_scr(FOLDER_MENU_BTN_ID, 2)
        self.find_element((By.XPATH, FOLDER_MENU_DEL_BTN_X), time=25).click()
        self.find_element((By.ID, POP_ACCEPT_BTN_ID), time=15).click()
        self.assert_element_disappear((By.XPATH, f"//*[@text='{album_name}']/.."), time=15)
        # self.find_element((By.ID, GALLERY_ADD_BUTTON_ID), time=15).click()

    def add_image(self, album_name):
        self.find_element((By.ID, GALLERY_ADD_BUTTON_ID), time=15).click()
        self.find_element((By.XPATH, ADD_IMAGE_FROM_DEVICE_X), time=15).click()
        self.find_element((By.ID, POP_ACCEPT_BTN_2_ID), time=20).click()
        self.find_element((By.XPATH, f"//*[@text='{album_name}']/.."), time=15).click()
        self.find_element((By.XPATH, IMAGE_PREVIEW_X), time=15).click()
        self.add_allure_scr(IMAGE_PREVIEW_X, 2)
        check = self.find_element((By.XPATH, IMAGE_PREVIEW_CHECKBOX_X), time=25)
        assert check.get_attribute("checked")
        self.find_element((By.ID, UPLOAD_BUTTON_ID), time=15).click()
        self.find_element((By.ID, IMAGE_PREVIEW_ID), time=15)
        return self.find_element((By.ID, UPLOADED_TITLE_ID), time=15)

    def delete_image(self):
        self.find_element((By.ID, IMAGE_PREVIEW_ID), time=15).click()
        self.find_element((By.ID, DELETE_BTN_ID), time=25).click()
        self.add_allure_scr(IMAGE_PREVIEW_ID, 2)
        self.find_element((By.XPATH, DELETE_TO_TRASH_BTN_X), time=15).click()
        self.assert_element_disappear((By.ID, IMAGE_PREVIEW_ID), time=15)
