import pytest

from pages.home_page import HomePage


@pytest.fixture(scope="function")
def home_page(browser, test_data):
    with HomePage(browser, test_data.HOME_URL) as home_page:
        yield home_page


@pytest.mark.parametrize("term", (["Backpack", "Hoodie", "Breathe"]))
def test_search_bar_valid_term(home_page, test_data, term):
    """
    Tests the search bar functionality with valid search terms.

    This method performs the following steps:
    1. Captures the current URL for later comparison.
    2. Fills the search bar with a valid term and submits the search.
    3. Waits for the URL to redirect from the current URL.
    4. Retrieves and asserts that all search results contain the search term.

    Args:
        home_page (Page Object): The page object representing the home page.
        test_data (TestData Object): Contains test data and URLs.
        term (str): A valid search term for the test.

    Asserts:
        All search results are relevant to the term, indicating correct search functionality.
    """
    current_url = home_page.browser.current_url
    home_page.fill_search_bar(term=term)
    home_page.browser.wait_for_url_redirect(current_url=current_url)
    results = home_page.get_product_text()
    assert all([term in result for result in
                results]), f"Search returned unrelated items: {[result for result in results if term not in result]}"


def test_search_bar_invalid_term(home_page, test_data):
    """
    Tests the search bar functionality with an invalid search term.

    Steps include:
    1. Fills the search bar with an invalid term.
    2. Waits for the URL to redirect to the home page URL.
    3. Retrieves and asserts the no results message from the search.

    Args:
        home_page (Page Object): Represents the home page.
        test_data (TestData Object): Contains URLs and other test-related data.

    Asserts:
        The displayed message matches the expected 'no results' text.
    """
    home_page.fill_search_bar(term="ajhfioeaqh")
    home_page.browser.wait_for_url_redirect(current_url=test_data.HOME_URL)
    result = home_page.get_search_message_notice()
    assert result == "Your search returned no results."


def test_autosuggestion(home_page, test_data):
    """
    Verifies the autosuggestion feature of the search bar.

    The method follows these steps:
    1. Enters a valid term in the search bar without submitting.
    2. Retrieves autosuggestion terms.
    3. Asserts that the entered term is present in the autosuggestions.

    Args:
        home_page (Page Object): The home page object.
        test_data (TestData Object): Contains test data.

    Asserts:
        The entered term appears in the autosuggestions, indicating the autosuggestion feature is functional.
    """
    home_page.fill_search_bar(term="Breathe", submit=False)
    autosuggestion_terms = home_page.get_autosuggestion_terms()
    assert "Breathe" in autosuggestion_terms
