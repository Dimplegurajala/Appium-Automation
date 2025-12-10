import pytest
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage

def test_sort_by_price_low_to_high(driver):
    # 1. Initialize
    login_page = LoginPage(driver)
    plp = ProductListingPage(driver)

    # 2. Login
    login_page.login("bob@example.com", "10203040")
    
    # 3. Sort by Price (Ascending = Low to High)
    # UPDATED: Matches the screenshot text exactly
    print("Sorting products by 'Price - Ascending'...")
    plp.sort_products_by("Price - Ascending")

    # 4. Verification
    # Cheapest item is usually $7.99 (Sauce Labs Onesie)
    first_price = plp.get_first_item_price()
    
    # Assertion: Check if price is low (e.g. <= $10) or exactly $7.99
    assert first_price == 7.99, f"Sort Failed! Expected $7.99 (Low) but got ${first_price}"
    print("   > TEST PASSED: First item is the cheapest ($7.99)")

def test_sort_by_price_high_to_low(driver):
    # 1. Initialize
    login_page = LoginPage(driver)
    plp = ProductListingPage(driver)

    # 2. Login
    login_page.login("bob@example.com", "10203040")
    
    # 3. Sort by Price (Descending = High to Low)
    # UPDATED: Matches the screenshot text exactly
    print("Sorting products by 'Price - Descending'...")
    plp.sort_products_by("Price - Descending")

    # 4. Verification
    # Most expensive item is $49.99 (Sauce Labs Fleece Jacket)
    first_price = plp.get_first_item_price()

    assert first_price == 49.99, f"Sort Failed! Expected $49.99 (High) but got ${first_price}"
    print("   > TEST PASSED: First item is the most expensive ($49.99)")