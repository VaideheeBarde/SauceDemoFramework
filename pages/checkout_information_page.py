import allure
from playwright.sync_api import Page
from .base_page import BasePage
from locators.checkout_information_locators import CheckoutInformationLocators

class CheckoutInformationPage(BasePage):

    def fill_customer_info(self, firstname, lastname, postalcode):
        with allure.step("Fill in the information"):
            self.page.fill(CheckoutInformationLocators.FIRST_NAME, firstname)
            self.page.fill(CheckoutInformationLocators.LAST_NAME, lastname)
            self.page.fill(CheckoutInformationLocators.POSTAL_CODE, postalcode)
            self.page.click(CheckoutInformationLocators.CONTINUE)
