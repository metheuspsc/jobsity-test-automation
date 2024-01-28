import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrdersReturnsPage(BasePage):

    def click_orders_returns_footer_link(self):
        locator = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/sales/guest/form/']")
        self.browser.do_click(locator)

    def click_continue(self):
        continue_button_locator = (By.XPATH, "//button[@class='action submit primary']")
        self.browser.do_submit(continue_button_locator)

    def fill_order_id(self, order_id):
        order_id_input_locator = (By.XPATH, "//input[@id='oar-order-id']")
        self.browser.do_send_keys(order_id_input_locator, order_id)

    def fill_last_name(self, last_name):
        last_name_input_locator = (By.XPATH, "//input[@id='oar-billing-lastname']")
        self.browser.do_send_keys(last_name_input_locator, last_name)

    def fill_email(self, email):
        email_input_locator = (By.XPATH, "//input[@id='oar_email']")
        self.browser.do_send_keys(email_input_locator, email)

    def verify_orders_returns(self, test_data):
        time.sleep(3)
        order_id_locator = (By.XPATH, "//h1[@class='page-title']")
        order_id_text = self.browser.text(order_id_locator)
        return test_data.VALID_ORDER_ID in order_id_text

    def get_orders_error_alert(self):
        time.sleep(3)
        alert_locator = (By.XPATH, "//div[@role='alert']")
        return self.browser.text(alert_locator)
