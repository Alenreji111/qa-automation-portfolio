import requests
import pytest
from pages.login_page import LoginPage
from pages.inventory_item import InventoryItem
from pages.inventory_details import InventoryDetails
from pages.toggle_menu import ToggleMenu
from pages.checkout_page import CheckoutPage


@pytest.fixture
def login_page(page:Page):
    return LoginPage(page)

@pytest.fixture
def product_add_to_cart(page:Page):
    return InventoryItem(page)

@pytest.fixture
def logged_user(page , login_page):
    login_page.open()
    login_page.login("standard_user","secret_sauce")
    return page

@pytest.fixture
def product_added_to_cart(page,product_add_to_cart):
    product_add_to_cart.click_add_to_cart()
    product_add_to_cart.checking_product_in_add_to_cart()
    product_add_to_cart.open()
    product_add_to_cart.verify_product_in_cart()
    return page

@pytest.fixture 
def checkout_product_page(page,product_add_to_cart):
    product_add_to_cart.click_add_to_cart()
    product_add_to_cart.checking_product_in_add_to_cart()
    product_add_to_cart.open()
    return page
@pytest.fixture
def inventory_item_details(page):
    return InventoryDetails(page)

@pytest.fixture
def toggle_menu(page):
    return ToggleMenu(page)

@pytest.fixture
def dynamic_catalog(page,toggle_menu):
    toggle_menu.open_menu()
    toggle_menu.open_dynamic_catalog()
    return page
@pytest.fixture 
def checkout_page(page):
    return CheckoutPage(page)





