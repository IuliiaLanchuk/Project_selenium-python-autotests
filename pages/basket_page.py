from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket_1(self):
        no_products_in_basket = self.browser.find_element(*BasePageLocators.NO_PRODUCTS_IN_BASKET)
        assert "Items to buy now" not in no_products_in_basket.text, \
            "There are some products in basket, but they should not be there"
        print(no_products_in_basket.text)

    def should_be_message_about_no_products_in_basket(self):
        message_about_no_products_in_basket = self.browser.find_element(*BasePageLocators.MESSAGE_ABOUT_NO_PRODUCTS_IN_BASKET)
        assert "Your basket is empty" in message_about_no_products_in_basket.text, \
            "There is no message about empty basket, but it should be"
        print(message_about_no_products_in_basket.text)

#пара тестов с is_element_present и is_NOT_element_present. Проверка осуществляется в test_product_page.py
    def should_be_products_in_basket(self):   #positive
        assert self.is_element_present(*BasePageLocators.PRODUCTS_IN_BASKET), "There are no any products in basket"
    def should_not_be_products_in_basket_2(self):   #negative
        assert self.is_not_element_present(*BasePageLocators.PRODUCTS_IN_BASKET), "There are some products in basket"