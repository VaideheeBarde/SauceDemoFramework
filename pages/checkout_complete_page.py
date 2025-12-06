import allure
from playwright.sync_api import Page
from .base_page import BasePage
from locators.checkout_complete_locators import CheckoutCompleteLocators

class CheckoutCompletePage(BasePage):
    
    def get_order_status(self):
        with allure.step("Return the confirmation messsage"):
            return self.page.inner_text(CheckoutCompleteLocators.HEADER)

    def back_home(self):
        with allure.step("Click on Back Home"):
            self.page.click(CheckoutCompleteLocators.BACK_HOME)
