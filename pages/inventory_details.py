from playwright.sync_api import Page
from playwright.sync_api import expect

class InventoryDetails:

    def __init__(self,page:Page):
        self.page = page
        self.item_detail = page.locator("[data-test='item-4-title-link']")
        self.select_element = page.locator("[data-test='product-sort-container']")
        self.all_products = page.locator("[data-test='inventory-item']")
        self.product_price = page.locator("[data-test='inventory-item-price']")
        
        
        


    def open(self):
        self.page.goto("https://www.saucedemo.com/inventory-item.html?id=4")

    def inventory_detail_of_item(self):
        self.item_detail.click()
        expect(self.item_detail).to_be_visible()

    def sorting_items_za(self):
        self.select_element.select_option(value="za")
        return self.all_products.all_text_contents()

    def sorting_items_lohi(self):
        self.select_element.select_option(value="lohi")
        return self.product_price.all_text_contents()

        

    def sorting_items_hilo(self):
        self.select_element.select_option(value="hilo")
        return self.product_price.all_text_contents()

    
    def sorting_items_az(self):
        self.select_element.select_option(value="az")
        return self.all_products.all_text_contents()

    




    



        
    