from test.conftest import logged_user,checkout_page,checkout_product_page
from playwright.sync_api import Page

def test_checkout_button(page,logged_user,checkout_product_page,checkout_page):
    checkout_page.click_checkout_button()
    assert page.url == "https://www.saucedemo.com/checkout-step-one.html"

