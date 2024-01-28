# Jobsity Test Automation Challenge

> This is a automated test script for Jobsity SDET position challenge. 
> using selenium and pytest.

## ✅ Challenge Requirements.
- [URL to test](https://magento.softwaretestingboard.com/)
- [Test Plan Spreadsheet](https://docs.google.com/spreadsheets/d/1qxXeYSfXi6RsiJUkqcy7StnE6gOIIGfwwxKqUP1BpqQ/edit?usp=sharing)
- [Bug Trello Board](https://trello.com/b/JPC86pNE/jobsity-bugs)

### Required tests:
    
- Orders and Returns Form:
  - [x] TC6.1: Verify accessibility of the Orders and Returns form from the footer.
  - [x] TC6.2: Test submitting the form with valid order information.
  - [x] TC6.3: Test submitting the form with invalid order information.
  - [x] TC6.4: Verify error handling for incomplete form submissions.

### Extra Tests:
- Layout Cross-Browser Compatibility:
  - [ ] TC1.1: Verify layout compatibility on Internet Explorer 11.
  - [X] TC1.2: Verify layout compatibility on Google Chrome (latest version).
  - [X] TC1.3: Verify layout compatibility on Mozilla Firefox (latest version).
  - [ ] TC1.4: Verify layout compatibility on Safari (latest version). 

- Search Functionality:
  - [X] TC2.1: Verify that the search bar is present and functional.
  - [X] TC2.2: Test searching with valid keywords displays correct products.
  - [X] TC2.3: Test searching with invalid keywords shows no results.
  - [X] TC2.4: Test auto-suggestions functionality during typing in the search bar.

- Add to Cart Flow:
  - [X]  TC3.1: Verify adding a product to the cart from the product listing.
  - [X]  TC3.2: Verify cart updates correctly when multiple products are added.
  - [X]  TC3.3: Test removing items from the cart.

- Account Creation and Login:
  - [ ]  TC4.1: Test creating a new user account.
  - [ ]  TC4.2: Verify login functionality with valid credentials.
  - [ ]  TC4.3: Verify login fails with invalid credentials.
  - [ ]  TC4.4: Test password reset functionality.

- Payment Form:
  - [ ]  TC5.1: Verify all required fields are present in the payment form.
  - [ ]  TC5.2: Test payment form with valid credit card details.
  - [ ]  TC5.3: Test payment form with invalid credit card details.
  - [ ]  TC5.4: Verify error handling for incomplete form submissions.



## ✨ Assumptions and comments
>>#### Orders and Returns:
>>* I assumed this form is only for unlogged customers, since it returns the same data as the "My Orders" section under "My Account" 


>### Classes and Fixtures:
>>#### TestData:
>>* SimpleNamespace containing the test data, could be easily replaced by a factory to implement multiple scenarios.
>>#### Browser:
>>* This class is a high level adapter for common browser methods.
>>#### HomePage, ProductPage, RefundPage:
>>* Class for higher level test interactions with the pages. 
>>* The locators are inside the methods to simplify maintenance since there's no repetition on locators.
>### Tests:
>>#### Browser Compatibility:
>>* Tests run in Chrome and Firefox, Safari and IE could be added later since the browser setup is extandable.



## 💻 Get Started

Before starting you need the following dependencies:
* Install `Python 3` latest version 
* Have Chrome and Firefox installed

## 🚀 Setup

```
./venv/scripts/activate
pip install -r requirements.txt
pytest -n auto --reruns 2 --rerun-except AssertionError --reruns-delay 2
```
