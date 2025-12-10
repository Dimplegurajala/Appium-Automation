from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    plp = ProductListingPage(driver)

    login_page.login("bob@example.com", "10203040")
    
    assert plp.is_on_products_page(), "Login failed: Products header not visible!"