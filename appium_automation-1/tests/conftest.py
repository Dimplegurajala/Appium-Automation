import sys
import os

# 1. Get the folder where this file is (tests/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go ONE LEVEL UP to the project root (appium_automation/)
project_root = os.path.dirname(current_dir)

# 3. Add the project root to Python's path
sys.path.append(project_root)
import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def driver():
    # 1. Setup: Get driver from Factory
    driver = DriverFactory.get_driver()
    
    # 2. Yield: Pass driver to the test function
    yield driver
    
    # 3. Teardown: Quit driver after test finishes
    driver.quit()