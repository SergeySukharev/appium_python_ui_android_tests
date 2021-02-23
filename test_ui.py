import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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


@pytest.mark.parametrize("word", ['java', ])
def test_search(set_up, word):
    set_up.find_element_by_id('org.wikipedia:id/search_container').send_keys(word)
    set_up.implicitly_wait(5)
    search_res = set_up.find_elements_by_id('org.wikipedia:id/page_list_item_title')
    for i in search_res:
        assert word in i.get_attribute('text').lower()


@pytest.mark.swipe
@pytest.mark.parametrize("word", ['java', ])
def test_swipe_article(set_up, word):
    set_up.find_element_by_id('org.wikipedia:id/search_container').send_keys(word)
    set_up.implicitly_wait(5)
    search_res = set_up.find_elements_by_id('org.wikipedia:id/page_list_item_title')
    for i in search_res:
        if i.text == "Java (programming language)":
            i.click()
    set_up.implicitly_wait(10)
    actions = TouchAction(set_up)
    size = set_up.get_window_size()
    x = int(size['width'] / 2)
    start_y = int(size['height'] * 0.8)
    end_y = int(size['height'] * 0.2)
    print(size, x, start_y, end_y)
    actions.press(x=x, y=start_y)
    actions.move_to(x=x, y=end_y)
    actions.release()
    actions.perform()
