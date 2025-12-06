from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_page(self, locator: str):
        self.page.wait_for_selector(locator)
