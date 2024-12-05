import time

from selenium.webdriver.common.by import By

from pages.main_page import MainPage

link = "https://termoshkaf.ru/"


def test_guest_can_go_to_catalog(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalog()
    time.sleep(5)
