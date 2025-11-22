from pages.register_page import RegisterPage
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogMaker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestRegister:
    register_url = "https://eduyemek.com/account/register"
    firstName = "fName Test 01"
    lastName = "lName Test 01"
    email = "test01@itu.edu.tr"
    newPassword = "test0101"
    logger = LogMaker.log_gen()

    def test_register(self, setup):
        self.logger.info("*************test_register function started*************")

        self.driver = setup
        self.driver.get(self.register_url)
        self.register_page = RegisterPage(self.driver)

        self.register_page.enter_first_name(self.firstName)
        self.register_page.enter_last_name(self.lastName)
        self.register_page.enter_email(self.email)
        self.register_page.create_password(self.newPassword)
        self.register_page.click_submit_button()

        succesfully_registered = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".filter-main-title"))
        )

        self.driver.close()