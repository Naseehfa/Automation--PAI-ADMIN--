
import time

import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


# ============================================================
# TEST DATA
# ============================================================

VALID_EMAIL = "admin@pineappleai.com"

VALID_PASSWORD = "SecureAdmin123!"

INVALID_EMAIL = "wrong@email.com"

INVALID_PASSWORD = "wrong123"

UNREGISTERED_EMAIL = "unregistereduser@example.com"

INVALID_EMAIL_FORMAT = "invalidemail"

EMAIL_WITH_SPACES = "  admin@pineappleai.com  "

SPACES_ONLY = "     "

EXCESSIVELY_LONG_EMAIL = (
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    "@example.com"
)


# ============================================================
# URLS
# ============================================================

LOGIN_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/login"
)

TEAM_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/team"
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def click_eye_and_remember(login_page):
    """
    Perform the common required actions:
    1. Click eye icon.
    2. Select Remember Me.
    """

    login_page.click_eye_button()

    login_page.click_remember_me()

    assert login_page.is_remember_me_selected(), (
        "FAIL: Remember Me checkbox was not selected."
    )


def assert_login_failed(driver):
    """
    Verify that login did not navigate to Team page.
    """

    time.sleep(2)

    assert driver.current_url != TEAM_URL, (
        "FAIL: Login was accepted when it should have failed."
    )


# ============================================================
# TEST 01
# Verify Login Page is displayed
# ============================================================

def test_login_page_displayed(driver):

    print(
        "\nTEST 01: Verify Login Page is displayed"
    )

    login_page = LoginPage(driver)

    assert login_page.is_login_page_displayed(), (
        "FAIL: Login page is not displayed."
    )

    print(
        "PASS: Login page is displayed."
    )


# ============================================================
# TEST 02
# Verify Login button is displayed
# ============================================================

def test_login_button_displayed(driver):

    print(
        "\nTEST 02: Verify Login button is displayed"
    )

    login_page = LoginPage(driver)

    assert login_page.is_login_button_displayed(), (
        "FAIL: Login button is not displayed."
    )

    print(
        "PASS: Login button is displayed."
    )


# ============================================================
# TEST 03
# Verify Login button is enabled
# ============================================================

def test_login_button_enabled(driver):

    print(
        "\nTEST 03: Verify Login button is enabled"
    )

    login_page = LoginPage(driver)

    assert login_page.is_login_button_enabled(), (
        "FAIL: Login button is not enabled."
    )

    print(
        "PASS: Login button is enabled."
    )


# ============================================================
# TEST 04
# Verify valid email can be entered
# ============================================================

def test_enter_valid_email(driver):

    print(
        "\nTEST 04: Verify valid email can be entered"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        VALID_EMAIL
    )

    actual_email = (
        login_page.get_email_value()
    )

    assert actual_email == VALID_EMAIL, (
        f"FAIL: Email was not entered correctly.\n"
        f"Expected: {VALID_EMAIL}\n"
        f"Actual: {actual_email}"
    )

    print(
        "PASS: Valid email entered."
    )


# ============================================================
# ============================================================
# TEST 05
# Verify valid password can be entered and shown
# ============================================================

