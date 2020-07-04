from pages.base_page import BasePage
from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link2 = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link2)
    product_page.open()
    product_page.add_product_to_basket() # выполняем метод страницы - добавляем товар в корзину
    product_page.solve_quiz_and_get_code()


def test_product_should_be_in_the_basket(browser):
    link2 = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link2)
    product_page.open()
    product_page.add_product_to_basket()  # выполняем метод страницы - добавляем товар в корзину
    product_page.solve_quiz_and_get_code()
    time.sleep(10)
    product_page.should_be_message_about_product_add()
    time.sleep(5)
    product_page.should_product_price_be_equal_to_basket_price()
    time.sleep(5)