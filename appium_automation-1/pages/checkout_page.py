from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class CheckoutPage(BasePage):
    # --- LOCATORS ---
    FULL_NAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")
    ADDRESS_INPUT   = (AppiumBy.ACCESSIBILITY_ID, "Address Line 1* input field")
    CITY_INPUT      = (AppiumBy.ACCESSIBILITY_ID, "City* input field")
    ZIP_INPUT       = (AppiumBy.ACCESSIBILITY_ID, "Zip Code* input field")
    COUNTRY_INPUT   = (AppiumBy.ACCESSIBILITY_ID, "Country* input field")
    TO_PAYMENT_BTN  = (AppiumBy.ACCESSIBILITY_ID, "To Payment button")

    # --- ACTIONS ---
    
    # INDENTATION FIX: This line must be indented 4 spaces to belong to the class
    def fill_shipping_info(self, full_name, address, city, zip_code, country):
        print(f"   > Entering Full Name: {full_name}...")
        self.fill(self.FULL_NAME_INPUT, full_name)
        
        print(f"   > Entering Address: {address}...")
        self.fill(self.ADDRESS_INPUT, address)
        
        print(f"   > Entering City: {city}...")
        self.fill(self.CITY_INPUT, city)
        
        print(f"   > Entering Zip: {zip_code}...")
        self.fill(self.ZIP_INPUT, zip_code)

        print(f"   > Entering Country: {country}...")
        self.fill(self.COUNTRY_INPUT, country)
        
        # --- SCROLL & KEYBOARD FIX ---
        
        # 1. Hide Keyboard
        try:
            self.driver.hide_keyboard()
        except:
            pass 

        # 2. Scroll to the BOTTOM (Using the blind scroll method)
        print("   > Scrolling down...")
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR, 
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(3)'
            )
        except Exception as e:
            print(f"   > [Warning] Scroll command had an issue: {e}")

        # 3. Click 'To Payment'
        print("   > Clicking 'To Payment'...")
        try:
            self.click(self.TO_PAYMENT_BTN)
        except:
            # Fallback if ID fails
            print("   > [Retry] Access ID failed, trying by Text...")
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='To Payment']").click()