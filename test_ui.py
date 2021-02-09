import pytest
import time
from appium import webdriver


@pytest.fixture(scope='session')
def set_up(request):
    des_cap = {
        "platformName": "Android",
        "deviceName": "AndroidTestDevice",
        "platformVervion": "8.0",
        "appPackage": "ru.mts.twomem",
        "appActivity": "ru.mts.twomem.app.AppActivity"
    }

    def tear_down():
        webdriver.Remote('http://localhost:4723/wd/hub', des_cap).quit()

    request.addfinalizer(tear_down)
    return webdriver.Remote('http://localhost:4723/wd/hub', des_cap)


def test_input(set_up):
    set_up.find_element_by_id("ru.mts.twomem:id/enter").click()
    time.sleep(5)
    set_up.find_element_by_id('phoneInput').send_keys('9250073358')
    set_up.find_element_by_id('submit').click()
    time.sleep(5)
    assert set_up.find_element_by_xpath('//android.webkit.WebView[@content-desc="Введите код из SMS"]'
                                        '/android.view.View/android.view.View[1]/android.view.View[4]/'
                                        'android.view.View/android.view.View/android.widget.EditText')
