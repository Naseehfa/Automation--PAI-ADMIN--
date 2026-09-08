import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ============================================================
    # LOCATORS
    # ============================================================

    # Logout button
    logout_btn = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[8]/button"
    )

    # ============================================================
    # LOGOUT
    # ============================================================

    def click_logout(self):

        # Wait until logout button is visible
        button = self.wait.until(
            EC.visibility_of_element_located(
                self.logout_btn
            )
        )

        # Scroll logout button into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        time.sleep(1)

        # Wait until button is clickable
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.logout_btn
            )
        )

        button.click()

        time.sleep(3)

    # ============================================================
    # VERIFY LOGOUT
    # ============================================================

    def is_logged_out(self):

        try:

            self.wait.until(
                EC.url_contains("/login")
            )

            return True

        except Exception:

            return False

    # ============================================================
    # COMPLETE LOGOUT
    # ============================================================

    def logout(self):

        self.click_logout()

        return self.is_logged_out()