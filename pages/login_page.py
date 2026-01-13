from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def go_to_login_page(self):
        self.driver.get(f'{BASE_URL}/account/login')
    
    def login(self, email: str, password: str):
        email_el = self.wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        email_el.clear()
        email_el.send_keys(email)

        password_el = self.wait.until(EC.visibility_of_element_located((By.ID, 'password')))
        password_el.clear()
        password_el.send_keys(password)

        self.wait.until(EC.element_to_be_clickable((By.ID, 'loginBtnText'))).click()

    def is_login_successful(self):
        self.wait.until(EC.url_contains('usermain'))
        return 'usermain' in self.driver.current_url
    
    def is_error_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.notification.error.show')
                )
            ).is_displayed()
    