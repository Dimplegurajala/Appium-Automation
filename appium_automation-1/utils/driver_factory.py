from appium import webdriver
from appium.options.android import UiAutomator2Options
class DriverFactory:
    @staticmethod
    def get_driver():
        options = UiAutomator2Options()
        options.platform_name = "Android"
        
        # This is just a label, "Android Emulator" is fine.
        options.device_name = "Android Emulator" 
        
        # OPTIONAL: This forces Appium to use specifically emulator-5554
        # You only need this if you have multiple devices connected.
        # options.udid = "emulator-5554" 
        
        # YOUR FIXED PATH looks good now!
        options.app = r"C:\Users\reshm\OneDrive\Desktop\Project 2\Sauce.apk"
        
        options.automation_name = "UiAutomator2"
        options.no_reset = False 
        options.new_command_timeout = 300
        
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        driver.implicitly_wait(10)
        return driver