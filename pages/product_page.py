from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_product_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_PRODUCT_TO_BASKET)
        button_product_to_basket.click()

    def should_be_message_about_product_add(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_after_product_add = self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_PRODUCT_ADD)
        assert product_name.text in message_after_product_add.text, "No product in the basket"

    def should_product_price_be_equal_to_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price.text in basket_price.text, "Basket price not equal to product price"