from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_item import InventoryItem
from test.conftest import login_page,product_add_to_cart,logged_user,product_added_to_cart



def test_valid_user(page,login_page):
    login_page.open()
    login_page.login("standard_user","secret_sauce")
    assert page.url != "https://www.saucedemo.com/"
   

def test_invalid_user(page,login_page):
    login_page.open()
    login_page.invalid_login("testuser","password")
    login_page.verify_wrong_username()
    assert page.url == "https://www.saucedemo.com/"

def test_empty_username(page,login_page):
    login_page.open()
    login_page.invalid_login("","secret_sauce")
    login_page.verify_empty_username_validation()
    page.locator("[data-test='error']").screenshot(
        path="artifacts/withoutusername.png"
    )
    assert page.url =="https://www.saucedemo.com/"

def test_empty_password(page,login_page):
    login_page.open()
    login_page.invalid_login("standard_user","")
    login_page.verify_empty_password_validation()
    page.screenshot(
        path="artifacts/nopassword.png",
        full_page=True
    )
    assert page.url =="https://www.saucedemo.com/"


def test_empty_both_input(page,login_page):
    login_page.open()
    login_page.invalid_login("","")
    login_page.verify_empty_username_validation()
    assert page.url == "https://www.saucedemo.com/"

def test_addtocard_product(page,logged_user,product_add_to_cart):
    product_add_to_cart.click_add_to_cart()
    product_add_to_cart.verify_product_remove()

def test_changeofbutton(page,logged_user,product_add_to_cart):
    product_add_to_cart.click_add_to_cart()
    page.screenshot(
        path="artifacts/changeofremovebtn.png",
        full_page=True
    )
    product_add_to_cart.verify_product_remove()
    
    product_add_to_cart.clicks_to_remove_btn()
    product_add_to_cart.verify_product_add_to_cart()
    page.screenshot(
        path="artifacts/changeofbutton.png",
        full_page=True
    )

def test_product_cart(page,logged_user,product_added_to_cart):
    assert page.url == "https://www.saucedemo.com/cart.html"
    page.screenshot(
        path ="artifacts/chechingproductcart.png",
        full_page=True
    )

def test_get_item_detail(page,logged_user,inventory_item_details):
    inventory_item_details.inventory_detail_of_item()
    inventory_item_details.open()
    page.screenshot(
        path="artifacts/itemdetailpage.png",
        full_page=True
    )


    






    

    





 
    



    