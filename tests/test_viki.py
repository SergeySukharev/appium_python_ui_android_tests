from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By

# INPUT_ID = 'org.wikipedia:id/search_container'
RESULT = "//*[contains(@text,'Java')]"
SEARCH_INIT_ELEMENT = "//*[contains(@text,'Search Wikipedia')]"
SEARCH_INPUT = "//*[contains(@text,'Search…')]"
FOOTER_ID = 'org.wikipedia:id/page_external_link'


class VikiPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def another_find_by_text(self, text):

        pass

    def find_element_by_text(self, text):
        return self.find_element((By.XPATH, f"//*[@text='{text}']/.."), time=15)

    def find_things(self):
        self.find_element((By.XPATH, SEARCH_INIT_ELEMENT), time=15).click()
        self.find_element((By.XPATH, SEARCH_INPUT), time=15).send_keys("Java")
        # self.find_element((By.CLASS_NAME, RESULT), time=15).click()
        self.find_element_by_text('Java (programming language)').click()

    def swipe_till_elem(self):
        counter = 100
        size = self.driver.get_window_size()
        x = int(size['width'] / 2)
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)
        actions = TouchAction(self.driver)
        while counter != 0:
            counter -= 1
            actions.press(x=x, y=start_y)
            actions.wait(150)
            actions.move_to(x=x, y=end_y)
            actions.release()
            actions.perform()
            footer = self.driver.find_elements_by_id(FOOTER_ID)
            if footer:
                break


def wait_for_element_present(driver, by, locator: str, timeout=15):
    wait = WebDriverWait(driver, timeout)
    return wait.until(
        EC.presence_of_element_located(
            (by, locator)
        )
    )


def test_viki(driver):
    auth = VikiPage(driver)
    auth.find_things()
    auth.swipe_till_elem()
