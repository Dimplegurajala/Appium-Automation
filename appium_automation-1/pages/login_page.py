from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    # --- LOCATORS (Legacy V1 App) ---
    
    # Menu
    MENU_ICON   = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    MENU_LOGIN  = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
    
    # NEW: Logout Locator (V1 App standard naming)
    MENU_LOGOUT = (AppiumBy.ACCESSIBILITY_ID, "menu item log out")

    # Login Screen
    USERNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    LOGIN_BTN      = (AppiumBy.ACCESSIBILITY_ID, "Login button")

    # --- ACTIONS ---

    def login(self, username, password):
        print("   > Opening Menu...")
        self.click(self.MENU_ICON)
        
        print("   > Clicking Login Menu Item...")
        self.click(self.MENU_LOGIN)
        
        print("   > Entering Credentials...")
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        
        print("   > Clicking Login Button...")
        self.click(self.LOGIN_BTN)

    def logout(self):
        """
        Logs out of the app.
        1. Click Menu (Hamburger)
        2. Click 'Log Out'
        """
        print("   > Opening Menu to Logout...")
        self.click(self.MENU_ICON)
        
        # Give menu animation a split second
        time.sleep(1)
        
        print("   > Clicking 'Log Out'...")
        self.click(self.MENU_LOGOUT)
        
        # Verify we are logged out by checking if "Log In" option reappears (Optional)
        # For now, we trust the click.