from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
import allure

class ProfilePage(BasePage):
    @allure.step('Открываем страницу профиля')
    def open_profile_page(self):
        self.wait_for_element(ProfilePageLocators.ACCOUNT_PAGE_MENU_BUTTON, 'visibility')
        self.click_on_element(ProfilePageLocators.ACCOUNT_PAGE_MENU_BUTTON)

    @allure.step('Открываем историю заказов')
    def open_orders_history(self):
        self.wait_for_element(ProfilePageLocators.ORDER_HISTORY_MENU_BUTTON, 'visibility')
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_MENU_BUTTON)
        return self.get_current_url()

    @allure.step('Поиск номера заказа в истории заказов')
    def search_number_in_orders_history(self):
        self.wait_for_element(ProfilePageLocators.ORDER_NUMBER_BOX, 'visibility')
        orders_history_number = self.get_text(ProfilePageLocators.ORDER_NUMBER_TEXT)
        return orders_history_number.lstrip('#0')

    @allure.step('Выход из аккаунта')
    def profile_log_out(self):
        self.wait_for_element(ProfilePageLocators.LOG_OUT_BUTTON, 'visibility')
        self.click_on_element(ProfilePageLocators.LOG_OUT_BUTTON)
        self.wait_for_element(ProfilePageLocators.LOG_IN_BUTTON, 'visibility')
        return self.get_current_url()