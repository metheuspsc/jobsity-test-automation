from types import SimpleNamespace

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.browser import Browser


@pytest.fixture(scope="session")
def test_data():
    return SimpleNamespace(
        HOME_URL="https://magento.softwaretestingboard.com/",
        TEST_SEARCH_URL="https://magento.softwaretestingboard.com/catalogsearch/result/?q=Breathe",
        TEST_PRODUCT_1="https://magento.softwaretestingboard.com/radiant-tee.html",
        TEST_PRODUCT_2="https://magento.softwaretestingboard.com/iris-workout-top.html",
        TEST_PRODUCT_3="https://magento.softwaretestingboard.com/karissa-v-neck-tee.html",
        CART_PAGE="https://magento.softwaretestingboard.com/checkout/cart/",
        VALID_ORDER_ID="000042185",
        INVALID_ORDER_ID="XXXXXXXXX",
        TEST_CUSTOMER_LAST_NAME="Corrêa",
        TEST_CUSTOMER_EMAIL="matheuspessoax@gmail.com",
        ORDERS_RETURNS_FORM_ALERT_TEXT="You entered incorrect data. Please try again.",
    )


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def browser(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox(options=options)
    return Browser(web_driver)
