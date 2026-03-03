from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    LINK = 'xpath=//*[@id="switch-up"]'
    USERNAME = 'xpath=//*[@id="LoginForm-Username"]'
    PASSWORD = 'xpath=//*[@id="LoginForm-Password"]'
    LOGIN_BUTTON = 'xpath=//*[@id="blackpearlLogin"]/span'

    def login(self, username, password):
        self.click(self.LINK)
        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)