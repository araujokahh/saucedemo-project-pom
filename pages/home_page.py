from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_home_page = (By.XPATH, "//span[@class='title']")
        self.item_from_home_page = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']")
        self.cart = (By.XPATH, "//*[text()='Add to cart']")
        self.cart_icon = (By.XPATH, "//*[@class='shopping_cart_badge']")

    def check_successfull_login(self):
        self.check_if_element_exist(self.title_home_page)

    def add_to_cart(self, item_name):
        item = (self.item_from_home_page[0], self.item_from_home_page[1].format(item_name))
        self.click(item)
        self.click(self.cart)

    def access_cart(self):
        self.click(self.cart_icon)





