from selenium.webdriver.common.by import By


class BasePageLocators:
    CATALOG_LINK = (By.XPATH, "//*[@id='laptopsImg']")


class LaptopPageLocators:
    LAPTOPS_BLOCK = (By.XPATH, "/html/body/div[3]/section/article/div[3]/div/div/div[2]/ul")
    LAPTOPS_ALL = (By.XPATH, "./*")
