Prerequisites:

1. Create a virtual environment and install the below packages
.\\venv\\Scripts\\Activate.ps1

2. Install Pytest and playwright

3. For browser dependencies, install using "playwright install"

4. To run the testcase, use below command format from root folder:
python -m pytest tests/test_login.py --html=report.html -v --headed

5. Modify the username and password in data/login.json file for input data

