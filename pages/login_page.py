from selenium.webdriver.common.by import By

class LoginPage:
    email_input_id = "email"
    password_input_id = "password"
    login_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_input_id).clear()
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_input_id).clear()
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

