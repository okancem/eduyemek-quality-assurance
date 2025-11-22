from selenium.webdriver.common.by import By

class RegisterPage:
    first_name_id = "firstName"
    last_name_id = "lastName"
    email_id = "email"
    password_id = "password"
    submit_btn_id = "submitBtn"

    def  __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, firstName):
        self.driver.find_element(By.ID, self.first_name_id).clear()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(firstName)

    def enter_last_name(self, lastName):
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(lastName)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def create_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(By.ID, self.submit_btn_id).click()


