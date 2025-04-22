from src.pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    CHECKOUT_BUTTON_SELECTOR = '#checkout'
    FIRSTNAME_SELECTOR = '#first-name'
    LASTNAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = '#postal-code'
    CONTINUE_BUTTON_SELECTOR = '[data-test="continue"]'
    BURGER_MENU_SELECTOR = '[id="react-burger-menu-btn"]'
    LOGAUT_SELECTOR = '[id="logout_sidebar_link"][class="bm-item menu-item"]'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.FIRSTNAME_SELECTOR)

    def fill_checkout_form(self, first_name, last_name, postal_code ):
        self.wait_for_selector_and_type(self.FIRSTNAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(self.LASTNAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 100)
        self.wait_for_selector_and_click(self.CONTINUE_BUTTON_SELECTOR)

    def logaut(self):
        self.wait_for_selector_and_click(self.BURGER_MENU_SELECTOR)
        self.wait_for_selector_and_click(self.LOGAUT_SELECTOR)
