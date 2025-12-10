from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CartPage(BasePage):
    # --- LOCATORS ---
    
    # STRATEGY: Use Accessibility ID with the " button" suffix pattern
    # Previous error: We looked for "Checkout button", but the text is "Proceed To Checkout"
    # New ID: "Proceed To Checkout button"
    CHECKOUT_BTN = (AppiumBy.ACCESSIBILITY_ID, "Proceed To Checkout button")
    
    # Item verification (XPath is still best here to match exact text content)
    CART_ITEM = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")

    # --- ACTIONS ---

    def proceed_to_checkout(self):
        print("   > Clicking 'Proceed To Checkout' Button...")
        self.click(self.CHECKOUT_BTN)