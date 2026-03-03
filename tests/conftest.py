# This file is used by pytest to automatically use the page objects we created
# All the page opbects can be decalred here and  used for different testcases
import pytest
from pages.home_page import HomePage

@pytest.fixture
def home_page_login(page):
    # This 'page' argument is built-in Playwright fixture
    return HomePage(page)