import allure
from urllib.parse import unquote, urlparse
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage
from pages.navigation_bar import NavigationBar


@allure.feature("Product Brands")
@allure.story("Browse products by brand")
@allure.title("TC-019 — View & Cart Brand Products")
@allure.severity(allure.severity_level.NORMAL)
def test_view_brand_products(driver: WebDriver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    products_page = ProductPage(driver)
    navigation_bar = NavigationBar(driver)

    with allure.step("Open Automation Exercise Website"):
        login_page.goto()

    with allure.step("Verify the homepage"):
        assert home_page.verify_home()

    with allure.step("Open the Products page"):
        navigation_bar.click_product()
        heading = products_page.product_header()
        assert heading.is_displayed()

    with allure.step("Verify the Brands heading"):
        heading = products_page.brands_heading()
        assert heading.is_displayed()
        assert heading.text.strip().upper() == "BRANDS"

    with allure.step("Select the Polo brand"):
        products_page.click_polo_brand()

    with allure.step("Verify the Polo brand page"):
        heading = products_page.brand_heading()
        assert heading.text.strip().upper() == "BRAND - POLO PRODUCTS"
        assert urlparse(driver.current_url).path == "/brand_products/Polo"

    with allure.step("Verify Polo products are displayed"):
        products = products_page.product_list()
        assert len(products) > 0, "No Polo products were displayed"

    with allure.step("Select the H&M brand from the sidebar"):
        products_page.click_hm_brand()

    with allure.step("Verify the H&M brand page"):
        heading = products_page.brand_heading()
        assert heading.text.strip().upper() == "BRAND - H&M PRODUCTS"
        assert unquote(urlparse(driver.current_url).path) == "/brand_products/H&M"

    with allure.step("Verify H&M products are displayed"):
        products = products_page.product_list()
        assert len(products) > 0, "No H&M products were displayed"