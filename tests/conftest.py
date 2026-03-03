# This file is used by pytest to automatically use the page objects we created
import pytest
from pages.login_page import HomePage

@pytest.fixture
def home_page_login(page):
    # This 'page' argument is built-in Playwright fixture
    return HomePage(page)