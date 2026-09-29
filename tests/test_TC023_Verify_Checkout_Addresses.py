import allure
from uuid import uuid4

from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage
from pages.navigation_bar import NavigationBar
from pages.registration_page import RegistrationPage


@allure.feature("Checkout")
@allure.story("Validate delivery and billing addresses")
@allure.title("TC-023 — Verify Address Details in Checkout Page")
@allure.severity(allure.severity_level.CRITICAL)
def test_verify_checkout_addresses(driver: WebDriver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    products_page = ProductPage(driver)
    navigation_bar = NavigationBar(driver)
    registration_page = RegistrationPage(driver)

    signup_name = "Reuben QA Tester"
    test_email = f"reuben.qa.{uuid4().hex}@example.com"

    address = {
        "first_name": "Reuben",
        "last_name": "Test",
        "company": "QA Test Company",
        "address1": "123 Test Street",
        "address2": "Unit 4",
        "country": "Canada",
        "state": "Ontario",
        "city": "Toronto",
        "zipcode": "M5V 2T6",
        "mobile_number": "4165550123",
    }

    expected_address_lines = [
        f"Mr. {address['first_name']} {address['last_name']}",
        address["company"],
        address["address1"],
        address["address2"],
        f"{address['city']} {address['state']} {address['zipcode']}",
        address["country"],
        address["mobile_number"],
    ]

    with allure.step("Open the website and verify the homepage"):
        login_page.goto()
        assert home_page.verify_home()

    with allure.step("Open Signup / Login"):
        login_page.click_signup_login()

    with allure.step("Sign up with a unique email"):
        login_page.insert_name(signup_name)
        login_page.insert_email(test_email)
        login_page.click_signup_wait()

        heading = registration_page.account_information_heading()
        assert heading.text.strip().upper() == "ENTER ACCOUNT INFORMATION"

    with allure.step("Enter account information"):
        registration_page.select_title_mr()
        registration_page.fill_account_information(
            password="Password test",
            day="31",
            month="7",
            year="2001",
        )
        registration_page.set_preferences(
            newsletter=True,
            special_offers=True,
        )

    with allure.step("Enter the address and contact information"):
        registration_page.fill_address_information(**address)

    with allure.step("Create the account and verify confirmation"):
        registration_page.create_account()

        heading = registration_page.account_created_heading()
        assert heading.text.strip().upper() == "ACCOUNT CREATED!"

    with allure.step("Continue and verify the registered user"):
        registration_page.click_continue()
        assert registration_page.logged_in_name().text.strip() == signup_name

    with allure.step("Add a product to the cart"):
        products_page.click_add_one()
        products_page.continue_shopping()

    with allure.step("Open and verify the cart"):
        navigation_bar.click_cart()
        assert products_page.product_one_details().is_displayed()
        assert "/view_cart" in driver.current_url

    with allure.step("Proceed to checkout"):
        products_page.proceed_checkout()
        assert products_page.delivery_address().is_displayed()
        assert "/checkout" in driver.current_url

    with allure.step("Verify delivery address matches registration data"):
        actual_delivery = products_page.delivery_address_lines()

        assert actual_delivery == expected_address_lines, (
            "Delivery address did not match the registration data.\n"
            f"Expected: {expected_address_lines}\n"
            f"Actual: {actual_delivery}"
        )

    with allure.step("Verify billing address matches registration data"):
        actual_billing = products_page.billing_address_lines()

        assert actual_billing == expected_address_lines, (
            "Billing address did not match the registration data.\n"
            f"Expected: {expected_address_lines}\n"
            f"Actual: {actual_billing}"
        )

    with allure.step("Delete the account created by this test"):
        registration_page.delete_account()

        heading = registration_page.account_deleted_heading()
        assert heading.text.strip().upper() == "ACCOUNT DELETED!"

    with allure.step("Continue and verify the user is signed out"):
        registration_page.click_continue()
        assert home_page.verify_home()
        assert login_page.logged_out_indicator().is_displayed()