import time

import pytest

from pages.cart_page import CartPage
from pages.checkout_finish import CheckoutFinish
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


#Essa tag mark serve para chamar o conftest (utilizando a tag, ele já utiliza a importação do webdriver usado no conftest)
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.cart
@pytest.mark.smoke
class TestAddProductsToCart:
    def test_add_products_to_cart(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        checkout_page = CheckoutPage()
        checkout_finish = CheckoutFinish()

        product_1 = "Sauce Labs Backpack"
        product_2 = "Sauce Labs Onesie"


        #  Fazendo login
        login_page.fazer_login("standard_user", "secret_sauce")


        #  Adicionando produto ao carrinho
        home_page.add_to_cart(product_1)

        home_page.access_cart()
        cart_page.check_if_product_exist_cart(product_1)

        cart_page.click_button_continue_shopping()

        #  Adicionando outro produto ao carrinho
        home_page.add_to_cart(product_2)

        home_page.access_cart()
        cart_page.check_if_product_exist_cart(product_1)
        cart_page.check_if_product_exist_cart(product_2)


        # Finalizando a compra
        cart_page.click_button_checkout()

        checkout_page.do_checkout("Karina", "Camargo", "1234-567")

        checkout_finish.finish_checkout()
