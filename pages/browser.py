from urllib.parse import unquote

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Browser:
    """High level adapter for WebDriver"""

    def __init__(self, driver):
        self.driver = driver

    def __getattr__(self, item):
        return getattr(self.driver, item)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator))

    def do_click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()

    def do_submit(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        ).submit()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element_value(locator, text)
        )

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

    def get_href(self, locator):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        href = element.get_attribute("href")
        return unquote(href)


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
