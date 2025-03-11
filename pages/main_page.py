import time

from pages.base_page import BasePage
from pages.locators import BasePageLocators, LaptopPageLocators


class MainPage(BasePage):

    def go_to_catalog(self):
        self.browser.find_element(*BasePageLocators.CATALOG_LINK).click()

    def should_be_laptops(self):
        laptops = self.browser.find_element(*LaptopPageLocators.LAPTOPS_BLOCK)
        assert len(laptops.find_elements(*LaptopPageLocators.LAPTOPS_ALL)) == 11, 'Неверное количество ноутбуков'
