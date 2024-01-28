import pytest

from pages.orders_returns_page import OrdersReturnsPage


@pytest.fixture(scope="function")
def orders_returns_page(browser, test_data):
    with OrdersReturnsPage(browser, test_data.HOME_URL) as orders_returns_page:
        yield orders_returns_page


def test_orders_returns_valid_data(orders_returns_page, test_data):
    """
    This test case verifies the functionality of the Orders and Returns form when submitted with valid order data.

    The test performs the following steps:
    1. Navigates to the Orders and Returns form through the footer link.
    2. Fills the form with valid order ID, customer last name, and email from the test data.
    3. Submits the form and checks if the submission is successful.

    Args:
        orders_returns_page (Page Object): The Page Object representing the Orders and Returns page.
        test_data (TestData Object): An object containing test data like valid order ID, customer last name, and email.

    Asserts:
        That the submission of the form with valid data is successful, which is verified by a specific method in the Orders and Returns page object.
    """
    orders_returns_page.click_orders_returns_footer_link()
    orders_returns_page.fill_order_id(test_data.VALID_ORDER_ID)
    orders_returns_page.fill_last_name(test_data.TEST_CUSTOMER_LAST_NAME)
    orders_returns_page.fill_email(test_data.TEST_CUSTOMER_EMAIL)
    orders_returns_page.click_continue()
    assert orders_returns_page.verify_orders_returns(test_data)


def test_orders_returns_invalid_data(orders_returns_page, test_data):
    """
    This test case verifies the functionality of the Orders and Returns form when submitted with invalid order data.

    The test performs the following steps:
    1. Navigates to the Orders and Returns form through the footer link.
    2. Fills the form with invalid order ID and valid last name and email from the test data.
    3. Submits the form and checks for an error message.

    Args:
        orders_returns_page (Page Object): The Page Object representing the Orders and Returns page.
        test_data (TestData Object): An object containing test data like invalid order ID, customer last name, and email.

    Asserts:
        The presence of a specific alert text in the error message returned by the Orders and Returns page, verifying the form's error handling capability when receiving invalid order data.
    """
    orders_returns_page.click_orders_returns_footer_link()
    orders_returns_page.fill_order_id(test_data.INVALID_ORDER_ID)
    orders_returns_page.fill_last_name(test_data.TEST_CUSTOMER_LAST_NAME)
    orders_returns_page.fill_email(test_data.TEST_CUSTOMER_EMAIL)
    orders_returns_page.click_continue()
    assert test_data.ORDERS_RETURNS_FORM_ALERT_TEXT in orders_returns_page.get_orders_error_alert()
