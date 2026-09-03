from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # ============================================================
    # LOCATORS
    # ============================================================

    email = (By.ID, "email")
    password = (By.ID, "password")
    login_btn = (By.CSS_SELECTOR, "button.login-btn")

    # Eye icon
    eye_btn = (By.CSS_SELECTOR, "button.eye-button")

    # Remember Me checkbox
    remember_checkbox = (By.CSS_SELECTOR, "input.remember-checkbox")

    # ============================================================
    # EMAIL METHODS
    # ============================================================

    def enter_username(self, username):
        email_field = self.driver.find_element(*self.email)
        email_field.clear()
        email_field.send_keys(username)

    # Alias for email-related test cases
    def enter_email(self, email):
        self.enter_username(email)

    # ============================================================
    # PASSWORD METHODS
    # ============================================================

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password)
        password_field.clear()
        password_field.send_keys(password)

    # ============================================================
    # BUTTON / CHECKBOX METHODS
    # ============================================================

    def click_eye_icon(self):
        self.driver.find_element(*self.eye_btn).click()

    def click_remember_me(self):
        checkbox = self.driver.find_element(*self.remember_checkbox)

        if not checkbox.is_selected():
            checkbox.click()

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    # ============================================================
    # LOGIN METHOD
    # ============================================================

    def login(self, username, password):
        """
        Normal login flow:
        1. Enter username/email
        2. Enter password
        3. Show password
        4. Select Remember Me
        5. Click Login
        """

        self.enter_username(username)
        self.enter_password(password)

        self.click_eye_icon()
        self.click_remember_me()
        self.click_login()

    # ============================================================
    # VALIDATION / UTILITY METHODS
    # ============================================================

    def is_login_button_displayed(self):
        return self.driver.find_element(*self.login_btn).is_displayed()

    def is_login_button_enabled(self):
        return self.driver.find_element(*self.login_btn).is_enabled()

    def get_email_value(self):
        return self.driver.find_element(*self.email).get_attribute("value")

    def get_password_value(self):
        return self.driver.find_element(*self.password).get_attribute("value")

    def get_email_validation_message(self):
        """
        Returns the browser's HTML5 validation message for
        the email field, if available.
        """
        email_field = self.driver.find_element(*self.email)
        return email_field.get_attribute("validationMessage")

    def get_password_validation_message(self):
        """
        Returns the browser's HTML5 validation message for
        the password field, if available.
        """
        password_field = self.driver.find_element(*self.password)
        return password_field.get_attribute("validationMessage")

    def click_login_multiple_times(self, count=3):
        """
        Click Login button multiple times.
        Used to verify that the login page remains stable.
        """

        for _ in range(count):
            self.driver.find_element(*self.login_btn).click()