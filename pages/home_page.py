from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:

    VIEW_PRODUCT = (By.LINK_TEXT, "View Product")

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

    