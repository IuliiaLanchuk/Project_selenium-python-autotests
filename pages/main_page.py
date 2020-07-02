from .base_page import BasePage
from selenium.webdriver.common.by import By
#импорт базового класса BasePage

#класс  MainPage - наследник класса BasePage(Класс-предок в Python указывается в скобках).класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка
class MainPage(BasePage): 
	def go_to_login_page(self):
		login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
		login_link.click()

#В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. 
#Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса: 
