import pytest
import allure
from PageObjects.AuthPage import AuthPage
from PageObjects.GalleryPage import GalleryPage

LOGIN = "9153821751"
PASSWORD = "Qwerty312"
ALBUM_NAME = "TestAlbum"
ALBUM_ON_DEVICE = "Download"


@allure.story('Проверка авторизации')
def test_auth(driver):
    auth = AuthPage(driver)
    auth.authUsingLogoPass(LOGIN, PASSWORD)


@allure.story("Создание альбома")
def test_create_open_delete_gallery(driver):
    auth = AuthPage(driver)
    auth.authUsingLogoPass(LOGIN, PASSWORD)
    gal = GalleryPage(driver)
    gal.create_album(ALBUM_NAME)
    gal.open_album(ALBUM_NAME)
    gal.delete_album(ALBUM_NAME)


@allure.story('Добавление изображения')
def test_add_file(driver):
    """Create album and add one photo to it"""
    """set_up"""
    auth = AuthPage(driver)
    auth.authUsingLogoPass(LOGIN, PASSWORD)
    gal = GalleryPage(driver)
    gal.create_album(ALBUM_NAME)
    gal.open_album(ALBUM_NAME)
    """test"""
    title = gal.add_image(ALBUM_ON_DEVICE)
    assert title.text == "Загрузка завершена"
    """tear_down"""
    gal.delete_image()
    gal.delete_album(ALBUM_NAME)
