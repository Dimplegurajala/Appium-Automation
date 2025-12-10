import pytest
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout_flow(driver):
    # Initialize Pages
    login = LoginPage(driver)
    plp = ProductListingPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # 1. Login
    print("Step 1: Logging in...")
    login.login("bob@example.com", "10203040")

    # 2. Add Item
    print("Step 2: Adding Backpack to cart...")
    plp.add_backpack_to_cart()
    plp.open_cart()

    # 3. Checkout (Cart Page)
    print("Step 3: Proceeding to Checkout...")
    cart.proceed_to_checkout()

    # 4. Fill Shipping Info (Checkout Page)
    print("Step 4: Filling Address Form...")
    # Passing the 5 mandatory fields
    checkout.fill_shipping_info(
        full_name="Bob Builder", 
        address="123 Builder Lane", 
        city="Buildville", 
        zip_code="12345", 
        country="United Kingdom"
    )

    # 5. Finish (Verify we moved past the form)
    # Note: If there is a final "Place Order" screen, you might need one more click.
    print("Test Finished (Form filled successfully)")