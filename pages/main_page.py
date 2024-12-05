from pages.base_page import BasePage
from pages.locators import BasePageLocators


class MainPage(BasePage):

    def go_to_catalog(self):
        self.browser.find_element(*BasePageLocators.CATALOG_LINK).click()
