from playwright.sync_api import sync_playwright
import time

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto('https://www.saucedemo.com/')

page.type(selector='[id="user-name"]', text='standard_user', delay=100)
page.fill(selector='#password', value='secret_sauce')
page.click(selector='.submit-button')
page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=10000)
page.wait_for_selector('#inventory_container')

button_add_card = '[data-test="add-to-cart-sauce-labs-backpack"]'
alt_locator_for_card = '[.inventory_item a:has-text("Sauce Labs Backpack")]'
card_button = '[.inventory_item_description:has-text("Sauce Labs Backpack" button:has-text("Add to cart")]'


page.is_visible(selector=button_add_card)
page.is_enabled(selector=button_add_card)
page.click(button_add_card)

page.click('[data-test="shopping-cart-link"]')
page.wait_for_url('https://www.saucedemo.com/cart.html')

buton_checkout = '#checkout'
page.is_visible(buton_checkout)
page.is_enabled(buton_checkout)
page.click(buton_checkout)

page.wait_for_url('https://www.saucedemo.com/checkout-step-one.html', timeout=10000)
page.fill(selector='#first-name', value='Firstname')
page.fill(selector='#last-name', value='Lastname')
page.fill(selector='#postal-code', value='123.0.0.0')
page.click('[id="continue"][type="submit"]')

button_finish = 'button:has-text("Finish")'
page.wait_for_url('https://www.saucedemo.com/checkout-step-two.html', timeout=10000)
page.wait_for_selector(button_finish)
page.click(button_finish)
page.wait_for_url('https://www.saucedemo.com/checkout-complete.html')

burger_menu = '[id="react-burger-menu-btn"]'
page.click(burger_menu)
page.click('[id="logout_sidebar_link"][class="bm-item menu-item"]')
page.wait_for_url('https://www.saucedemo.com/')

time.sleep(3)
browser.close()
playwright.stop()