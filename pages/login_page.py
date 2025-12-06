import allure
from playwright.sync_api import Page
from .base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    
    def login(self, username: str, password: str):
        with allure.step("Login using username and password"):
            self.page.fill(LoginLocators.USERNAME_INPUT, username)
            self.page.fill(LoginLocators.PASSWORD_INPUT, password)
            self.page.click(LoginLocators.LOGIN_BUTTON)
