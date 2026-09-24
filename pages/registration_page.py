from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class RegistrationPage:
    ACCOUNT_INFORMATION_HEADING = (
        By.XPATH,
        "//h2[normalize-space()='Enter Account Information']",
    )
    TITLE_MR = (By.ID, "id_gender1")
    PASSWORD = (By.ID, "password")
    DAY = (By.ID, "days")
    MONTH = (By.ID, "months")
    YEAR = (By.ID, "years")
    NEWSLETTER = (By.ID, "newsletter")
    SPECIAL_OFFERS = (By.ID, "optin")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS_ONE = (By.ID, "address1")
    ADDRESS_TWO = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    LOGGED_IN_NAME = (
        By.XPATH,
        "//header//a[contains(normalize-space(.), 'Logged in as')]/b",
    )
    DELETE_ACCOUNT = (By.CSS_SELECTOR, "a[href='/delete_account']")
    ACCOUNT_DELETED = (By.CSS_SELECTOR, "h2[data-qa='account-deleted']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _type(self, locator, value):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _select(self, locator, value):
        dropdown = self.wait.until(EC.element_to_be_clickable(locator))
        Select(dropdown).select_by_value(value)

    def _set_checkbox(self, locator, checked):
        checkbox = self.wait.until(EC.element_to_be_clickable(locator))
        if checkbox.is_selected() != checked:
            checkbox.click()

    def account_information_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_INFORMATION_HEADING)
        )

    def select_title_mr(self):
        self._click(self.TITLE_MR)

    def fill_account_information(self, *, password, day, month, year):
        """Use numeric strings for the date, for example month='7' for July."""
        self._type(self.PASSWORD, password)
        self._select(self.DAY, day)
        self._select(self.MONTH, month)
        self._select(self.YEAR, year)

    def set_preferences(self, *, newsletter, special_offers):
        self._set_checkbox(self.NEWSLETTER, newsletter)
        self._set_checkbox(self.SPECIAL_OFFERS, special_offers)

    def fill_address_information(
        self, *, first_name, last_name, company, address1, address2,
        country, state, city, zipcode, mobile_number,
    ):
        self._type(self.FIRST_NAME, first_name)
        self._type(self.LAST_NAME, last_name)
        self._type(self.COMPANY, company)
        self._type(self.ADDRESS_ONE, address1)
        self._type(self.ADDRESS_TWO, address2)
        self._select(self.COUNTRY, country)
        self._type(self.STATE, state)
        self._type(self.CITY, city)
        self._type(self.ZIPCODE, zipcode)
        self._type(self.MOBILE_NUMBER, mobile_number)

    def create_account(self):
        self._click(self.CREATE_ACCOUNT)

    def account_created_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_CREATED)
        )

    def click_continue(self):
        self._click(self.CONTINUE)

    def logged_in_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN_NAME)
        )

    def delete_account(self):
        """Delete the currently signed-in account; call only for test-owned users."""
        self._click(self.DELETE_ACCOUNT)

    def account_deleted_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_DELETED)
        )
