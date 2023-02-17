from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_product_page_article()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is " \
                                                                                   "missing "

    def should_be_product_page_article(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PAGE_ARTICLE), "Product page article is " \
                                                                                   "missing "

    def should_be_title_in_message(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_TITLE_IN_MESSAGE), "No title in message"

    def should_be_price_in_message(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_IM_MESSAGE), "No price in message"

    def should_be_same_book_title(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text == \
               self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_MESSAGE).text, "different book titles"

    def should_be_same_book_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IM_MESSAGE).text, "different book prices"
