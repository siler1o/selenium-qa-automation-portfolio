import allure
from uuid import uuid4

from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage
from pages.navigation_bar import NavigationBar
from pages.registration_page import RegistrationPage


@allure.feature("Shopping Cart")
@allure.story("Preserve searched products in cart after login")
@allure.title("TC-020 — Search Products and Verify Cart After Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_products_cart_after_login(driver: WebDriver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    products_page = ProductPage(driver)
    navigation_bar = NavigationBar(driver)
    registration_page = RegistrationPage(driver)

    signup_name = "Reuben QA tester"
    test_email = f"reuben.qa.{uuid4().hex}@example.com"
    test_password = "Password test"
    search_term = "top"

    address = {
        "first_name": "Reuben",
        "last_name": "Test",
        "company": "QA Test Company",
        "address1": "123 Test Street",
        "address2": "Unit 4",
        "country": "Singapore",
        "state": "Singapore",
        "city": "Singapore",
        "zipcode": "123456",
        "mobile_number": "12345678",
    }

    with allure.step("Setup: open Signup / Login"):
        login_page.goto()
        login_page.click_signup_login()

    with allure.step("Setup: register a unique test account"):
        login_page.insert_name(signup_name)
        login_page.insert_email(test_email)
        login_page.click_signup_wait()

        heading = registration_page.account_information_heading()
        assert heading.text.strip().upper() == "ENTER ACCOUNT INFORMATION"

        registration_page.select_title_mr()
        registration_page.fill_account_information(
            password=test_password,
            day="31",
            month="7",
            year="2001",
        )
        registration_page.set_preferences(
            newsletter=True,
            special_offers=True,
        )
        registration_page.fill_address_information(**address)
        registration_page.create_account()

        heading = registration_page.account_created_heading()
        assert heading.text.strip().upper() == "ACCOUNT CREATED!"

        registration_page.click_continue()
        assert registration_page.logged_in_name().text.strip() == signup_name

    with allure.step("Setup: log out before adding products"):
        login_page.click_logout()
        assert login_page.loginverify().is_displayed()

    with allure.step("Open the website and verify the homepage"):
        login_page.goto()
        assert home_page.verify_home()

    with allure.step("Open Products and verify the heading"):
        navigation_bar.click_product()
        heading = products_page.product_header()
        assert heading.text.strip().upper() == "ALL PRODUCTS"

    with allure.step("Search for products"):
        products_page.type_search(search_term)
        products_page.click_search()

    with allure.step("Verify the searched-products heading"):
        heading = products_page.search_header()
        assert heading.text.strip().upper() == "SEARCHED PRODUCTS"

    with allure.step("Record and validate all search results"):
        expected_products = products_page.searched_product_details()

        assert expected_products, "No search results were displayed"
        product_ids = [product["id"] for product in expected_products]
        assert len(product_ids) == len(set(product_ids)), (
            "Search results contained duplicate product IDs"
        )

        expected_products = sorted(
            expected_products,
            key=lambda product: product["id"],
        )

    with allure.step("Add every searched product once"):
        for product in expected_products:
            with allure.step(f"Add {product['name']} to cart"):
                products_page.add_product_by_id(product["id"])

    with allure.step("Verify cart contents before login"):
        navigation_bar.click_cart()
        actual_products = products_page.cart_product_details()

        assert "/view_cart" in driver.current_url
        assert sorted(
            actual_products,
            key=lambda product: product["id"],
        ) == expected_products, (
            "Cart contents before login did not match the selected products"
        )

    with allure.step("Open the login form"):
        login_page.click_signup_login()
        assert login_page.loginverify().is_displayed()

    with allure.step("Log in using the account created during setup"):
        login_page.enter_email(test_email)
        login_page.enter_pwd(test_password)
        login_page.click_login_wait()

        assert login_page.loggedin_indicator().is_displayed()
        assert registration_page.logged_in_name().text.strip() == signup_name

    with allure.step("Verify cart contents are preserved after login"):
        navigation_bar.click_cart()
        actual_products = products_page.cart_product_details()

        assert "/view_cart" in driver.current_url
        assert sorted(
            actual_products,
            key=lambda product: product["id"],
        ) == expected_products, (
            "Products, prices, or quantities changed after login"
        )

    with allure.step("Delete the account created by this test"):
        registration_page.delete_account()
        heading = registration_page.account_deleted_heading()
        assert heading.text.strip().upper() == "ACCOUNT DELETED!"

    with allure.step("Continue and verify the user is signed out"):
        registration_page.click_continue()
        assert home_page.verify_home()
        assert login_page.logged_out_indicator().is_displayed()