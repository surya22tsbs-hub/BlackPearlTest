import json
import pytest

def load_data():
    with open("data/login.json") as f:
        return json.load(f)

#Testcases

#1. Load the login page.
def test_login(home_page_login):
    data = load_data()
    home_page_login.navigate_to(data["url"])

#2. Interact with the interface to change to the username/password version of the login page.
#3. Input the username and password into their corresponding fields.
#4. Click the login button to proceed to the logged-in state.
def test_load_login(home_page_login):
    data = load_data()
    home_page_login.navigate_to(data["url"])
    home_page_login.login(data["username"], data["password"])  #Replace with the user credentials from login.json file

#5. Check that there is a loaded user number on the dashboard (the content needs to be present but could be a changing value)
def test_dashboard(home_page_login):
    data = load_data()
    home_page_login.navigate_to(data["url"])
    home_page_login.login(data["username"], data["password"])
    user = data["username"][:5]
    user = user.capitalize()
    email = data["username"]
    home_page_login.check_dashboard(user,email)