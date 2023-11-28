import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


#Essa tag mark serve para chamar o conftest (utilizando a tag, ele já utiliza a importação do webdriver usado no conftest)
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLogin:
    def test_login(self):
        #instacia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()

        #faz login
        login_page.fazer_login("standard_user", "secret_sauce")

        #verifica se o login foi realizado
        home_page.check_successfull_login()



