from playwright.sync_api import Page 
from playwright.sync_api import expect 

class CheckoutPage:

    def __init__(self,page:Page):
        self.page = page 
        self.checkout_button = page.locator("[data-test='checkout']")
        self.firstname_form = page.get_by_placeholder("First Name")
        self.lastname_form = page.get_by_placeholder("Last Name")
        self.zipcode_form = page.get_by_placeholder("Zip/Postal Code")
        self.continue_btn = page.get_by_role('button',name="continue")

    def click_checkout_button(self):
        self.checkout_button.click()

    def open_checkout_stepone(self):
        self.page.goto("https://www.saucedemo.com/checkout-step-one.html")

    
        
    def after_click_checkout(self,firstname,lastname,zipcode):
        self.firstname_form.fill(firstname)
        self.lastname_form.fill(lastname)
        self.zipcode_form.fill(zipcode)
        expect(self.continue_btn).to_be_visible()
        self.continue_btn.click()






