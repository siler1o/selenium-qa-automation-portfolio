from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage:
    ALL_PRODUCTS_HEADING = (By.XPATH,"//h2[normalize-space()='All Products']")
    ADD_CART = (By.CSS_SELECTOR, "button.btn.btn-default.cart")
    CHANGE_QUANTITY = (By.ID, "quantity")
    LISTING_PRICE_ONE = (By.XPATH,"//div[contains(@class, 'productinfo')][.//a[@data-product-id='1']]//h2")
    LISTING_PRICE_TWO = (By.XPATH,"//div[contains(@class, 'productinfo')][.//a[@data-product-id='2']]//h2")
    PRODUCT_LIST = (By.CLASS_NAME, "productinfo")
    VIEW_PRODUCT = (By.LINK_TEXT, "View Product")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product-information h2")
    PRODUCT_INFORMATION = (By.CSS_SELECTOR, "div.product-information")
    SEARCH_BAR = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_HEADER = (By.XPATH,"//h2[text()='Searched Products']")
    PRODUCT_ONE = (By.CSS_SELECTOR,"a[data-product-id='1']" )
    PRODUCT_TWO = (By.CSS_SELECTOR,"a[data-product-id='2']" )
    CONTINUE_SHOP = (By.CSS_SELECTOR,"button[class='btn btn-success close-modal btn-block']")
    VIEW_CART = (By.LINK_TEXT,"View Cart")
    PRODUCT_DETAILS_ONE = (By.CSS_SELECTOR,".cart_description a[href='/product_details/1']")
    PRODUCT_DETAILS_TWO = (By.CSS_SELECTOR, ".cart_description a[href='/product_details/2']")
    FIRST_PRICE = (By.CSS_SELECTOR, "#product-1 > .cart_price")
    SECOND_PRICE = (By.CSS_SELECTOR, "#product-2 > .cart_price")                      
    FIRST_QUANITY = (By.CSS_SELECTOR, "#product-1 > .cart_quantity > button")     
    SECOND_QUANITY = (By.CSS_SELECTOR, "#product-2 > .cart_quantity > button")  
    FIRST_TOTAL = (By.CSS_SELECTOR,"#product-1 .cart_total_price")                 
    SECOND_TOTAL = (By.CSS_SELECTOR,"#product-2 .cart_total_price")     
    CHECK_OUT = (By.CSS_SELECTOR, "a.btn.btn-default.check_out")
    CHECKOUT_REGISTER = (By.LINK_TEXT, "Register / Login")
    DELIVERY_ADDRESS = (By.CSS_SELECTOR, "#address_delivery")
    ORDER_COMMENT = (By.NAME,"message")
    PLACE_ORDER = (By.CSS_SELECTOR, "a[href='/payment']")
    CONFIRM_PAY = (By.CSS_SELECTOR, "button[class='form-control btn btn-primary submit-button']")
    ORDER_CONFIRMATION = (By.CSS_SELECTOR, "h2[data-qa='order-placed']")
    ORDER_CONTINUE = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    NAME_ON_CARD = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXPIRY_MONTH = (By.NAME, "expiry_month")
    EXPIRY_YEAR = (By.NAME, "expiry_year")
    BILLING_ADDRESS = (By.CSS_SELECTOR, "#address_invoice")

    def __init__(self, driver):
     self.driver = driver
     self.wait = WebDriverWait(driver, 10)

    def product_header (self):
        return self.wait.until(
            EC.visibility_of_element_located(
               self.ALL_PRODUCTS_HEADING
            )
        )

    def product_list(self):
        return self.wait.until(
            EC.visibility_of_all_elements_located(
                self.PRODUCT_LIST
            )
        )

    def click_product(self):
        view_product = self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_PRODUCT
            )
        )
        view_product.click()

    def product_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_TITLE
            )
        )

    def product_details(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_INFORMATION
            )
        )

    def type_search(self, search):
        search_type = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BAR
            )
        )
        search_type.send_keys(search)

    def click_search(self):
        click_search_button = self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        )
        click_search_button.click()

    def search_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_HEADER
            )
        )

    def click_add_one(self):
        add_to_cart_one = self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_ONE
            )
        )
        add_to_cart_one.click()   
        
    def continue_shopping(self):
        click_continue = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_SHOP
            )
        )
        click_continue.click()   

    def click_add_two(self):
        add_to_cart_two = self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_TWO
            )
        )
        add_to_cart_two.click()   

    def view_cart(self):
        click_cart = self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_CART
            )
        )
        click_cart.click()  

    def product_one_details(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_DETAILS_ONE
            )
        )

    def product_two_details(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_DETAILS_TWO
            )
        )

    def price_one(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_PRICE
            )
        )

    def price_two(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.SECOND_PRICE
            )
        )
    
    def first_listing_price(self):
        return self.wait.until(
            EC.visibility_of_element_located(
            self.LISTING_PRICE_ONE
        )
    )

    def second_listing_price(self):
        return self.wait.until(
            EC.visibility_of_element_located(
            self.LISTING_PRICE_TWO
        )
    )

    def first_cart_quantity(self):
        return self.wait.until(
            EC.visibility_of_element_located(
            self.FIRST_QUANITY
        )
    )

    def second_cart_quantity(self):
        return self.wait.until(
            EC.visibility_of_element_located(
            self.SECOND_QUANITY
        )
    )
    
    def first_cart_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(
            self.FIRST_TOTAL
        )
    )

    def second_cart_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(
            self.SECOND_TOTAL
        )
    )

    def quantity_change(self, quantity):
        quantity_field = self.wait.until(
            EC.visibility_of_element_located(
                self.CHANGE_QUANTITY
            )
        )
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

    def quantity_check(self):
        return self.wait.until(
        EC.visibility_of_element_located(
            self.CHANGE_QUANTITY
        )
    )

    def add_cart(self):
        cart_add = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_CART
            )
        )
        cart_add.click()

    def proceed_checkout(self):
        click_proceed = self.wait.until(
            EC.element_to_be_clickable(
                self.CHECK_OUT
            )
        )
        click_proceed.click()

    def click_checkout_register(self):
        click_register = self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT_REGISTER
            )
        )
        click_register.click()


    def delivery_address(self):
        return self.wait.until(
        EC.visibility_of_element_located(
            self.DELIVERY_ADDRESS)
         )
    
    def billing_address(self):
        return self.wait.until(
        EC.visibility_of_element_located(
            self.BILLING_ADDRESS
        )
    )

    def comment_order(self, comment):
        type_comment = self.wait.until(
        EC.visibility_of_element_located(self.ORDER_COMMENT)
    )
        type_comment.clear()
        type_comment.send_keys(comment)

    def place_order(self):
        place_order_button = self.wait.until(
        EC.element_to_be_clickable(self.PLACE_ORDER)
    )
        place_order_button.click()

    def _type(self, locator, value):
        field = self.wait.until(
        EC.visibility_of_element_located(locator)
    )
        field.clear()
        field.send_keys(value)

    def fill_payment_information(
        self, *, name_on_card, card_number, cvc, expiry_month, expiry_year):
        self._type(self.NAME_ON_CARD, name_on_card)
        self._type(self.CARD_NUMBER, card_number)
        self._type(self.CVC, cvc)
        self._type(self.EXPIRY_MONTH, expiry_month)
        self._type(self.EXPIRY_YEAR, expiry_year)

    def confirm_payment(self):
        click_pay = self.wait.until(
            EC.element_to_be_clickable(
                self.CONFIRM_PAY
            )
        )
        click_pay.click()

    def order_confirmation(self):
        return self.wait.until(
        EC.visibility_of_element_located(self.ORDER_CONFIRMATION)
    )

    def continue_after_order(self):
        continue_button = self.wait.until(
        EC.element_to_be_clickable(self.ORDER_CONTINUE)
    )
        continue_button.click()
