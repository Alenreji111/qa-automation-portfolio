from playwright.sync_api import Page 
from playwright.sync_api import expect

class ToggleMenu:
    def __init__(self,page:Page):
        self.page = page
        self.menu_button = page.get_by_role("button" , name="Open Menu")
        self.all_item_menu = page.locator("[data-test='inventory-sidebar-link']")
        self.all_product_visible = page.locator("[data-test='inventory-item']")
        self.logout_menu = page.locator("[data-test='logout-sidebar-link']")
        self.dynamic_catalogs = page.locator("[data-test='dynamic-catalog-sidebar-link']")
        self.lazy_load = page.locator("[data-test='dynamic-catalog-lazy-load-link']")
        self.spinner = page.locator("[data-test='dynamic-catalog-spinner-link']")
        self.slider_catalog = page.locator("[data-test='dynamic-catalog-slider-link']")
        self.lazy_load_container = page.locator("[data-test='dynamic-catalog-lazy-load-container']")
        self.spinner_container = page.locator("[data-test='dynamic-catalog-spinner-grid']")
        self.slider_container = page.locator("[data-test='dynamic-catalog-slider-container']")

    def open_menu(self):
        self.menu_button.click()

    def click_all_item_menu(self):
        self.all_item_menu.click()
        self.all_product_visible.all_text_contents()
        # expect(self.all_product_visible).to_be_visible()

    def checking_logout(self):
        self.logout_menu.click()

    def open_dynamic_catalog(self):
        self.dynamic_catalogs.click()

    def checking_lazy_load_catolog(self):
        self.lazy_load.click()
        self.lazy_load_container.all_text_contents()
        expect(self.lazy_load_container).to_be_visible()

    def checking_spinner_catalog(self):
        self.spinner.click()
        self.spinner_container.all_text_contents()
        expect(self.spinner_container).to_be_visible()

    def checking_slider_catalog(self):
        self.slider_catalog.click()
        self.slider_container.all_text_contents()
        expect(self.slider_container).to_be_visible()


        
        
        

    
    