import time

import pytest

from utils.driver_setup import get_driver

from config.config import (
    URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


# ============================================================
# DRIVER FIXTURE
# ============================================================

@pytest.fixture
def driver():

    driver = get_driver()

    yield driver

    driver.quit()


# ============================================================
# LOGIN FIXTURE
# ============================================================

@pytest.fixture
def logout_page(driver):

    # --------------------------------------------------------
    # Open Login Page
    # --------------------------------------------------------

    driver.get(URL)

    time.sleep(2)

    # --------------------------------------------------------
    # Login
    # --------------------------------------------------------

    login = LoginPage(driver)

    login.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    # --------------------------------------------------------
    # Wait until login is completed
    # --------------------------------------------------------

    from selenium.webdriver.support.ui import WebDriverWait

    wait = WebDriverWait(driver, 20)

    wait.until(
        lambda d: "login" not in d.current_url
    )

    time.sleep(2)

    print(
        "After login URL:",
        driver.current_url
    )

    # --------------------------------------------------------
    # Create Logout Page
    # --------------------------------------------------------

    logout = LogoutPage(driver)

    return logout


# ============================================================
# LOGOUT TEST
# ============================================================

def test_logout_successfully(logout_page):

    # --------------------------------------------------------
    # Click Logout
    # --------------------------------------------------------

    logout_page.click_logout()

    # --------------------------------------------------------
    # Verify user is logged out
    # --------------------------------------------------------

    assert logout_page.is_logged_out()

    time.sleep(2)