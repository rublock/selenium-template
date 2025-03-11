from pages.main_page import MainPage

link = "https://www.advantageonlineshopping.com/#/"


def test_guest_can_see_laptops_list(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalog()
    page.should_be_laptops()