def test_enter_valid_password(driver):

    print(
        "\nTEST 05: Verify valid password can be entered "
        "and shown"
    )

    login_page = LoginPage(driver)

    # --------------------------------------------------------
    # STEP 1: Enter valid password
    # --------------------------------------------------------

    login_page.enter_password(
        VALID_PASSWORD
    )

    # --------------------------------------------------------
    # STEP 2: Verify password was entered correctly
    # --------------------------------------------------------

    actual_password = (
        login_page.get_password_value()
    )

    assert actual_password == VALID_PASSWORD, (
        "FAIL: Password was not entered correctly.\n"
        f"Expected: {VALID_PASSWORD}\n"
        f"Actual: {actual_password}"
    )

    print(
        "PASS: Valid password entered."
    )

    # --------------------------------------------------------
    # STEP 3: Verify password is initially masked
    # --------------------------------------------------------

    assert login_page.is_password_masked(), (
        "FAIL: Password is not masked initially."
    )

    print(
        "PASS: Password is initially masked."
    )

    # --------------------------------------------------------
    # STEP 4: Click eye icon
    # --------------------------------------------------------

    login_page.click_eye_button()

    print(
        "PASS: Eye icon clicked."
    )

    # --------------------------------------------------------
    # STEP 5: Verify password is visible
    # --------------------------------------------------------

    assert login_page.is_password_visible(), (
        "FAIL: Password did not become visible "
        "after clicking eye icon."
    )

    print(
        "PASS: Password became visible after "
        "clicking eye icon."
    )
# ============================================================
# TEST 06
# Verify Remember Me checkbox can be selected
# ============================================================

def test_remember_me_can_be_selected(driver):

    print(
        "\nTEST 06: Verify Remember Me checkbox can be selected"
    )

    login_page = LoginPage(driver)

    login_page.click_remember_me()

    assert login_page.is_remember_me_selected(), (
        "FAIL: Remember Me checkbox was not selected."
    )

    print(
        "PASS: Remember Me checkbox selected."
    )




# ============================================================
# TEST 08
# Verify admin can log in with valid credentials
# ============================================================

def test_valid_login(driver):

    print(
        "\nTEST 08: Verify admin can log in with valid credentials"
    )

    login_page = LoginPage(driver)

    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    assert login_page.is_team_page_displayed(), (
        f"FAIL: Valid login did not navigate to Team page.\n"
        f"Expected: {TEAM_URL}\n"
        f"Actual: {driver.current_url}"
    )

    assert driver.current_url == TEAM_URL, (
        f"FAIL: Incorrect URL after valid login.\n"
        f"Expected: {TEAM_URL}\n"
        f"Actual: {driver.current_url}"
    )

    print(
        "PASS: Admin logged in successfully."
    )

    print(
        "PASS: User navigated to Team page."
    )




# ============================================================
# TEST 10
# Verify login with valid email and invalid password
# ============================================================

