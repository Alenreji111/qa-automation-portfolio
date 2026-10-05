from playwright.sync_api import Page
from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page:Page):

        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button=page.get_by_role("button",name="Login")
        self.wrong_username_msg = page.get_by_text("Epic sadface: Username and password do not match any user in this service")
        self.empty_username_msg = page.get_by_text("Epic sadface: Username is required")
        self.empty_password_msg = page.get_by_text("Epic sadface: Password is required")
        

    def open(self):
        self.page.goto("https://www.saucedemo.com/")
    
    def login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def invalid_login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify_empty_username_validation(self):
        expect(self.empty_username_msg).to_be_visible()

    def verify_empty_password_validation(self):
        expect(self.empty_password_msg).to_be_visible()

    def verify_wrong_username(self):
        expect(self.wrong_username_msg).to_be_visible()
        



        
        


  
    