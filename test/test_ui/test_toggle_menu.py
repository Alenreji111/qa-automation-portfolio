from playwright.sync_api import Page 
from playwright.sync_api import expect 
from test.conftest import toggle_menu,logged_user,dynamic_catalog


def test_all_item_menu(page,logged_user,toggle_menu):
    toggle_menu.open_menu()
    toggle_menu.click_all_item_menu()

def test_logout_button(page,logged_user,toggle_menu):
    toggle_menu.open_menu()
    toggle_menu.checking_logout()
    assert page.url == "https://www.saucedemo.com/"
    
def test_lazy_load_catalog(page,logged_user,toggle_menu,dynamic_catalog):
    toggle_menu.checking_lazy_load_catolog()

def test_spinner_catalog(page,logged_user,dynamic_catalog,toggle_menu):
    toggle_menu.checking_spinner_catalog()

def test_slider_catalog(page,logged_user,dynamic_catalog,toggle_menu):
    toggle_menu.checking_slider_catalog()


    
    


    