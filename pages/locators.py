from selenium.webdriver.common.by import By


class BasePageLocators:
    CATALOG_LINK = (By.XPATH, "//span[text()='Каталог']")
    PRICE_LIST_LINK = (By.CSS_SELECTOR, ".price_download")
