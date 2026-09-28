import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage


@allure.feature("Product Categories")
@allure.story("Browse products by category")
@allure.title("TC-018 — View Category Products")
@allure.severity(allure.severity_level.NORMAL)
def test_view_category_products(driver: WebDriver):
    login_page = LoginPage(driver)
    products_page = ProductPage(driver)
    home_page = HomePage(driver)

    with allure.step("Open Automation Exercise Website"):
        login_page.goto()

    with allure.step("Verify Homepage"):
        assert home_page.verify_home()

    with allure.step("Verify the category options are visible"):
        assert home_page.women_category().is_displayed()
        assert home_page.men_category().is_displayed()
        assert home_page.kids_category().is_displayed()

    with allure.step("Expand Women Category"):
        home_page.click_woman_category()

    with allure.step("Select Tops under Women"):
        home_page.click_women_tops()

    with allure.step("Verify the Women Tops category page"):
        heading = products_page.category_heading()
        assert heading.text.strip().upper() == "WOMEN - TOPS PRODUCTS"
        assert "/category_products/2" in driver.current_url

    with allure.step("Verify Women Tops products are visible"):
        products = products_page.product_list()
        assert len(products) > 0, "No Women Tops products were displayed"

    with allure.step("Expand Men Category"):
        home_page.click_men_category()

    with allure.step("Select Tshirts under Men"):
        home_page.click_men_tshirts()

    with allure.step("Verify the Men Tshirts category page"):
        heading = products_page.category_heading()
        assert heading.text.strip().upper() == "MEN - TSHIRTS PRODUCTS"
        assert "/category_products/3" in driver.current_url

    with allure.step("Verify Men Tshirts products are visible"):
        products = products_page.product_list()
        assert len(products) > 0, "No Men Tshirts products were displayed"