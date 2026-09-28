import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage
from pages.navigation_bar import NavigationBar

@allure.feature("Shopping Cart")
@allure.story("Remove a product from the cart")
@allure.title("TC-017 — Remove Products From Cart")
@allure.severity(allure.severity_level.NORMAL)
def test_remove_products_from_cart(driver: WebDriver):
    login_page = LoginPage(driver)
    products_page = ProductPage(driver)
    home_page = HomePage(driver)
    navigation_bar = NavigationBar(driver)

    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Verify Homepage"):
        assert home_page.verify_home()
    with allure.step("Record the selected product's details"):
        expected_name = home_page.first_product_name().text.strip()
        expected_price = home_page.first_product_price().text.strip()
        expected_quantity = "1"
    with allure.step("Hover over first product and click 'Add to cart'"):
        products_page.click_add_one()
    with allure.step("Click 'Continue Shopping' button"):
        products_page.continue_shopping()
    with allure.step("Click Cart In The Navigation Bar"):
        navigation_bar.click_cart()
    with allure.step("Verify the product in the cart"):
        cart_name = products_page.product_one_details()
        cart_price = products_page.price_one()
        cart_quantity = products_page.first_cart_quantity()
        assert cart_name.text.strip() == expected_name
        assert cart_price.text.strip() == expected_price
        assert cart_quantity.text.strip() == expected_quantity
        assert "/view_cart" in driver.current_url
    with allure.step("Remove the product from the cart"):
        products_page.click_remove()
    with allure.step("Verify the cart is empty"):
        empty_message = products_page.empty_cart_message()
        assert empty_message.is_displayed()
        assert empty_message.text.strip() == "Cart is empty!"