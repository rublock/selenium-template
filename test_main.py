import time

from selenium.webdriver.common.by import By

link = "https://www.advantageonlineshopping.com/#/category/Laptops/1"


def test_count_products_on_page(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    review_block = browser.find_element(
        By.XPATH, "/html/body/div[3]/section/article/div[3]/div/div/div[2]/ul"
    )
    reviews = review_block.find_elements(By.XPATH, "./*")
    time.sleep(5)  # human verify
    assert len(reviews) == 11
