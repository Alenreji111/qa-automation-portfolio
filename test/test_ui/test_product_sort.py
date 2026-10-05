from playwright.sync_api import Page
# from pages.inventory_details import InventoryDetails
from test.conftest import logged_user,inventory_item_details

def test_sorting_inventory_za(page,logged_user,inventory_item_details):
    actual_result=inventory_item_details.sorting_items_za()
    
    assert actual_result == sorted(actual_result,reverse=True)

def test_sorting_inventory_lohi(page,logged_user,inventory_item_details):
    prices = inventory_item_details.sorting_items_lohi()
    prices = [float(price.replace("$",""))for price in prices]
    assert prices == sorted(prices)

def test_sorting_inventory_hilo(page,logged_user,inventory_item_details):
    prices = inventory_item_details.sorting_items_hilo()
    prices = [float(price.replace("$",""))for price in prices]
    assert prices == sorted(prices,reverse=True)

def test_sorting_inventory_az(page,logged_user,inventory_item_details):
    actual_result=inventory_item_details.sorting_items_az()
    assert actual_result == sorted(actual_result)