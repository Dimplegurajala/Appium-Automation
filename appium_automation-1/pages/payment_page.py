from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time  # <--- Import this!

class PaymentPage(BasePage):
    
    # --- LOCATORS ---
    FULL_NAME_INPUT  = (AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")
    CARD_NUM_INPUT   = (AppiumBy.ACCESSIBILITY_ID, "Card Number* input field")
    EXP_DATE_INPUT   = (AppiumBy.ACCESSIBILITY_ID, "Expiration Date* input field")
    CVV_INPUT        = (AppiumBy.ACCESSIBILITY_ID, "Security Code* input field")
    REVIEW_ORDER_BTN = (AppiumBy.ACCESSIBILITY_ID, "Review Order button")

    # --- ACTIONS ---

    def enter_payment_details(self, full_name, card_num, exp_date, cvv):
        
        # FIX 1: Wait for page animation to finish (Prevents immediate crash)
        print("   > Waiting for Payment Page to load...")
        time.sleep(2) 

        # 1. Full Name
        print(f"   > Entering Full Name: {full_name}...")
        name_element = self.driver.find_element(*self.FULL_NAME_INPUT)
        name_element.clear()
        name_element.send_keys(full_name)

        # 2. Card Number
        print(f"   > Entering Card Number: {card_num}...")
        card_element = self.driver.find_element(*self.CARD_NUM_INPUT)
        card_element.clear()
        card_element.send_keys(card_num)
        
        # 3. Expiration Date
        print(f"   > Entering Expiry: {exp_date}...")
        exp_element = self.driver.find_element(*self.EXP_DATE_INPUT)
        exp_element.clear()
        exp_element.send_keys(exp_date)
        
        # 4. CVV
        print(f"   > Entering CVV: {cvv}...")
        cvv_element = self.driver.find_element(*self.CVV_INPUT)
        cvv_element.clear()
        cvv_element.send_keys(cvv)
        
        # FIX 2: Hide keyboard before clicking the button
        try:
            self.driver.hide_keyboard()
        except:
            pass
            
        # FIX 3: Wait a moment for the keyboard to go away
        time.sleep(1)
        
        # 5. Review
        print("   > Clicking 'Review Order'...")
        self.click(self.REVIEW_ORDER_BTN)