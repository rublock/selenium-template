import time

from selenium.webdriver.common.by import By

link = "https://termoshkaf.ru/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.XPATH, "//span[text()='Каталог']").click()
    time.sleep(5)
