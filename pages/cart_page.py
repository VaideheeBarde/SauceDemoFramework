import allure
from playwright.sync_api import Page
from .base_page import BasePage
from locators.cart_locators import CartLocators

class CartPage(BasePage):

    def click_checkout(self):
        with allure.step("Click on the checkout button"):
            self.page.click(CartLocators.CHECKOUT_BUTTON)
