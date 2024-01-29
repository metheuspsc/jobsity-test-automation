import pytest

from pages.product_page import ProductPage

def test_add_single_product(browser, test_data):
    """
    Adds a single product to the shopping cart and verifies if the cart contains only this item.

    This method performs the following actions:
    1. Adds a specified product (TEST_PRODUCT_1) to the cart.
    2. Loads the cart page.
    3. Asserts that the number of products in the cart is exactly one.

    Args:
        product_page (Page Object): The page object representing the product page.
        test_data (TestData Object): An object containing test data including product information and URLs.

    Asserts:
        The cart contains exactly one item, ensuring the add to cart functionality works for a single product.
    """
    with ProductPage(browser, test_data.HOME_URL) as product_page:
        product_page.add_to_cart(test_data.TEST_PRODUCT_1)
        product_page.load(test_data.CART_PAGE)
        assert product_page.check_product_cart_count(1), "Cart does not have a single item."


def test_add_multiple_products(browser, test_data):
    """
    Adds multiple products to the shopping cart and checks if the correct number of items are present.

    Steps include:
    1. Adding three different products (TEST_PRODUCT_1, TEST_PRODUCT_2, TEST_PRODUCT_3) to the cart.
    2. Navigating to the cart page.
    3. Asserting that the cart contains exactly three items.

    Args:
        product_page (Page Object): The page object for product interactions.
        test_data (TestData Object): Contains data for various test products and cart page URL.

    Asserts:
        The cart contains three items, verifying the add to cart functionality for multiple products.
    """
    with ProductPage(browser, test_data.HOME_URL) as product_page:
        product_page.add_to_cart(test_data.TEST_PRODUCT_1)
        product_page.add_to_cart(test_data.TEST_PRODUCT_2)
        product_page.add_to_cart(test_data.TEST_PRODUCT_3)
        product_page.load(test_data.CART_PAGE)
        assert product_page.check_product_cart_count(3), "Cart does not have a 3 itens."


def test_remove_product(browser, test_data):
    """
    Tests the functionality of removing a product from the shopping cart.

    The method follows these steps:
    1. Adds a product (TEST_PRODUCT_1) to the cart.
    2. Loads the cart page.
    3. Removes the product from the cart.
    4. Asserts that the cart is empty after removal.

    Args:
        product_page (Page Object): Page object for handling product interactions.
        test_data (TestData Object): Contains product data and cart page information.

    Asserts:
        The shopping cart is empty after removing the product, ensuring the remove functionality works correctly.
    """
    with ProductPage(browser, test_data.HOME_URL) as product_page:
        product_page.add_to_cart(test_data.TEST_PRODUCT_1)
        product_page.load(test_data.CART_PAGE)
        product_page.remove_from_cart()
        assert product_page.verify_cart_empty(), "Cart not empty."


def test_checkout_redirection(browser, test_data):
    """
    Verifies the redirection to the checkout form after adding a product to the cart.

    The steps include:
    1. Adding a product (TEST_PRODUCT_1) to the cart.
    2. Navigating to the cart page.
    3. Initiating the checkout process.
    4. Asserting the presence of the checkout form.

    Args:
        product_page (Page Object): The page object representing the product page.
        test_data (TestData Object): Contains test data including product and checkout form information.

    Asserts:
        The checkout form is present, confirming successful redirection to the checkout page.
    """
    with ProductPage(browser, test_data.HOME_URL) as product_page:
        product_page.add_to_cart(test_data.TEST_PRODUCT_1)
        product_page.load(test_data.CART_PAGE)
        product_page.click_checkout()
        assert product_page.verify_checkout_form(), "No checkout form."