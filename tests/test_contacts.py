import pytest

from PageObjects.AuthPage import AuthPage
from PageObjects.ContactsPage import ContactsPage
from PageObjects.MainMenu import MainMenu
from tests.test_gallery import LOGIN, PASSWORD


@pytest.fixture(scope='session')
def con_obj(driver):
    auth = AuthPage(driver)
    menu = MainMenu(driver)
    auth.auth_suing_logo_pass(LOGIN, PASSWORD)
    menu.switch('contacts')
    return ContactsPage(driver)


class TestContacts:

    def test_create_back(self, con_obj):
        con_obj.create_back_of_contacts()

    def test_swipe_till_contact(self, con_obj):
        con_obj.swipe_till_contact('Vivek Rana')

    def test_find_contact_by_name(self, con_obj):
        con_obj.find_by_name('Bansal Nancy')

    def test_delete_contacts(self, con_obj):
        con_obj.delete_contacts()


    # con.create_back_of_contacts()
    #
    # con.swipe_till_contact()
    # con.find_by_name()
    #
    # con.delete_contacts()
