import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage

@allure.feature("Shopping Cart")
@allure.story("Update product quantity")
@allure.title("TC-013 — Verify Product Quantity in Cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_quantity_in_cart(driver: WebDriver):
    login_page = LoginPage(driver)
    products_page = ProductPage(driver)
    home_page = HomePage(driver)
    expected_quantity = "4"

    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Verify Homepage"):
        assert home_page.verify_home()
    with allure.step("Click View Product for the first product"):
        home_page.click_product()
    with allure.step("Verify the product detail page"):
        assert "/product_details/1" in driver.current_url
        product_info = products_page.product_details()
        assert product_info.is_displayed()
    with allure.step("Record the displayed product name"):
        product_name = products_page.product_title().text.strip()
    with allure.step("Change the product quantity"):
        products_page.quantity_change(expected_quantity)
    with allure.step("Verify the quantity field value"):    
        quantity_check = products_page.quantity_check()
        assert quantity_check.get_attribute("value") == expected_quantity
    with allure.step("Click Add to cart"): 
        products_page.add_cart()
    with allure.step("Select View Cart in the confirmation"):  
        products_page.view_cart()
    with allure.step("Verify that it redirects to Cart"):
        assert "/view_cart" in driver.current_url
    with allure.step("Verify the selected product"): 
        product_title = products_page.product_one_details()
        assert product_title.text.strip() == product_name
    with allure.step("Verify the product quantity"): 
        cart_quantity = products_page.first_cart_quantity()
        assert cart_quantity.text.strip() == expected_quantity