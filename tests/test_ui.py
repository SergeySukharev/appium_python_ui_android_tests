import pytest
import time









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
@pytest.mark.parametrize("word", ['java'])
def test_swipe_article(set_up, word):
    set_up.find_element_by_id('org.wikipedia:id/search_container').send_keys(word)

    element = wait_for_element_present(
        set_up,
        By.XPATH,
        '//*[@resource-id="org.wikipedia:id/page_list_item_title"][@text="Java (programming language)"]/..'
    )
    element.click()

    wait_for_element_present(
        set_up,
        By.ID,
        'org.wikipedia:id/view_page_title_text'
    )

    actions = TouchAction(set_up)

    size = set_up.get_window_size()
    x = int(size['width'] / 2)
    start_y = int(size['height'] * 0.8)
    end_y = int(size['height'] * 0.2)

    actions.press(x=x, y=start_y)
    actions.wait(200)
    actions.move_to(x=x, y=end_y)
    actions.release()
    actions.perform()

    time.sleep(15)


@pytest.mark.swipe_until
@pytest.mark.parametrize("word", ['java'])
def test_swipe_until_footer(set_up, word):
    set_up.find_element_by_id('org.wikipedia:id/search_container').send_keys(word)

    element = wait_for_element_present(
        set_up,
        By.XPATH,
        '//*[@resource-id="org.wikipedia:id/page_list_item_title"][@text="Java (programming language)"]/..'
    )
    element.click()

    wait_for_element_present(
        set_up,
        By.ID,
        'org.wikipedia:id/view_page_title_text'
    )

    footer = wait_for_element_present(set_up, By.XPATH, '//*[@resource-id="org.wikipedia:id/page_external_link"]'

                                                        '[@text="View page in browser"]/..')
    counter = 1000
    while footer or counter == 0:
        size = set_up.get_window_size()
        x = int(size['width'] / 2)
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)
        print(size, start_y, end_y)
        counter -= 1
        actions = TouchAction(set_up)
        actions.press(x=x, y=start_y)
        actions.wait(200)
        actions.move_to(x=x, y=0)
        actions.release()
        actions.perform()
