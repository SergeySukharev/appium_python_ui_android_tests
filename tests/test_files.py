from PageObjects.AuthPage import AuthPage
from PageObjects.FilesPage import FilesPage
from PageObjects.MainMenu import MainMenu
from tests.test_gallery import LOGIN, PASSWORD

file_name = '5a2992e221a221440d7adc341a552693_fitted_960x600.jpg'
folder_name = 'panasenkov_photo'


def test_auth(driver):
    auth = AuthPage(driver)
    auth.auth_suing_logo_pass(LOGIN, PASSWORD)
    menu = MainMenu(driver)
    menu.switch('files')
    files = FilesPage(driver)
    name = files.create_folder('lol')
    assert name == 'lol'
    files.add_media()
    files.delete_from_context_menu()
    menu.switch('files')
    files.delete_from_context_menu()


def test_add_media(driver):
    auth = AuthPage(driver)
    auth.auth_suing_logo_pass(LOGIN, PASSWORD)
    menu = MainMenu(driver)
    menu.switch('files')
    files = FilesPage(driver)
    files.add_media()
    files.delete_from_context_menu()


def test_add_file(driver):
    auth = AuthPage(driver)
    auth.auth_suing_logo_pass(LOGIN, PASSWORD)
    menu = MainMenu(driver)
    menu.switch('files')
    files = FilesPage(driver)
    f_name = files.add_file(file_name)
    assert f_name == file_name
    files.delete_from_context_menu()


def test_add_file_photo_to_folder(driver):
    auth = AuthPage(driver)
    auth.auth_suing_logo_pass(LOGIN, PASSWORD)

    menu = MainMenu(driver)
    menu.switch('files')

    files = FilesPage(driver)
    name = files.create_folder(folder_name)
    assert name == folder_name
    f_name = files.add_file(file_name)
    assert f_name == file_name
    files.add_media()

    files.switch_file_type('photo')
    files.delete_by_name(file_name)
    files.delete_from_context_menu()
    files.back()
    files.delete_from_context_menu()
