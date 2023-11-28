from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_from_home_page = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.button_continue_shopping = (By.ID, "continue-shopping")
        self.button_checkout = (By.ID, "checkout")


    def check_if_product_exist_cart(self, item_name):
        item = (self.item_from_home_page[0], self.item_from_home_page[1].format(item_name))
        self.check_if_element_exist(item)

    def click_button_continue_shopping(self):
        self.click(self.button_continue_shopping)

    def click_button_checkout(self):
        self.click(self.button_checkout)
