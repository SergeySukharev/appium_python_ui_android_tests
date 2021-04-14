import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def driver(request):
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

