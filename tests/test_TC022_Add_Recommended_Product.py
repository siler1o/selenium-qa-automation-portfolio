import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage


@allure.feature("Shopping Cart")
@allure.story("Add a recommended product to the cart")
@allure.title("TC-022 — Add to Cart from Recommended Items")
@allure.severity(allure.severity_level.NORMAL)
def test_add_recommended_product_to_cart(driver: WebDriver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    products_page = ProductPage(driver)

    with allure.step("Open the website and verify the homepage"):
        login_page.goto()
        assert home_page.verify_home()

    with allure.step("Scroll to the recommended-items section"):
        home_page.scroll_to_recommended_items()

    with allure.step("Verify the recommended-items heading"):
        heading = home_page.recommended_heading()
        assert heading.is_displayed()
        assert heading.text.strip().upper() == "RECOMMENDED ITEMS"

    with allure.step("Record and add a visible recommended product"):
        expected_product = home_page.add_recommended_product()

        assert expected_product["id"], "Product ID was missing"
        assert expected_product["name"], "Product name was empty"
        assert expected_product["price"], "Product price was empty"

    with allure.step("Select View Cart in the confirmation"):
        products_page.view_cart()

    with allure.step("Verify the cart page and selected product"):
        actual_products = products_page.cart_product_details()

        assert "/view_cart" in driver.current_url
        assert len(actual_products) == 1, (
            f"Expected one cart item, found {len(actual_products)}"
        )

        actual_product = actual_products[0]

        assert actual_product["id"] == expected_product["id"]
        assert actual_product["name"] == expected_product["name"]

    with allure.step("Verify the recommended product's price and quantity"):
        assert actual_product["price"] == expected_product["price"]
        assert actual_product["quantity"] == "1"