from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):

    # construtor da classe
    def __init__(self):
        self.driver = conftest.driver
        #aqui no contrutor da classe definiremos os locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_login = (By.XPATH, "//*[@data-test='error']")

    #aqui colocamos o "*self + variável" como os parâmentros. precisa do * para chamar o primeiro parâmetro (By.ID e o self por estar em outro metodo
    def fazer_login(self, username, password):
        self.write(self.username_field, username)
        self.write(self.password_field, password)
        self.click(self.login_button)

    def check_error_message(self):
        self.check_if_element_exist(self.error_login)

    #verifica o conteúdo do texto
    def check_text_mesage_error_login(self, expected_text):
        finded_text = self.take_text_element(self.error_login)
        assert finded_text == expected_text, f"O texto encontrado foi '{finded_text}', mas era esperado '{expected_text}'."

