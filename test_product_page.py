import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

#def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #product_page = ProductPage(browser, link)
    #product_page.open()
    #product_page.add_product_to_basket()

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  #pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])                                #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#def test_product_should_be_in_the_basket(browser, link):
    #product_page = ProductPage(browser, link)
    #product_page.open()
    #product_page.add_product_to_basket()
    #product_page.solve_quiz_and_get_code()
    #product_page.should_be_message_about_product_add()
    #product_page.should_product_price_be_equal_to_basket_price()

#@pytest.mark.xfail
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #product_page = ProductPage(browser, link)
    #product_page.open()
    #product_page.add_product_to_basket()
    #product_page.should_not_be_success_message_after_adding_product_to_basket()

#def test_guest_cant_see_success_message(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #product_page = ProductPage(browser, link)
    #product_page.open()
    #product_page.should_not_be_success_message_after_adding_product_to_basket()

#@pytest.mark.xfail
#def test_message_disappeared_after_adding_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #product_page = ProductPage(browser, link)
    #product_page.open()
    #product_page.add_product_to_basket()
    #product_page.should_not_be_success_message_after_adding_product_to_basket_2()

#def test_guest_should_see_login_link_on_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #page = ProductPage(browser, link)
    #page.open()
    #page.should_be_login_link()

#def test_guest_can_go_to_login_page_from_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #page = ProductPage(browser, link)
    #page.open()
    #page.go_to_login_page()
    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page_positive_test(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket_2()
    basket_page.should_be_message_about_no_products_in_basket()

def test_guest_cant_see_product_in_basket_opened_from_product_page_negative_test(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_products_in_basket()