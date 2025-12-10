import pytest
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.review_page import ReviewPage
import time

def test_complete_checkout_flow(driver):
    # Initialize Pages
    login = LoginPage(driver)
    plp = ProductListingPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    payment = PaymentPage(driver)
    review = ReviewPage(driver)

    # 1. Login
    print("\nStep 1: Logging in...")
    login.login("bob@example.com", "10203040")

    # 2. Add Item
    print("Step 2: Adding Backpack to cart...")
    plp.add_backpack_to_cart()
    plp.open_cart()

    # 3. Cart -> Checkout
    print("Step 3: Proceeding to Checkout...")
    cart.proceed_to_checkout()

    # 4. Fill Shipping Info
    print("Step 4: Filling Shipping Address...")
    checkout.fill_shipping_info(
        full_name="Rebecca Winter", 
        address="Mandorley 112", 
        city="Truro", 
        zip_code="89750", 
        country="United Kingdom"
    )

    # 5. Fill Payment Info
    print("Step 5: Entering Payment Details...")
    payment.enter_payment_details("Rebecca Winter", "4242 4242 4242 4242", "12/30", "123")


    # 6. Review Order
    print("Step 6: Reviewing Order...")
    assert review.verify_product_is_present(), "Error: Backpack not found in Order Review!"
    review.place_order()

    # 7. Final Verification
    print("Step 7: Verifying Success...")
    assert review.is_checkout_complete(), "Error: 'Checkout Complete' message not seen!"
    print("   > Order Placed Successfully!")

    # 8. Continue Shopping (Return to Home)
    print("Step 8: Continuing Shopping...")
    review.click_continue_shopping()

    print(" >Waiting for home page to load...")
    time.sleep(3)  # Wait for the home page to load
    # NOTE: "Cancel Order" step is skipped because the button does not exist in this app.

    # 9. Logout
    print("Step 9: Logging Out...")
    login.logout()
    
    print("TEST PASSED: Full E2E Flow Completed!")