import pytest
from appium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    des_cap = {
        "platformName": "Android",
        "deviceName": "ADV8",
        "platformVervion": "8.0",
        "appPackage": "ru.mts.twomem",
        "appActivity": "ru.mts.twomem.app.AppActivity",
        "app": "C:\\Users\\IDDQD\\Documents\\Python\\appium_python_ui_android_tests\\apks\\app-debug.apk"
        # "appPackage": "org.wikipedia",
        # "appActivity": "org.wikipedia.main.MainActivity"

    }

    def tear_down():
        webdriver.Remote('http://localhost:4723/wd/hub', des_cap).quit()

    request.addfinalizer(tear_down)
    return webdriver.Remote('http://localhost:4723/wd/hub', des_cap)
