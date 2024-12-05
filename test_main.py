import time

from selenium.webdriver.common.by import By

from pages.main_page import MainPage

link = "https://termoshkaf.ru/"


def test_guest_can_see_price_list(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalog()
    page.should_be_price_list()
    time.sleep(5)
