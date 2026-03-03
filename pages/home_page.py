from pages.base_page import BasePage
from playwright.sync_api import expect
import time
import logging
import re

class HomePage(BasePage):
    # Locators
    LINK = '(//*[contains(text(),"username and password")])[1]'
    USERNAME = 'xpath=//*[@id="LoginForm-Username"]'
    PASSWORD = 'xpath=//*[@id="LoginForm-Password"]'
    LOGIN_BUTTON = 'xpath=//*[@id="blackpearlLogin"]/span'
    USER = 'xpath=//*[contains(text(),"Welcome {}")]'
    USER_EMAIL = 'xpath=//*[@id="ui-member-email"]'
    USER_EMAIL_NAME = 'xpath=(//*[contains(text(),"{}")])[1]'

    def login(self, username, password):
        self.page.screenshot(path="Link.png")
        self.click(self.LINK)
        logging.info("Username and password link is visible")

        expect(self.page.locator(self.USERNAME)).to_be_visible()
        expect(self.page.locator(self.PASSWORD)).to_be_visible()
        expect(self.page.locator(self.LOGIN_BUTTON)).to_be_visible()
        logging.info("Username, password fields and Login button is visible")

        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        time.sleep(5)   # Sleep time given for page to load after login
        self.page.screenshot(path="Login.png")
        expect(self.page,message="The Login was not successful!").to_have_url(re.compile(r".*/dashboard"))
        

    def check_dashboard(self,user,email):
        name = self.USER.format(user)
        expect(self.page.locator(name),"Name is not visible").to_be_visible()
        logging.info(f"Name {user} is visible in the logged in page")

        expect(self.page.locator(self.USER_EMAIL)).to_be_visible()
        expect(self.page.locator(self.USER_EMAIL_NAME.format(email)),"Email is not present").to_be_visible()
        logging.info(f"Email {email} is visible in the logged in page")