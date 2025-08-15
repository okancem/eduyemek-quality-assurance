import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.user_page import UserPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogMaker

class TestUser:
    login_url = ReadConfig.get_login_page_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    restaurant_name = ReadConfig.get_restaurant_name()
    logger = LogMaker.log_gen()

    def test_add_to_basket(self, setup):
        self.logger.info("*************test_add_to_basket function started*************")
        self.driver = setup
        self.driver.get(self.login_url)

        self.login_page = LoginPage(self.driver)
        self.login_page.enter_email(self.email)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()

        self.user_page = UserPage(self.driver)
        self.user_page.select_restaurant(self.restaurant_name)

        self.user_page.select_menu()
        self.user_page.customization_page_increase_quantity()
        self.user_page.add_to_basket()

        successfully_added_to_basket = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ürün sepete eklendi')]"))
        ).text

        if successfully_added_to_basket == "Ürün sepete eklendi":
            self.logger.info("*************test_add_to_basket function passed*************")
            assert True
        else:
            self.logger.info("*************test_add_to_basket function failed*************")
            self.driver.save_screenshot(".\\screenshots\\test_add_to_basket_failed.png")
            assert False

        self.driver.close()


