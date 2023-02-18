from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "'Basket' is not in URL"

    def should_be_basket_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_PAGE_HEADER), "No header Корзина"

    def should_be_message_no_products(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NO_PRODUCTS_MESSAGE), "No message 'Basket is empty'"

    def should_not_be_basket_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FIRST_PRODUCT), "Product is presented in " \
                                                                                      "basket, but should be missing "


