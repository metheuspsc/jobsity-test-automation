import contextlib
import time
from urllib.parse import unquote

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Browser:
    """High level adapter for WebDriver"""

    def __init__(self, driver):
        self.driver = driver

    def __getattr__(self, item):
        return getattr(self.driver, item)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def do_click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()

    def do_submit(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        ).submit()

    def do_send_keys(self, locator, text):
        for char in text:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            ).send_keys(char)
            time.sleep(0.2)
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element_value(locator, text)
        )

    def do_clear(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        ).clear()

    def click_and_wait_redirect(self, locator):
        self.do_submit(locator)
        WebDriverWait(self.driver, 5).until(
            lambda driver: len(driver.window_handles) > 1
        )
        return Tab(self)

    def text(self, locator):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def get_element_list(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def get_text_list(self, locator):
        elements = self.get_element_list(locator)
        return [element.text for element in elements]

    def get_href(self, locator):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        href = element.get_attribute("href")
        return unquote(href)

    def wait_for_url_redirect(self, current_url, timeout=5):
        """Waits for url to redirect after performing an action

        Args:
            current_url: current url the page is on.
            timeout: wait time for page to redirect.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: driver.current_url != current_url)

    def wait_for_complete(self, timeout=30):
        """Waits until page completes loading"""
        with contextlib.suppress(TimeoutException):
            wait_driver = WebDriverWait(self.driver, timeout)
            return wait_driver.until(
                lambda driver: driver.execute_script("return document.readyState") == "complete")

class Tab(Browser):

    def current_tab_index(self):
        cur = self.driver.current_window_handle
        return self.driver.window_handles.index(cur)

    def next_window(self, idx):
        return self.driver.window_handles[idx + 1]

    def previous_window(self, idx):
        return self.driver.window_handles[idx - 1]

    def __enter__(self):
        idx = self.current_tab_index()
        self.driver.switch_to_window(self.next_window(idx))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        idx = self.current_tab_index()
        self.driver.close()
        self.driver.switch_to_window(self.previous_window(idx))
