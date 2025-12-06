import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from utilities.constants import Constants

@pytest.mark.order(1)
def test_login_success(page):
    with allure.step("Login into SauceLabs"):
        login = LoginPage(page)
        login.login(Constants.username, Constants.password)

        assert page.url.endswith("/inventory.html"), "Login failed"

@pytest.mark.order(2)
def test_add_products_and_goto_cart(page):
    with allure.step("Add product to cart"):
        inventory = InventoryPage(page)
        products = Constants.products

        for product in products:
            inventory.add_product_to_cart(product)

        count = inventory.cart_count()
        assert count == len(products), f"Cart count is {count}, expected {len(products)}"

        with allure.step("Navigate to cart"):
            inventory.go_to_cart()
            assert page.url.endswith("/cart.html"), "Not navigated to Cart page"

@pytest.mark.order(3)
def test_checkout_button(page):
    with allure.step("Click checkout on Cart page"):
        cart = CartPage(page)
        cart.click_checkout()

        assert "checkout-step-one" in page.url, "Checkout Step One page not loaded"

@pytest.mark.order(4)
def test_fill_customer_info(page):
    with allure.step("Fill customer information in checkout information page"):
        checkoutInformation = CheckoutInformationPage(page)
        checkoutInformation.fill_customer_info("Vaidehee", "Barde", "12345")

        assert "checkout-step-two" in page.url, "Checkout Step Two page not loaded"

@pytest.mark.order(5)
def test_complete_order(page):
    with allure.step("Click Finish in Checkout Overview page"):
        checkoutOverview = CheckoutOverviewPage(page)
        checkoutOverview.click_finish()

    with allure.step("Validate order success message in Checkout Complete Page"):
        checkoutComplete = CheckoutCompletePage(page)
        status = checkoutComplete.get_order_status()

        assert "Thank you for your order!" in status, f"Order completion message incorrect: {status}"