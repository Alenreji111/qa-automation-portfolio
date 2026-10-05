from playwright.sync_api import Page 
from playwright.sync_api import expect 

class CheckoutPage:

    def __init__(self,page:Page):
        self.page = page 
        self.checkout_button = page.locator("[data-test='checkout']")

    def click_checkout_button(self):
        self.checkout_button.click()




