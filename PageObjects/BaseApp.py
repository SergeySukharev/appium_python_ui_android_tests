from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from supp import screen_name
import allure
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def assert_element_disappear(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    @staticmethod
    def send_data(obj, keys):
        obj.click()
        obj.clear()
        obj.send_keys(keys)

    def tap_by_coord(self, x, y):
        TouchAction(self.driver).tap(x=x, y=y).perform()

    def accept_alert(self):
        # 	com.android.packageinstaller:id/do_not_ask_checkbox
        self.find_element((By.ID, "com.android.packageinstaller:id/permission_allow_button"), time=15).click()

    def add_allure_scr(self, name, sleep):
        time.sleep(sleep)
        allure.attach(self.driver.get_screenshot_as_png(), name=screen_name(name),
                      attachment_type=AttachmentType.PNG)

    def swipe_till_elem(self,By: By, elem_id: str) -> None:
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
            footer = self.find_elements((By, elem_id), time=15)
            if footer:
                break

