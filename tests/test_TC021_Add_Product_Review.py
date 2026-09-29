import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage
from pages.navigation_bar import NavigationBar


@allure.feature("Product Reviews")
@allure.story("Submit a product review")
@allure.title("TC-021 — Add Review on Product")
@allure.severity(allure.severity_level.NORMAL)
def test_add_product_review(driver: WebDriver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    products_page = ProductPage(driver)
    navigation_bar = NavigationBar(driver)

    review_data = {
        "name": "Reuben QA Tester",
        "email": "reuben.qa@example.com",
        "review": (
            "Test review: The product details are clear and informative."
        ),
    }

    with allure.step("Open the website and verify the homepage"):
        login_page.goto()
        assert home_page.verify_home()

    with allure.step("Open Products and verify the heading"):
        navigation_bar.click_product()
        heading = products_page.product_header()
        assert heading.text.strip().upper() == "ALL PRODUCTS"

    with allure.step("Open the first product's detail page"):
        products_page.click_product()

        product_info = products_page.product_details()
        assert product_info.is_displayed()
        assert "/product_details/1" in driver.current_url

    with allure.step("Verify the review heading"):
        heading = products_page.review_heading()
        assert heading.is_displayed()
        assert heading.text.strip().upper() == "WRITE YOUR REVIEW"

    with allure.step("Enter the reviewer name, email, and review"):
        products_page.fill_review(**review_data)

    with allure.step("Verify the review form contains the entered data"):
        actual_values = products_page.review_field_values()
        assert actual_values == review_data, (
            "Review form values did not match the entered data"
        )

    with allure.step("Submit the review"):
        products_page.submit_review()

    with allure.step("Verify the success confirmation"):
        message = products_page.review_success_message()
        assert message.is_displayed()
        assert message.text.strip() == "Thank you for your review."