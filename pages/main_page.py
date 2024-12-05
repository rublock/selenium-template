from pages.base_page import BasePage
from pages.locators import BasePageLocators


class MainPage(BasePage):

    def go_to_catalog(self):
        self.browser.find_element(*BasePageLocators.CATALOG_LINK).click()

    def should_be_price_list(self):
        assert self.is_element_present(
            *BasePageLocators.PRICE_LIST_LINK
        ), "Нет ссылка на прайс-лист (.price_download)"
