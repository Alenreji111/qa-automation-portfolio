from playwright.sync_api import Page
import pytest 

@pytest.mark.regression
def test_sorting_inventory_za(page,logged_user,inventory_item_details):
    actual_result=inventory_item_details.sorting_items_za()
    
    assert actual_result != sorted(actual_result,reverse=True)

@pytest.mark.regression
def test_sorting_inventory_lohi(page,logged_user,inventory_item_details):
    prices = inventory_item_details.sorting_items_lohi()
    prices = [float(price.replace("$",""))for price in prices]
    assert prices != sorted(prices)

@pytest.mark.regression
def test_sorting_inventory_hilo(page,logged_user,inventory_item_details):
    prices = inventory_item_details.sorting_items_hilo()
    prices = [float(price.replace("$",""))for price in prices]
    assert prices == sorted(prices,reverse=True)

@pytest.mark.regression
def test_sorting_inventory_az(page,logged_user,inventory_item_details):
    actual_result=inventory_item_details.sorting_items_az()
    assert actual_result == sorted(actual_result)