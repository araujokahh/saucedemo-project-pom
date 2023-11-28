from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class CheckoutFinish(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.finish_button = (By.ID, "finish")

    def finish_checkout(self):
        self.click(self.finish_button)


