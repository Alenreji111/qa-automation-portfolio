from playwright.sync_api import Page
import pytest 


@pytest.mark.regression
def test_checkout_button(page,logged_user,checkout_product_page,checkout_page):
    checkout_page.click_checkout_button()
    assert page.url == "https://www.saucedemo.com/checkout-step-one.html"


@pytest.mark.smoke
@pytest.mark.regression
def test_steps_of_checkout(page,logged_user,checkout_product_page,checkout_page):
    checkout_page.click_checkout_button()
    checkout_page.open_checkout_steps()
    checkout_page.after_click_checkout("alen","reji","abcdefg")
    assert page.url == "https://www.saucedemo.com/checkout-step-two.html"



