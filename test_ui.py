import pytest
from appium import webdriver


@pytest.fixture(scope='session')
def set_up(request):
    des_cap = {
        "platformName": "Android",
        "deviceName": "AndroidTestDevice",
        "platformVervion": "8.0",
        "appPackage": "org.wikipedia",
        "appActivity": "org.wikipedia.main.MainActivity"
    }

    def tear_down():
        webdriver.Remote('http://localhost:4723/wd/hub', des_cap).quit()

    request.addfinalizer(tear_down)
    return webdriver.Remote('http://localhost:4723/wd/hub', des_cap)


@pytest.mark.parametrize("text,elem", [("Search Wikipedia", "android.widget.TextView"), ])
def test_validate_text_of_element(set_up, text, elem):
    elem = set_up.find_element_by_class_name(elem)
    assert elem.text == text, f"Элемент {elem}, не содержит текст - {text}"
