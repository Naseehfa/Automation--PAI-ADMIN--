
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    """
    Page Object Model for the PAI Admin Login page.
    """

    # ============================================================
    # LOCATORS
    # ============================================================

    EMAIL = (
        By.XPATH,
        '//*[@id="email"]'
    )

    PASSWORD = (
        By.XPATH,
        '//*[@id="password"]'
    )

    EYE_BUTTON = (
        By.XPATH,
        '/html/body/div/div/div[2]/form/div[2]/button'
    )

    REMEMBER_ME = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/form/div[3]/label/input'
    )

    LOGIN_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/form/button'
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
    # WAIT TIME
    # ============================================================

    WAIT_TIME = 20

    # ============================================================
    # CONSTRUCTOR
    # ============================================================

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            self.WAIT_TIME
        )

    # ============================================================
    # PAGE NAVIGATION
    # ============================================================

    def open_login_page(self):
        """
        Open the login page and wait for the email field.
        """

        self.driver.get(self.LOGIN_URL)

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        )

    def go_to_login_page(self):
        """
        Return to the login page.
        """

        self.open_login_page()

    # ============================================================
    # EMAIL
    # ============================================================

    def enter_email(self, email):
        """
        Enter email address.
        """

        email_field = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        )

        email_field.click()
        email_field.clear()

        if email is not None:
            email_field.send_keys(email)

    def clear_email(self):
        """
        Clear email field.
        """

        email_field = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        )

        email_field.click()
        email_field.clear()

    def get_email_value(self):
        """
        Return current email field value.
        """

        email_field = self.wait.until(
            EC.presence_of_element_located(
                self.EMAIL
            )
        )

        return email_field.get_attribute("value")

    # ============================================================
    # PASSWORD
    # ============================================================

    def enter_password(self, password):
        """
        Enter password.
        """

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        )

        password_field.click()
        password_field.clear()

        if password is not None:
            password_field.send_keys(password)

    def clear_password(self):
        """
        Clear password field.
        """

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        )

        password_field.click()
        password_field.clear()

    def get_password_value(self):
        """
        Return current password field value.
        """

        password_field = self.wait.until(
            EC.presence_of_element_located(
                self.PASSWORD
            )
        )

        return password_field.get_attribute("value")

    # ============================================================
    # PASSWORD TYPE
    # ============================================================

    def get_password_input_type(self):
        """
        Return password input type.

        Expected:
            password -> masked
            text     -> visible
        """

        password_field = self.wait.until(
            EC.presence_of_element_located(
                self.PASSWORD
            )
        )

        return password_field.get_attribute("type")

    def is_password_masked(self):
        """
        Check whether password is masked.
        """

        return (
            self.get_password_input_type()
            == "password"
        )

    def is_password_visible(self):
        """
        Check whether password is visible.
        """

        return (
            self.get_password_input_type()
            == "text"
        )

    # ============================================================
    # SHOW PASSWORD
    # ============================================================

    def click_eye_button(self):
        """
        Click password eye/show-password button.
        """

        eye_button = self.wait.until(
            EC.element_to_be_clickable(
                self.EYE_BUTTON
            )
        )

        eye_button.click()

    # ============================================================
    # REMEMBER ME
    # ============================================================

    def click_remember_me(self):
        """
        Select Remember Me if it is not already selected.
        """

        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                self.REMEMBER_ME
            )
        )

        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_remember_me(self):
        """
        Unselect Remember Me if it is selected.
        """

        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                self.REMEMBER_ME
            )
        )

        if checkbox.is_selected():
            checkbox.click()

    def is_remember_me_selected(self):
        """
        Check whether Remember Me is selected.
        """

        checkbox = self.wait.until(
            EC.presence_of_element_located(
                self.REMEMBER_ME
            )
        )

        return checkbox.is_selected()

    # ============================================================
    # LOGIN BUTTON
    # ============================================================

    def click_login(self):
        """
        Click Login button.
        """

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        )

        login_button.click()

    def is_login_button_displayed(self):
        """
        Check whether Login button is displayed.
        """

        try:
            return self.wait.until(
                EC.visibility_of_element_located(
                    self.LOGIN_BUTTON
                )
            ).is_displayed()

        except TimeoutException:
            return False

    def is_login_button_enabled(self):
        """
        Check whether Login button is enabled.
        """

        try:
            return self.wait.until(
                EC.presence_of_element_located(
                    self.LOGIN_BUTTON
                )
            ).is_enabled()

        except TimeoutException:
            return False

    # ============================================================
    # LOGIN
    # ============================================================

    def login(self, email, password):
        """
        Complete login process.

        Steps:
        1. Enter email
        2. Enter password
        3. Click eye icon
        4. Select Remember Me
        5. Click Login
        """

        self.enter_email(email)

        self.enter_password(password)

        self.click_eye_button()

        self.click_remember_me()

        self.click_login()

    # ============================================================
    # EMPTY LOGIN
    # ============================================================

    def login_with_empty_fields(self):
        """
        Attempt login with both fields empty.
        """

        self.clear_email()

        self.clear_password()

        self.click_eye_button()

        self.click_remember_me()

        self.click_login()

    # ============================================================
    # PAGE CHECKS
    # ============================================================

    def is_login_page_displayed(self):
        """
        Check whether login page is displayed.
        """

        try:
            return self.wait.until(
                EC.visibility_of_element_located(
                    self.EMAIL
                )
            ).is_displayed()

        except TimeoutException:
            return False

    def is_team_page_displayed(self):
        """
        Check whether navigation reached Team page.
        """

        try:
            self.wait.until(
                EC.url_to_be(
                    self.TEAM_URL
                )
            )

            return True

        except TimeoutException:
            return False

    def is_not_team_page(self):
        """
        Check that user was not redirected to Team page.
        """

        return self.driver.current_url != self.TEAM_URL

    # ============================================================
    # VALIDATION MESSAGE
    # ============================================================

    def get_email_validation_message(self):
        """
        Get browser HTML validation message for email.
        """

        try:
            email_field = self.driver.find_element(
                *self.EMAIL
            )

            return (
                email_field.get_attribute(
                    "validationMessage"
                )
                or ""
            )

        except Exception:
            return ""

    def get_password_validation_message(self):
        """
        Get browser HTML validation message for password.
        """

        try:
            password_field = self.driver.find_element(
                *self.PASSWORD
            )

            return (
                password_field.get_attribute(
                    "validationMessage"
                )
                or ""
            )

        except Exception:
            return ""

    def has_validation_message(self):
        """
        Check whether browser validation message
        exists for email or password.
        """

        email_message = (
            self.get_email_validation_message()
        )

        password_message = (
            self.get_password_validation_message()
        )

        return bool(
            email_message
            or password_message
        )

    # ============================================================
    # SCREEN RESOLUTION
    # ============================================================

    def set_window_size(self, width, height):
        """
        Set browser window size.
        """

        self.driver.set_window_size(
            width,
            height
        )

    # ============================================================
    # PAGE STABILITY
    # ============================================================

    def is_login_page_stable(self):
        """
        Check that important login elements remain visible.
        """

        return (
            self.is_login_page_displayed()
            and self.is_login_button_displayed()
        )

