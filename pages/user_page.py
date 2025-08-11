from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserPage:
    def __init__(self, driver):
        self.driver = driver

    def select_restaurant(self, restaurant_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), '{restaurant_name}')] | //span[contains(text(), '{restaurant_name}')] | //h1[contains(text(), '{restaurant_name}')] | //h2[contains(text(), '{restaurant_name}')] | //h3[contains(text(), '{restaurant_name}')]"))
        )

        xpath_selector = f"//div[contains(text(), '{restaurant_name}')] | //span[contains(text(), '{restaurant_name}')] | //h1[contains(text(), '{restaurant_name}')] | //h2[contains(text(), '{restaurant_name}')] | //h3[contains(text(), '{restaurant_name}')]"
        self.driver.find_element(By.XPATH, xpath_selector).click()

    def select_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ana-ürünler"]/div/div'))
        )

        self.driver.find_element(By.XPATH, '//*[@id="ana-ürünler"]/div/div').click()

    def customization_page_increase_quantity(self):
        self.driver.find_element(By.XPATH, '//*[@id="increaseQuantity"]').click()

    def add_to_basket(self):
        self.driver.find_element(By.XPATH, '//*[@id="addToBasketBtn"]').click()

