from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' is not in current url. Link is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password, password_confirm):
        self.email = email
        email = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_EMAIL)
        email.send_keys(str(time.time()) + "@fakemail.org")
        self.password = password
        password = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD)
        password.send_keys("m1n2b3v4c5!!")
        self.password_confirm = password_confirm
        password_confirm = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD_CONFIRM)
        password_confirm.send_keys("m1n2b3v4c5!!")
        button_registration_submit = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT)
        button_registration_submit.click()

    def login_user(self, email, password):
        self.email = email
        email = self.browser.find_element(*LoginPageLocators.INPUT_LOGIN_EMAIL)
        email.send_keys("lola1@mail.ru")
        self.password = password
        password = self.browser.find_element(*LoginPageLocators.INPUT_LOGIN_PASSWORD)
        password.send_keys("m1n2b3v4c5!!")
        button_login_submit = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN_SUBMIT)
        button_login_submit.click()