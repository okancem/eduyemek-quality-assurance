import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig

class TestLogin:
    login_url = ReadConfig.get_login_page_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    invalid_email = ReadConfig.get_invalid_email()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.login_url)

        self.login_page = LoginPage(self.driver)
        self.login_page.enter_email(self.email)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()

        filter_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".filter-main-title"))
        ).text

        if filter_title == "Filtrele":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_login_failed.png")
            assert False

        self.driver.close()

    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.get(self.login_url)

        self.login_page = LoginPage(self.driver)
        self.login_page.enter_email(self.invalid_email)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_button()

        notification_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".notification.error.show"))
        ).text

        if notification_text == "Geçersiz bilgiler":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_login_failed.png")
            assert False

        self.driver.close()

