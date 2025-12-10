from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class ProductListingPage(BasePage):
    # --- LOCATORS (Old App Version) ---
    
    # 1. Verification & Navigation
    CART_ICON = (AppiumBy.ACCESSIBILITY_ID, "cart badge")
    
    # 2. Sorting
    SORT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "sort button")
    ITEM_PRICES = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '$')]")
    
    # 3. Add to Cart (From your working script)
    # We click the text to open the details, then click the button
    BACKPACK_ITEM = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")
    ADD_TO_CART_BTN = (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")

    # --- ACTIONS ---

    def is_on_products_page(self):
        """Checks if the Cart Icon is visible (Proof we are logged in)"""
        return self.is_visible(self.CART_ICON)

    def open_cart(self):
        """Clicks the cart icon to go to the Cart Page"""
        print("   > Opening Cart...")
        self.click(self.CART_ICON)

    def add_backpack_to_cart(self):
        """
        Flow matches your working script:
        1. Click 'Sauce Labs Backpack' text
        2. Click 'Add To Cart' button
        """
        print("   > Clicking 'Sauce Labs Backpack' item...")
        self.click(self.BACKPACK_ITEM)
        
        print("   > Clicking 'Add To Cart' button...")
        self.click(self.ADD_TO_CART_BTN)
        
        # Optional: Wait a moment for animation
        time.sleep(1) 

    def sort_products_by(self, sort_option_text):
        print(f"   > Clicking Sort Button...")
        self.click(self.SORT_BUTTON)
        
        print(f"   > Selecting option: '{sort_option_text}'...")
        option_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{sort_option_text}")')
        self.click(option_locator)
        time.sleep(1.5) #waiting for animation to finish

    def get_first_item_price(self):
        prices = self.driver.find_elements(*self.ITEM_PRICES)
        if prices:
           price_text = prices[0].text
           print(f"   > First item price found: {price_text}")
           clean_price = price_text.replace("$", "").strip()
           return float(clean_price)
            
        print("   > [WARNING] No price elements found!")
        return 0.0
        