import allure
from uuid import uuid4

from selenium.webdriver.chrome.webdriver import WebDriver
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage
from pages.navigation_bar import NavigationBar


@allure.feature("Checkout")
@allure.story("Place an order by logging in before checkout")
@allure.title("TC-016 — Place Order: Login Before Checkout")
@allure.severity(allure.severity_level.CRITICAL)
def test_order_login_before_checkout(driver: WebDriver):
    login_page = LoginPage(driver)
    products_page = ProductPage(driver)
    home_page = HomePage(driver)
    navigation_bar = NavigationBar(driver)
    registration_page = RegistrationPage(driver)

    signup_name = "Reuben QA tester"
    test_email = f"reuben.qa.{uuid4().hex}@example.com"
    test_password = "Password test"
    expected_quantity = "1"

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

    expected_full_name = (
        f"{address['first_name']} {address['last_name']}"
    )

    # Setup: create an account specifically for this test.
    with allure.step("Setup: open the registration page"):
        login_page.goto()
        login_page.click_signup_login()

    with allure.step("Setup: sign up with a unique email"):
        login_page.insert_name(signup_name)
        login_page.insert_email(test_email)
        login_page.click_signup_wait()

        heading = registration_page.account_information_heading()
        assert heading.text.strip().upper() == "ENTER ACCOUNT INFORMATION"

    with allure.step("Setup: complete account and address information"):
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

    with allure.step("Setup: create the account and verify confirmation"):
        registration_page.create_account()

        heading = registration_page.account_created_heading()
        assert heading.text.strip().upper() == "ACCOUNT CREATED!"

        registration_page.click_continue()
        assert registration_page.logged_in_name().text.strip() == signup_name

    with allure.step("Setup: log out before testing login"):
        login_page.click_logout()
        assert login_page.loginverify().is_displayed()

    # TC016 begins with an existing account and a logged-out user.
    with allure.step("Open the website and verify the homepage"):
        login_page.goto()
        assert home_page.verify_home()

    with allure.step("Open Signup / Login"):
        login_page.click_signup_login()
        assert login_page.loginverify().is_displayed()

    with allure.step("Enter the existing test account's credentials"):
        login_page.enter_email(test_email)
        login_page.enter_pwd(test_password)

    with allure.step("Submit the login form"):
        login_page.click_login_wait()

    with allure.step("Verify the correct user is logged in"):
        assert login_page.loggedin_indicator().is_displayed()
        assert registration_page.logged_in_name().text.strip() == signup_name

    with allure.step("Record the selected product's details"):
        expected_name = home_page.first_product_name().text.strip()
        expected_price = home_page.first_product_price().text.strip()

    with allure.step("Add the first product to the cart"):
        products_page.click_add_one()

    with allure.step("Click Continue Shopping"):
        products_page.continue_shopping()

    with allure.step("Open Cart from the navigation bar"):
        navigation_bar.click_cart()

    with allure.step("Verify the product in the cart"):
        cart_name = products_page.product_one_details()
        cart_price = products_page.price_one()
        cart_quantity = products_page.first_cart_quantity()

        assert "/view_cart" in driver.current_url
        assert cart_name.text.strip() == expected_name
        assert cart_price.text.strip() == expected_price
        assert cart_quantity.text.strip() == expected_quantity

    with allure.step("Proceed to checkout while signed in"):
        products_page.proceed_checkout()

    with allure.step("Verify the delivery address"):
        delivery_address = products_page.delivery_address()
        delivery_text = " ".join(delivery_address.text.split())

        assert expected_full_name in delivery_text
        assert address["company"] in delivery_text
        assert address["address1"] in delivery_text
        assert address["address2"] in delivery_text
        assert address["city"] in delivery_text
        assert address["state"] in delivery_text
        assert address["zipcode"] in delivery_text
        assert address["country"] in delivery_text
        assert address["mobile_number"] in delivery_text

    with allure.step("Verify the billing address"):
        billing_address = products_page.billing_address()
        billing_text = " ".join(billing_address.text.split())

        assert expected_full_name in billing_text
        assert address["company"] in billing_text
        assert address["address1"] in billing_text
        assert address["address2"] in billing_text
        assert address["city"] in billing_text
        assert address["state"] in billing_text
        assert address["zipcode"] in billing_text
        assert address["country"] in billing_text
        assert address["mobile_number"] in billing_text

    with allure.step("Verify the order review on the checkout page"):
        cart_name = products_page.product_one_details()
        cart_price = products_page.price_one()
        cart_quantity = products_page.first_cart_quantity()

        assert cart_name.text.strip() == expected_name
        assert cart_price.text.strip() == expected_price
        assert cart_quantity.text.strip() == expected_quantity

    with allure.step("Enter an order comment"):
        products_page.comment_order("Enter an example comment")

    with allure.step("Select Place Order"):
        products_page.place_order()

    with allure.step("Enter payment details"):
        products_page.fill_payment_information(
            name_on_card="QA Tester",
            card_number="4111111111111111",
            cvc="123",
            expiry_month="12",
            expiry_year="2030",
        )
        assert "/payment" in driver.current_url

    with allure.step("Select Pay and Confirm Order"):
        products_page.confirm_payment()

    with allure.step("Verify the order was placed successfully"):
        confirmation = products_page.order_confirmation()
        assert confirmation.is_displayed()
        assert confirmation.text.strip().upper() == "ORDER PLACED!"

    with allure.step("Continue to the homepage"):
        products_page.continue_after_order()
        assert home_page.verify_home()

    with allure.step("Delete the account created by this test"):
        registration_page.delete_account()

        heading = registration_page.account_deleted_heading()
        assert heading.text.strip().upper() == "ACCOUNT DELETED!"

    with allure.step("Continue and verify the user is signed out"):
        registration_page.click_continue()
        assert home_page.verify_home()
        assert login_page.logged_out_indicator().is_displayed()