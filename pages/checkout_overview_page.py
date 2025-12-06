import allure
from playwright.sync_api import Page
from .base_page import BasePage
from locators.checkout_overview_locators import CheckoutOverviewLocators

class CheckoutOverviewPage(BasePage):

    def click_finish(self):
        with allure.step("Click on Finish"):
            self.page.click(CheckoutOverviewLocators.FINISH)
