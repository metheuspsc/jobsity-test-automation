import time
from random import choice

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    def choose_color(self):
        locator = (By.XPATH, f"//div[@attribute-code='color']//div[@class='swatch-option color']")
        color = choice(self.browser.get_element_list(locator))
        color.click()

    def choose_size(self):
        locator = (By.XPATH, f"//div[@attribute-code='size']//div[@class='swatch-option text']")
        size = choice(self.browser.get_element_list(locator))
        size.click()

    def add_to_cart(self, product_url):
        self.load(product_url)
        self.choose_size()
        self.choose_color()
        locator = (By.XPATH, "//button[@title='Add to Cart']")
        self.browser.do_submit(locator)
        self.browser.wait_for_element((By.XPATH, "//span[@class='counter qty']"))

    def remove_from_cart(self):
        locator = (By.XPATH, "//a[@class='action action-delete']")
        self.browser.do_click(locator)

    def click_checkout(self):
        locator = (By.XPATH, "//button[@data-role='proceed-to-checkout']")
        time.sleep(3)
        self.browser.do_click(locator)

    def verify_checkout_form(self):
        locator = (By.XPATH, "//div[@class='checkout-container']")
        return self.browser.wait_for_element(locator)

    def verify_cart_empty(self):
        locator = (By.XPATH, "//*[@class='cart-empty']")
        return self.browser.text(locator)

    def fill_search_bar(self, term, submit=True):
        locator = (By.XPATH, "//input[@id='search']")
        self.browser.do_send_keys(locator, term)
        if submit:
            self.browser.do_submit(locator)
        else:
            self.browser.do_click(locator)

    def get_product_text(self):
        locator = (By.XPATH, "//a[@class='product-item-link']")
        return self.browser.text(locator)

    def check_product_cart_count(self, count):
        locator = (By.XPATH, "//tbody[@class='cart item']")
        cart_items = self.browser.get_element_list(locator)
        return len(cart_items) == count
