class InventoryLocators:
    CART_BADGE = '[data-test="shopping-cart-link"]'

    @staticmethod
    def product_add_button(product_name: str):
        formatted_product_name = product_name.lower().replace(" ", "-")
        return f"[data-test='add-to-cart-{formatted_product_name}']"