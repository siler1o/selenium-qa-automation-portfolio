from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:

    VIEW_PRODUCT = (By.LINK_TEXT, "View Product")
    FIRST_PRODUCT_NAME = (By.XPATH,"//div[contains(@class, 'productinfo')]/a[@data-product-id='1']/../p")
    FIRST_PRODUCT_PRICE = (By.XPATH,"//div[contains(@class, 'productinfo')]/a[@data-product-id='1']/../h2")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.home_url = "https://automationexercise.com/"


    def verify_home(self):
        return self.wait.until(
            EC.url_to_be(self.home_url)
        )
    
    def click_product(self):
        view_product = self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_PRODUCT
            )
        )
        view_product.click()

    def first_product_name(self):
        return self.wait.until(
        EC.visibility_of_element_located(self.FIRST_PRODUCT_NAME)
    )

    def first_product_price(self):
        return self.wait.until(
        EC.visibility_of_element_located(self.FIRST_PRODUCT_PRICE)
    )
    