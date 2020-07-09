from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a.btn.btn-default")
    NO_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner")
    MESSAGE_ABOUT_NO_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .basket-title.hidden-xs")
    ALL_BOOKS_LINK = (By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")
    PRODUCT_PAGE_LINK = (By.CSS_SELECTOR, ".col-xs-6.col-sm-4.col-md-3.col-lg-3:nth-child(4) a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_LOGIN_EMAIL = (By.CSS_SELECTOR, "input#id_login-username")
    INPUT_LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    INPUT_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    INPUT_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    INPUT_REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#id_registration-password2")
    BUTTON_REGISTRATION_SUBMIT = (By.CSS_SELECTOR, ".col-sm-6.register_form button.btn.btn-lg.btn-primary")
    BUTTON_LOGIN_SUBMIT = (By.CSS_SELECTOR, ".col-sm-6.login_form button.btn.btn-lg.btn-primary")

class ProductPageLocators():
    BUTTON_ADD_PRODUCT_TO_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    MESSAGE_AFTER_PRODUCT_ADD = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in strong")
