from test.conftest import logged_user,checkout_page,checkout_product_page
from playwright.sync_api import Page
from playwright.sync_api import expect

def test_checkout_button(page,logged_user,checkout_product_page,checkout_page):
    checkout_page.click_checkout_button()
    assert page.url == "https://www.saucedemo.com/checkout-step-one.html"



def test_steps_of_checkout(page:Page,logged_user,checkout_product_page,checkout_page):
    checkout_page.click_checkout_button()
    checkout_page.open_checkout_stepone()
    checkout_page.after_click_checkout("alen","reji","abcdefg")
    assert page.url == "https://www.saucedemo.com/checkout-step-two.html"
    



