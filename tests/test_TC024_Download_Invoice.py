import allure
from pathlib import Path
from uuid import uuid4

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage
from pages.navigation_bar import NavigationBar
from pages.registration_page import RegistrationPage


@allure.feature("Checkout")
@allure.story("Download an invoice after placing an order")
@allure.title("TC-024 — Download Invoice After Purchase Order")
@allure.severity(allure.severity_level.NORMAL)
def test_download_invoice(driver: WebDriver, download_dir: Path):
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

    with allure.step("Record the first product's details"):
        expected_name = home_page.first_product_name().text.strip()
        expected_price = home_page.first_product_price().text.strip()
        expected_quantity = "1"

    with allure.step("Add the product and continue shopping"):
        products_page.click_add_one()
        products_page.continue_shopping()

    with allure.step("Open Cart and verify the selected product"):
        navigation_bar.click_cart()

        assert products_page.product_one_details().text.strip() == expected_name
        assert products_page.price_one().text.strip() == expected_price
        assert products_page.first_cart_quantity().text.strip() == expected_quantity
        assert "/view_cart" in driver.current_url

    with allure.step("Proceed to checkout and select Register / Login"):
        products_page.proceed_checkout()
        products_page.click_checkout_register()

    with allure.step("Sign up with a unique email"):
        login_page.insert_name(signup_name)
        login_page.insert_email(test_email)
        login_page.click_signup_wait()

        heading = registration_page.account_information_heading()
        assert heading.text.strip().upper() == "ENTER ACCOUNT INFORMATION"

    with allure.step("Complete account information"):
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

    with allure.step("Complete address information"):
        registration_page.fill_address_information(**address)

    with allure.step("Create the account and verify confirmation"):
        registration_page.create_account()
        heading = registration_page.account_created_heading()
        assert heading.text.strip().upper() == "ACCOUNT CREATED!"

    with allure.step("Continue and verify the registered user"):
        registration_page.click_continue()
        assert registration_page.logged_in_name().text.strip() == signup_name

    with allure.step("Return to Cart and proceed to checkout"):
        navigation_bar.click_cart()
        assert products_page.product_one_details().is_displayed()
        products_page.proceed_checkout()
        assert products_page.delivery_address().is_displayed()
        assert "/checkout" in driver.current_url

    with allure.step("Verify delivery address"):
        assert (
            products_page.delivery_address_lines()
            == expected_address_lines
        )

    with allure.step("Verify billing address"):
        assert (
            products_page.billing_address_lines()
            == expected_address_lines
        )

    with allure.step("Verify the order review"):
        assert products_page.product_one_details().text.strip() == expected_name
        assert products_page.price_one().text.strip() == expected_price
        assert products_page.first_cart_quantity().text.strip() == expected_quantity

    with allure.step("Enter a comment and select Place Order"):
        products_page.comment_order("Invoice download test order")
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

    with allure.step("Verify the order confirmation"):
        confirmation = products_page.order_confirmation()
        assert confirmation.text.strip().upper() == "ORDER PLACED!"

    with allure.step("Download the invoice"):
        assert not list(download_dir.iterdir()), (
            "The test download directory was not empty"
        )
        products_page.download_invoice()

    with allure.step("Verify the invoice download completed"):
        invoice_path = download_dir / "invoice.txt"

        def download_completed(_driver):
            return (
                invoice_path.is_file()
                and invoice_path.stat().st_size > 0
                and not list(download_dir.glob("*.crdownload"))
                and not list(download_dir.glob("*.tmp"))
            )

        WebDriverWait(driver, 30).until(
            download_completed,
            message=(
                "A completed, non-empty invoice.txt "
                "was not downloaded within 30 seconds"
            ),
        )

        allure.attach.file(
            str(invoice_path),
            name="Downloaded invoice",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Continue to the homepage"):
        products_page.continue_after_order()
        assert home_page.verify_home()

    with allure.step("Delete the account created by this test"):
        registration_page.delete_account()
        heading = registration_page.account_deleted_heading()
        assert heading.text.strip().upper() == "ACCOUNT DELETED!"

    with allure.step("Continue and verify sign-out"):
        registration_page.click_continue()
        assert home_page.verify_home()
        assert login_page.logged_out_indicator().is_displayed()