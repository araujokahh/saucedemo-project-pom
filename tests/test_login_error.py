import pytest
from pages.login_page import LoginPage


#Essa tag mark serve para chamar o conftest (utilizando a tag, ele já utiliza a importação do webdriver usado no conftest)
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLoginError:
    def test_login_error(self):
        expected_message = "Epic sadface: Username and password do not match any user in this service"
       # instacia os objetos a serem usados no teste
        login_page = LoginPage()


        # faz login
        login_page.fazer_login("standard_user", "zzzzzz")

        #verifica se o login não foi realizado e a mensagem de erro apareceu
        login_page.check_error_message()
        login_page.check_text_mesage_error_login(expected_message)


