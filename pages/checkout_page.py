from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def do_checkout(self, firstname, lastname, postalcode):
        self.write(self.first_name_field, firstname)
        self.write(self.last_name_field, lastname)
        self.write(self.postal_code_field, postalcode)
        self.click(self.continue_button)
