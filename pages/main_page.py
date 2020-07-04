from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


#класс  MainPage - наследник класса BasePage(Класс-предок в Python указывается в скобках).
#класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка

class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

#В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. 
#Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса: 
