from uuid import uuid4
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@allure.feature("User Registration")
@allure.story("Register a new user and delete the test account")
@allure.title("TC-001 — Register User")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_user(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    registration_page = RegistrationPage(driver)

    signup_name = "Reuben QA tester"
    test_email = f"reuben.qa.{uuid4().hex}@example.com"
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

    with allure.step("Open the website and verify the homepage URL"):
        login_page.goto()
        assert home_page.verify_home()

    with allure.step("Open Signup / Login and verify the signup heading"):
        login_page.click_signup_login()
        heading = login_page.newuserverify()
        assert heading.text.strip() == "New User Signup!"

    with allure.step("Sign up with a name and a unique email"):
        login_page.insert_name(signup_name)
        login_page.insert_email(test_email)
        login_page.click_signup_wait()

    with allure.step("Verify the account-information form"):
        heading = registration_page.account_information_heading()
        assert heading.text.strip().upper() == "ENTER ACCOUNT INFORMATION"

    with allure.step("Enter title, password, and date of birth"):
        registration_page.select_title_mr()
        registration_page.fill_account_information(
            password="Password test", day="31", month="7", year="2001",
        )

    with allure.step("Select newsletter and special-offer preferences"):
        registration_page.set_preferences(newsletter=True, special_offers=True)

    with allure.step("Enter the address and contact information"):
        registration_page.fill_address_information(**address)

    with allure.step("Create the account and verify confirmation"):
        registration_page.create_account()
        heading = registration_page.account_created_heading()
        assert heading.text.strip().upper() == "ACCOUNT CREATED!"

    with allure.step("Continue and verify the registered user is signed in"):
        registration_page.click_continue()
        assert registration_page.logged_in_name().text.strip() == signup_name

    with allure.step("Delete the account created by this test"):
        registration_page.delete_account()
        heading = registration_page.account_deleted_heading()
        assert heading.text.strip().upper() == "ACCOUNT DELETED!"

    with allure.step("Continue and verify the user is signed out"):
        registration_page.click_continue()
        assert home_page.verify_home()
        assert login_page.logged_out_indicator().is_displayed()
