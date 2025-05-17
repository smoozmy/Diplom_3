import src.urls
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
import allure


class TestProfilePage:
    @allure.title('Проверка перехода к Личному кабинету')
    def test_open_profile_page_by_button_click_on_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_login_page()

        assert main_page.get_current_url() == src.urls.SIGN_IN_PAGE_URL

    @allure.title('Проверка перехода к разделу История заказов')
    def test_open_orders_history_by_button_click_on_profile_page(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.open_login_page()
        login_page = LoginPage(driver)
        login_page.user_login(create_user)
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()

        assert profile_page.open_orders_history() == src.urls.ORDERS_PAGE_URL

    @allure.title('Проверка на выход из профиля')
    def test_check_user_log_out_by_button_click_on_profile_page(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.open_login_page()
        login_page = LoginPage(driver)
        login_page.user_login(create_user)
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()

        assert profile_page.profile_log_out() == src.urls.SIGN_IN_PAGE_URL
