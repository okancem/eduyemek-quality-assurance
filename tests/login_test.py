import pytest
from pages.login_page import LoginPage
from data.credentials import VALID_USER, INVALID_USERS

@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(VALID_USER['email'], VALID_USER['password']) 
    assert login_page.is_login_successful()

@pytest.mark.regression
@pytest.mark.parametrize('user', INVALID_USERS)
def test_invalid_login_shows_error(driver, user):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(user['email'], user['password'])
    assert login_page.is_error_displayed()
