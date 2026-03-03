import json
import pytest
import logging

#Input data
def load_data():
    with open("data/login.json") as f:
        #Loads the data from data/login.json file into a dictionary
        return json.load(f)

#Testcases
@pytest.mark.parametrize("data",load_data())
def test_dashboard(home_page_login, data):
    #1. Load the login page.
    home_page_login.navigate_to(data["url"])
    logging.info("Page opened successfully")

    #2. Interact with the interface to change to the username/password version of the login page.
    #3. Input the username and password into their corresponding fields.
    #4. Click the login button to proceed to the logged-in state.
    home_page_login.login(data["username"], data["password"])
    logging.info("Logged in successfully")

    #5. Check that there is a loaded user number on the dashboard (the content needs to be present but could be a changing value)
    home_page_login.check_dashboard(data["username"][:5].capitalize(),data["username"])
    logging.info("Dashboard opened successfully with username and mail")