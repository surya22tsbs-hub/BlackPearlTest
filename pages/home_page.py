from pages.base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    # Locators
    #LINK = 'xpath=//*[@id="switch-up"]'
    LINK = '(//*[contains(text(),"username and password")])[1]'
    USERNAME = 'xpath=//*[@id="LoginForm-Username"]'
    PASSWORD = 'xpath=//*[@id="LoginForm-Password"]'
    LOGIN_BUTTON = 'xpath=//*[@id="blackpearlLogin"]/span'
    USER = 'xpath=//*[contains(text(),"Welcome {}")]'
    USER_EMAIL = 'xpath=//*[@id="ui-member-email"]'
    USER_EMAIL_NAME = 'xpath=//*[contains(text(),"{}")]'

    def login(self, username, password):
        self.click(self.LINK)
        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def check_dashboard(self,user,email):
        name = self.USER.format(user)
        expect(self.page.locator(name)).to_be_visible()
        expect(self.page.locator(self.USER_EMAIL)).to_be_visible()
        email = self.USER.format(email)
        expect(self.page.locator(email)).to_be_visible()