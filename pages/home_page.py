from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    def get_demo_text(self):
        locator = (By.XPATH, "//div[@class='message global demo']//p")
        return self.browser.text(locator)

    def fill_search_bar(self, term, submit=True):
        locator = (By.XPATH, "//input[@id='search']")
        self.browser.do_clear(locator)
        self.browser.do_send_keys(locator, term)
        if submit:
            self.browser.do_submit(locator)
        else:
            self.browser.do_click(locator)

    def get_product_text(self):
        locator = (By.XPATH, "//a[@class='product-item-link']")
        return self.browser.get_text_list(locator)

    def get_search_message_notice(self):
        locator = (By.XPATH, "//div[@class='message notice']/div")
        return self.browser.text(locator)

    def get_autosuggestion_terms(self):
        locator = (By.XPATH, "//div[@id='search_autocomplete']//li")
        return self.browser.text(locator)