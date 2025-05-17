from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
import allure
import src.urls


class TestResetPassword:
    @allure.title('Проверка перехода на страницу восстановления пароля через кнопку Восстановить пароль')
    def test_open_password_recovery_page_by_button_click(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_password_recovery_button()

        assert login_page.get_current_url() == src.urls.PASSWORD_RECOVERY_PAGE_URL

    @allure.title('Проверка ввода почты и работы кнопки Восстановить')
    def test_email_input_form_and_password_recovery_button_by_input_and_click(self, create_user, driver):
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.open_password_recovery_page()
        reset_password_page.fill_email_input_form(create_user)
        reset_password_page.click_password_recovery_button()

        assert reset_password_page.get_current_url() == src.urls.PASSWORD_RESET_PAGE_URL

    @allure.title('Проверка скрытия/показа текста в поле Пароль')
    def test_password_show_button_and_active_state_by_click_on_hide_password_button(self, driver, create_user):
        recovery_page = ResetPasswordPage(driver)
        recovery_page.open_password_reset_page(create_user)

        assert recovery_page.click_hide_password_icon()