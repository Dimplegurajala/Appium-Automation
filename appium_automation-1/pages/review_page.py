from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ReviewPage(BasePage):
    # --- LOCATORS ---
    
    PRODUCT_ITEM    = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")
    PLACE_ORDER_BTN = (AppiumBy.ACCESSIBILITY_ID, "Place Order button")
    
    # Final Screen
    CHECKOUT_COMPLETE = (AppiumBy.XPATH, "//android.widget.TextView[@text='Checkout Complete']")
    
    # V1 App usually uses "Continue Shopping button"
    CONTINUE_BTN      = (AppiumBy.ACCESSIBILITY_ID, "Continue Shopping button")

    # --- ACTIONS ---

    def verify_product_is_present(self):
        print("   > Verifying product in summary...")
        return self.is_visible(self.PRODUCT_ITEM)

    def place_order(self):
        print("   > Clicking 'Place Order'...")
        self.click(self.PLACE_ORDER_BTN)

    def is_checkout_complete(self):
        return self.is_visible(self.CHECKOUT_COMPLETE)
    
    def click_continue_shopping(self):
        print("   > Clicking 'Continue Shopping' to return home...")
        self.click(self.CONTINUE_BTN)