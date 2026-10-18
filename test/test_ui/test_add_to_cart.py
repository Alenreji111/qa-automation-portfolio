from playwright.sync_api import Page 
from playwright.sync_api import expect
import pytest 


@pytest.mark.regression
def test_addtocard_product(page,logged_user,product_add_to_cart):
    product_add_to_cart.click_add_to_cart()
    product_add_to_cart.verify_product_remove()

@pytest.mark.smoke
@pytest.mark.regression
def test_changeofbutton(page,logged_user,product_add_to_cart):
    
    product_add_to_cart.click_add_to_cart()
    page.screenshot(
        path="artifacts/changeofremovebtn.png",
        full_page=True
    )
    product_add_to_cart.verify_product_remove()
    
    product_add_to_cart.clicks_to_remove_btn()
    # product_add_to_cart.verify_product_add_to_cart()
    page.screenshot(
        path="artifacts/changeofbutton.png",
        full_page=True
    )


