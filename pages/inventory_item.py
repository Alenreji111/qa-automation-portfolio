from playwright.sync_api import Page
from playwright.sync_api import expect

class InventoryItem:

    def __init__(self,page:Page):
        self.page = page
        self.bagpack_item = page.locator("[data-test='inventory-item']").filter(
            has_text = "Sauce Labs Backpack"
        )
        self.product_add_to_cart =self.bagpack_item.get_by_role("button",name='Add to cart')
        self.product_remove = self.bagpack_item.get_by_role("button",name='Remove')
        self.cart_button = page.locator("[data-test='shopping-cart-link']")
       
        

    def click_add_to_cart(self):
        self.product_add_to_cart.click()

    def verify_product_remove(self):
        expect(self.product_remove).to_be_visible()

    def clicks_to_remove_btn(self):
        self.product_remove.click()

    def verify_product_add_to_cart(self):
        expect(self.product_add_to_cart).to_be_visible()

    def open(self):
        self.page.goto("https://www.saucedemo.com/cart.html")


    def checking_product_in_add_to_cart(self):
        self.cart_button.click()
        # expect(self.bagpack_item).to_be_visible()

    def verify_product_in_cart(self):
        expect(self.bagpack_item).to_be_visible()

        


    