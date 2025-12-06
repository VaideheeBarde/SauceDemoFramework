import allure
from playwright.sync_api import Page
from .base_page import BasePage
from locators.inventory_locators import InventoryLocators

class InventoryPage(BasePage):
    
    def add_product_to_cart(self, product_name: str):
        with allure.step("Add product to cart"):
            product = InventoryLocators.product_add_button(product_name)
            self.page.click(product)

    def cart_count(self):
        with allure.step("Count the number of items displayed on the cart"):
            if self.page.is_visible(InventoryLocators.CART_BADGE):
                return int(self.page.inner_text(InventoryLocators.CART_BADGE))
            return 0
        
    def go_to_cart(self):
        with allure.step("Go to cart"):
            self.page.click(InventoryLocators.CART_BADGE)
