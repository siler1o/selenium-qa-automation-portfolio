import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage


@allure.feature("Page Navigation")
@allure.story("Return to the top using the scroll-up arrow")
@allure.title("TC-025 — Verify Scroll Up Using Arrow Button")
@allure.severity(allure.severity_level.NORMAL)
def test_scroll_up_using_arrow(driver: WebDriver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    with allure.step("Open the website and verify the homepage"):
        login_page.goto()
        assert home_page.verify_home()

    with allure.step("Scroll to the bottom of the page"):
        home_page.scroll_to_bottom()

    with allure.step("Verify Subscription is visible on screen"):
        heading = home_page.subscription_heading_in_view()

        assert heading.text.strip().upper() == "SUBSCRIPTION"
        assert home_page.scroll_position() > 0, (
            "The page did not scroll down"
        )

    with allure.step("Click the scroll-up arrow"):
        home_page.click_scroll_up_arrow()

    with allure.step("Verify the page returned to the top"):
        assert home_page.scroll_position() <= 1, (
            "The page did not return to the top"
        )

    with allure.step("Verify the homepage banner text is visible on screen"):
        heading = home_page.home_banner_in_view()

        assert " ".join(heading.text.split()) == (
            "Full-Fledged practice website for Automation Engineers"
        )