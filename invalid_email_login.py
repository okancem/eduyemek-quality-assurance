from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://eduyemek.com/account/login')

wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_element_located((By.ID, 'email'))).send_keys('invalidemail@itu.edu.tr')

wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys('password')

wait.until(EC.element_to_be_clickable((By.ID, 'loginBtn'))).click()

assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.error.show')))

driver.quit()