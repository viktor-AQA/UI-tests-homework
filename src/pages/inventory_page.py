from src.pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CARD_SELECTOR = ".inventory_item >> text='Add to cart'"
    SHOPPING_CARD_SELECTOR = '[data-test="shopping-cart-link"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    def add_first_item_to_card(self):
        self.wait_for_selector_and_click(self.ADD_TO_CARD_SELECTOR)
        self.assert_element_is_visible(self.SHOPPING_CARD_SELECTOR)
        self.wait_for_selector_and_click(self.SHOPPING_CARD_SELECTOR)
