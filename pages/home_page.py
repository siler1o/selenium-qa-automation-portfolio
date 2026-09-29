from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:

    VIEW_PRODUCT = (By.LINK_TEXT, "View Product")
    FIRST_PRODUCT_NAME = (By.XPATH,"//div[contains(@class, 'productinfo')]/a[@data-product-id='1']/../p")
    FIRST_PRODUCT_PRICE = (By.XPATH,"//div[contains(@class, 'productinfo')]/a[@data-product-id='1']/../h2")
    WOMEN_CATEGORY = (By.CSS_SELECTOR, ".badge.pull-right")
    WOMEN_CATEGORY = (By.CSS_SELECTOR, "a[href='#Women']")
    MEN_CATEGORY = (By.CSS_SELECTOR, "a[href='#Men']")
    KIDS_CATEGORY = (By.CSS_SELECTOR, "a[href='#Kids']")
    RECOMMENDED_HEADING = (By.CSS_SELECTOR,".recommended_items h2.title", )
    ACTIVE_RECOMMENDED_PRODUCT = (By.CSS_SELECTOR,"#recommended-item-carousel .item.active:not(.left):not(.right) "".productinfo",)
    ADD_CONFIRMATION = (By.ID, "cartModal")
    WOMEN_TOPS = (
        By.CSS_SELECTOR,
        "a[href='/category_products/2']"
    )
    MEN_TSHIRTS = (
        By.CSS_SELECTOR,
        "a[href='/category_products/3']"
    )


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

    def click_woman_category(self):
        click_woman = self.wait.until(
            EC.element_to_be_clickable(
                self.WOMEN_CATEGORY
            )
        )
        click_woman.click()

    def women_category(self):
        return self.wait.until(
        EC.visibility_of_element_located(self.WOMEN_CATEGORY)
    )


    def men_category(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MEN_CATEGORY)
        )


    def kids_category(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.KIDS_CATEGORY)
        )


    def click_woman_category(self):
        self.wait.until(
            EC.element_to_be_clickable(self.WOMEN_CATEGORY)
        ).click()


    def click_women_tops(self):
        self.wait.until(
            EC.element_to_be_clickable(self.WOMEN_TOPS)
        ).click()


    def click_men_category(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MEN_CATEGORY)
        ).click()


    def click_men_tshirts(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MEN_TSHIRTS)
        ).click()


    def scroll_to_recommended_items(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.RECOMMENDED_HEADING)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            heading,
        )


    def recommended_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.RECOMMENDED_HEADING)
        )


    def add_recommended_product(self):
        card = self.wait.until(
            EC.visibility_of_element_located(
                self.ACTIVE_RECOMMENDED_PRODUCT
            )
        )

        # Hover over the selected recommendation before reading and clicking.
        ActionChains(self.driver).move_to_element(card).perform()

        button = card.find_element(
            By.CSS_SELECTOR,
            "a.add-to-cart[data-product-id]",
        )

        product = {
            "id": button.get_attribute("data-product-id"),
            "name": card.find_element(
                By.CSS_SELECTOR, "p"
            ).text.strip(),
            "price": card.find_element(
                By.CSS_SELECTOR, "h2"
            ).text.strip(),
            "quantity": "1",
        }

        self.wait.until(
            EC.element_to_be_clickable(button)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.ADD_CONFIRMATION)
        )

        return product