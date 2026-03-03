from playwright.sync_api import Page
from playwright.sync_api import expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, path: str):
        self.page.goto(path)

    def click(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible()
        self.page.locator(selector).click()

    def input_text(self, selector: str, text: str):
        expect(self.page.locator(selector)).to_be_visible()
        self.page.locator(selector).fill(text)