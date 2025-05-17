from selenium import webdriver
import requests
import pytest
import src.generators
import src.urls
import src.data
import chromedriver_autoinstaller
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):

    if request.param == 'chrome':
        chromedriver_autoinstaller.install()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')

        web_driver = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        web_driver.maximize_window()

    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def create_user():
    email, password, name = src.generators.generate_user_data()
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    response = requests.post(src.urls.SIGN_UP_URL, data=payload)
    token = response.json().get("accessToken")

    yield email, password, name
    requests.delete(src.urls.REMOVE_USER_URL, headers={"Authorization": f'{token}'})

@pytest.fixture(scope='function')
def login_user_and_create_order(create_user):
    email, password, _ = create_user
    payload = {
        'email': email,
        'password': password,
    }
    response = requests.post(src.urls.LOGIN_USER_URL, data=payload)
    token = response.json().get("accessToken")
    payload = {
        "ingredients": [src.data.CRATER_BUN_ID, src.data.FILLET_MAIN_ID, src.data.CHEESE_MAIN_ID, src.data.SPICY_SAUCE_ID]
    }
    response = requests.post(src.urls.CREATE_ORDER_URL, headers={"Authorization": f'{token}'}, data=payload)
    number = str(response.json()['order']['number'])
    return email, password, number