def test_valid_email_invalid_password(driver):

    print(
        "\nTEST 10: Verify login with valid email "
        "and invalid password"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        VALID_EMAIL
    )

    login_page.enter_password(
        INVALID_PASSWORD
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    assert_login_failed(driver)

    print(
        "PASS: Invalid password was rejected."
    )


# ============================================================
# TEST 11
# Verify login with unregistered email
# ============================================================

def test_unregistered_email(driver):

    print(
        "\nTEST 11: Verify login with unregistered email"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        UNREGISTERED_EMAIL
    )

    login_page.enter_password(
        VALID_PASSWORD
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    assert_login_failed(driver)

    print(
        "PASS: Unregistered email was rejected."
    )


# ============================================================
# TEST 12
# Verify login with invalid email
# ============================================================

def test_invalid_email(driver):

    print(
        "\nTEST 12: Verify login with invalid email"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        INVALID_EMAIL
    )

    login_page.enter_password(
        VALID_PASSWORD
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    assert_login_failed(driver)

    print(
        "PASS: Invalid email was rejected."
    )


# ============================================================
# TEST 13
# Verify login with invalid email and invalid password
# ============================================================

def test_invalid_email_and_password(driver):

    print(
        "\nTEST 13: Verify login with invalid email "
        "and invalid password"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        INVALID_EMAIL
    )

    login_page.enter_password(
        INVALID_PASSWORD
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    assert_login_failed(driver)

    print(
        "PASS: Invalid credentials were rejected."
    )


# ============================================================
# TEST 14
# Verify login with both email and password empty
# ============================================================

def test_empty_email_and_password(driver):

    print(
        "\nTEST 14: Verify login with both "
        "email and password fields empty"
    )

    login_page = LoginPage(driver)

    login_page.clear_email()

    login_page.clear_password()

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    time.sleep(1)

    assert login_page.is_login_page_displayed(), (
        "FAIL: Login page did not remain displayed."
    )

    assert driver.current_url != TEAM_URL, (
        "FAIL: Empty credentials were accepted."
    )

    print(
        "PASS: Empty email and password were rejected."
    )


# ============================================================
# TEST 15
# Verify login with empty email
# ============================================================

def test_empty_email(driver):

    print(
        "\nTEST 15: Verify login with empty email"
    )

    login_page = LoginPage(driver)

    login_page.clear_email()

    login_page.enter_password(
        VALID_PASSWORD
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    assert_login_failed(driver)

    print(
        "PASS: Empty email was rejected."
    )


# ============================================================
# TEST 16
# Verify login with empty password
# ============================================================

def test_empty_password(driver):

    print(
        "\nTEST 16: Verify login with empty password"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        VALID_EMAIL
    )

    login_page.clear_password()

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    assert_login_failed(driver)

    print(
        "PASS: Empty password was rejected."
    )


# ============================================================
# TEST 17
# Verify Login button behavior when required fields empty
# ============================================================

def test_login_button_behavior_when_fields_empty(
    driver
):

    print(
        "\nTEST 17: Verify Login button behavior "
        "when required fields are empty"
    )

    login_page = LoginPage(driver)

    login_page.clear_email()

    login_page.clear_password()

    assert login_page.is_login_button_displayed(), (
        "FAIL: Login button is not displayed."
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    time.sleep(1)

    assert login_page.is_login_page_displayed(), (
        "FAIL: Login page did not remain displayed."
    )

    assert driver.current_url != TEAM_URL, (
        "FAIL: Empty required fields were accepted."
    )

    print(
        "PASS: Login button did not allow "
        "empty-field login."
    )


# ============================================================
# TEST 18
# Verify login page remains stable after repeated
# Login button clicks
# ============================================================

def test_repeated_login_button_clicks(driver):

    print(
        "\nTEST 18: Verify login page remains stable "
        "after repeated Login button clicks"
    )

    login_page = LoginPage(driver)

    login_page.clear_email()

    login_page.clear_password()

    click_eye_and_remember(
        login_page
    )

    for attempt in range(3):

        print(
            f"Login button click attempt "
            f"{attempt + 1}"
        )

        try:
            login_page.click_login()

        except Exception as error:

            pytest.fail(
                f"FAIL: Login button failed on "
                f"attempt {attempt + 1}: {error}"
            )

        time.sleep(0.5)

    assert login_page.is_login_page_stable(), (
        "FAIL: Login page became unstable "
        "after repeated Login button clicks."
    )

    assert driver.current_url != TEAM_URL, (
        "FAIL: Empty credentials were accepted."
    )

    print(
        "PASS: Login page remained stable."
    )


# ============================================================
# TEST 19
# Verify email format validation
# ============================================================

def test_email_format_validation(driver):

    print(
        "\nTEST 19: Verify email format validation"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        INVALID_EMAIL_FORMAT
    )

    login_page.enter_password(
        VALID_PASSWORD
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    time.sleep(1)

    assert driver.current_url != TEAM_URL, (
        "FAIL: Invalid email format was accepted."
    )

    validation_message = (
        login_page.get_email_validation_message()
    )

    if validation_message:

        print(
            "PASS: Browser email validation "
            "message displayed."
        )

    else:

        print(
            "PASS: Invalid email format did not "
            "authenticate."
        )


# ============================================================
# TEST 20
# Verify login with leading/trailing spaces in email
# ============================================================

def test_email_with_leading_trailing_spaces(
    driver
):

    print(
        "\nTEST 20: Verify login with leading "
        "or trailing spaces in email"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        EMAIL_WITH_SPACES
    )

    login_page.enter_password(
        VALID_PASSWORD
    )

    actual_email = (
        login_page.get_email_value()
    )

    print(
        f"Email entered: '{actual_email}'"
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    time.sleep(2)

    if driver.current_url == TEAM_URL:

        print(
            "INFO: Application trims the leading/"
            "trailing spaces and accepted login."
        )

    else:

        print(
            "PASS: Email with leading/trailing "
            "spaces was rejected."
        )


# ============================================================
# TEST 21
# Verify login with excessively long email
# ============================================================

def test_excessively_long_email(driver):

    print(
        "\nTEST 21: Verify login with excessively "
        "long email input"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        EXCESSIVELY_LONG_EMAIL
    )

    login_page.enter_password(
        VALID_PASSWORD
    )

    actual_email = (
        login_page.get_email_value()
    )

    print(
        f"Entered email length: {len(actual_email)}"
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    assert_login_failed(driver)

    print(
        "PASS: Excessively long email "
        "was not accepted."
    )


# ============================================================
# TEST 22
# Verify login behavior after spaces-only input
# ============================================================

def test_spaces_only_in_required_fields(driver):

    print(
        "\nTEST 22: Verify login behavior after "
        "entering only spaces in required fields"
    )

    login_page = LoginPage(driver)

    login_page.enter_email(
        SPACES_ONLY
    )

    login_page.enter_password(
        SPACES_ONLY
    )

    assert login_page.get_email_value() == SPACES_ONLY, (
        "FAIL: Spaces-only email was not entered."
    )

    assert login_page.get_password_value() == SPACES_ONLY, (
        "FAIL: Spaces-only password was not entered."
    )

    click_eye_and_remember(
        login_page
    )

    login_page.click_login()

    assert_login_failed(driver)

    print(
        "PASS: Spaces-only credentials were rejected."
    )


# ============================================================
# TEST 23
# Verify password remains masked
# ============================================================

def test_password_remains_masked(driver):

    print(
        "\nTEST 23: Verify password remains masked"
    )

    login_page = LoginPage(driver)

    login_page.enter_password(
        VALID_PASSWORD
    )

    assert login_page.is_password_masked(), (
        "FAIL: Password is not masked."
    )

    print(
        "PASS: Password is masked."
    )


# ============================================================
# TEST 25
# Verify login page layout at 1920x1080
# ============================================================

def test_login_page_1920x1080(driver):

    print(
        "\nTEST 25: Verify login page layout "
        "at 1920x1080"
    )

    login_page = LoginPage(driver)

    login_page.set_window_size(
        1920,
        1080
    )

    time.sleep(1)

    assert login_page.is_login_page_stable(), (
        "FAIL: Login page is not stable "
        "at 1920x1080."
    )

    print(
        "PASS: Login page stable at 1920x1080."
    )


# ============================================================
# TEST 26
# Verify login page layout at 1366x768
# ============================================================

def test_login_page_1366x768(driver):

    print(
        "\nTEST 26: Verify login page layout "
        "at 1366x768"
    )

    login_page = LoginPage(driver)

    login_page.set_window_size(
        1366,
        768
    )

    time.sleep(1)

    assert login_page.is_login_page_stable(), (
        "FAIL: Login page is not stable "
        "at 1366x768."
    )

    print(
        "PASS: Login page stable at 1366x768."
    )


# ============================================================
# TEST 27
# Verify login page layout at 1024x768
# ============================================================

def test_login_page_1024x768(driver):

    print(
        "\nTEST 27: Verify login page layout "
        "at 1024x768"
    )

    login_page = LoginPage(driver)

    login_page.set_window_size(
        1024,
        768
    )

    time.sleep(1)

    assert login_page.is_login_page_stable(), (
        "FAIL: Login page is not stable "
        "at 1024x768."
    )

    print(
        "PASS: Login page stable at 1024x768."
    )


