from selenium import webdriver
import requests
import pytest
import src.generators
import src.urls
import src.data
import chromedriver_autoinstaller


@pytest.fixture()
def driver():
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


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