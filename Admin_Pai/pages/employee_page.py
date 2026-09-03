
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class EmployeePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ============================================================
    # URL
    # ============================================================

    EMPLOYEE_URL = (
        "https://paiwebsiteqa.pineappleai.cloud/admin/team"
    )

    # ============================================================
    # SIDEBAR
    # ============================================================

    team_menu = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[2]/button/span"
    )

    # ============================================================
    # EMPLOYEE TABLE
    # ============================================================

    first_employee_edit_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div/button[1]/img"
    )

    # ============================================================
    # EDIT FORM
    # ============================================================

    employee_name = (
        By.XPATH,
        "//*[@id='modal-name']"
    )

    position_container = (
        By.XPATH,
        "/html/body/div/div/div/div[2]/div[2]/div/form/div[1]/div[2]/div[2]/select"
    )

    position_select = (
        By.XPATH,
        "//*[@id='modal-position']"
    )

    linkedin_field = (
        By.XPATH,
        "//*[@id='modal-linkedin']"
    )

    description_field = (
        By.XPATH,
        "//*[@id='modal-description']"
    )

    update_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/form/div[3]/button"
    )

    # ============================================================
    # GENERIC WAIT METHODS
    # ============================================================

    def wait_visible(self, locator, timeout=20):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=20):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.element_to_be_clickable(locator)
        )

    # ============================================================
    # OPEN EMPLOYEE PAGE
    # ============================================================

    def open_employee_page(self):

        print("\nOpening Employee / Team page...")

        self.driver.get(self.EMPLOYEE_URL)

        self.wait.until(
            lambda driver:
            driver.current_url == self.EMPLOYEE_URL
        )

        time.sleep(2)

        print("Employee page opened.")

    # ============================================================
    # SCROLL TO TOP
    # ============================================================

    def scroll_to_top(self):

        self.driver.execute_script(
            "window.scrollTo(0, 0);"
        )

        time.sleep(1)

    # ============================================================
    # SCROLL TO EMPLOYEE TABLE
    # ============================================================

    def scroll_to_employee_table(self):

        try:

            edit_button = self.wait_visible(
                self.first_employee_edit_button
            )

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    behavior: 'instant',
                    block: 'center'
                });
                """,
                edit_button
            )

            time.sleep(1)

        except TimeoutException:

            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(1)

    # ============================================================
    # OPEN FIRST EMPLOYEE EDIT FORM
    # ============================================================

    def click_edit_first_employee(self):

        print("\nClicking Edit icon of first employee...")

        self.scroll_to_employee_table()

        edit_button = self.wait_clickable(
            self.first_employee_edit_button
        )

        try:

            edit_button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                edit_button
            )

        time.sleep(2)

        print("Employee Edit icon clicked.")

    # ============================================================
    # VERIFY EDIT FORM OPEN
    # ============================================================

    def is_edit_form_open(self):

        try:

            self.wait_visible(
                self.employee_name,
                timeout=10
            )

            return True

        except TimeoutException:

            return False

    # ============================================================
    # GET NAME
    # ============================================================

    def get_employee_name(self):

        field = self.wait_visible(
            self.employee_name
        )

        return (
            field.get_attribute("value")
            or ""
        ).strip()

    # ============================================================
    # ENTER NAME
    # ============================================================

    def enter_employee_name(self, name):

        field = self.wait_visible(
            self.employee_name
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: 'center'
            });
            """,
            field
        )

        field.click()
        field.clear()
        field.send_keys(name)

        print(
            "Employee Name entered:",
            name
        )

    # ============================================================
    # CLEAR NAME
    # ============================================================

    def clear_employee_name(self):

        field = self.wait_visible(
            self.employee_name
        )

        field.click()
        field.clear()

        # Trigger React input/change events
        self.driver.execute_script(
            """
            arguments[0].dispatchEvent(
                new Event('input', {bubbles: true})
            );

            arguments[0].dispatchEvent(
                new Event('change', {bubbles: true})
            );
            """,
            field
        )

        print("Employee Name cleared.")

    # ============================================================
    # GET POSITION
    # ============================================================

    def get_position(self):

        field = self.wait_visible(
            self.position_select
        )

        select = Select(field)

        try:
            return select.first_selected_option.text.strip()
        except Exception:
            return ""

    # ============================================================
    # GET POSITION OPTIONS
    # ============================================================

    def get_position_options(self):

        field = self.wait_visible(
            self.position_select
        )

        select = Select(field)

        options = []

        for option in select.options:

            text = option.text.strip()

            value = option.get_attribute("value")

            if text:
                options.append(
                    {
                        "text": text,
                        "value": value
                    }
                )

        return options

    # ============================================================
    # CHANGE POSITION
    # ============================================================

    def change_position(self):

        field = self.wait_visible(
            self.position_select
        )

        select = Select(field)

        current_position = (
            select.first_selected_option.text.strip()
        )

        options = select.options

        print(
            "Current Position:",
            current_position
        )

        # --------------------------------------------------------
        # Find another valid selectable option
        # --------------------------------------------------------

        for option in options:

            text = option.text.strip()
            value = option.get_attribute("value")

            if not text:
                continue

            # Skip placeholder options
            if value in (None, ""):
                continue

            if text == current_position:
                continue

            try:

                select.select_by_visible_text(text)

                # Trigger change event for React
                self.driver.execute_script(
                    """
                    arguments[0].dispatchEvent(
                        new Event('change', {bubbles: true})
                    );

                    arguments[0].dispatchEvent(
                        new Event('input', {bubbles: true})
                    );
                    """,
                    field
                )

                time.sleep(1)

                print(
                    "Position changed from",
                    current_position,
                    "to",
                    text
                )

                return text

            except Exception:

                continue

        raise AssertionError(
            "No different valid Position option "
            "was available."
        )

    # ============================================================
    # CLEAR POSITION / NO POSITION SELECTION
    # ============================================================

    def clear_position(self):

        field = self.wait_visible(
            self.position_select
        )

        select = Select(field)

        print(
            "Attempting to clear Position..."
        )

        # First try selecting empty value
        try:

            select.select_by_value("")

        except Exception:

            try:

                select.select_by_index(0)

            except Exception:

                self.driver.execute_script(
                    """
                    arguments[0].selectedIndex = 0;

                    arguments[0].dispatchEvent(
                        new Event('change', {bubbles: true})
                    );

                    arguments[0].dispatchEvent(
                        new Event('input', {bubbles: true})
                    );
                    """,
                    field
                )

        time.sleep(1)

        print(
            "Position selection cleared."
        )

    # ============================================================
    # GET LINKEDIN
    # ============================================================

    def get_linkedin(self):

        field = self.wait_visible(
            self.linkedin_field
        )

        return (
            field.get_attribute("value")
            or ""
        ).strip()

    # ============================================================
    # ENTER LINKEDIN
    # ============================================================

    def enter_linkedin(self, linkedin):

        field = self.wait_visible(
            self.linkedin_field
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: 'center'
            });
            """,
            field
        )

        field.click()
        field.clear()
        field.send_keys(linkedin)

        print(
            "LinkedIn entered:",
            linkedin
        )

    # ============================================================
    # GET DESCRIPTION
    # ============================================================

    def get_description(self):

        field = self.wait_visible(
            self.description_field
        )

        return (
            field.get_attribute("value")
            or ""
        ).strip()

    # ============================================================
    # ENTER DESCRIPTION
    # ============================================================

    def enter_description(self, description):

        field = self.wait_visible(
            self.description_field
        )

        field.click()
        field.clear()
        field.send_keys(description)

        print(
            "Description entered:",
            description
        )

    # ============================================================
    # CLICK UPDATE
    # ============================================================

    def click_update(self):

        print("\nClicking Update button...")

        button = self.wait_clickable(
            self.update_button
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: 'center'
            });
            """,
            button
        )

        time.sleep(1)

        try:

            button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        time.sleep(3)

        print("Update button clicked.")

    # ============================================================
    # GET VALIDATION MESSAGES
    # ============================================================

    def get_validation_messages(self):

        messages = []

        # Common validation elements
        locators = [

            (
                By.XPATH,
                "//*[@id='modal-name']/following::*[self::span or self::p][1]"
            ),

            (
                By.XPATH,
                "//*[@id='modal-position']/following::*[self::span or self::p][1]"
            ),

            (
                By.XPATH,
                "//*[@id='modal-linkedin']/following::*[self::span or self::p][1]"
            ),

            (
                By.XPATH,
                "//*[contains(@class,'error')]"
            ),

            (
                By.XPATH,
                "//*[contains(@class,'invalid')]"
            )
        ]

        for locator in locators:

            try:

                elements = self.driver.find_elements(
                    *locator
                )

                for element in elements:

                    if element.is_displayed():

                        text = element.text.strip()

                        if text and text not in messages:

                            messages.append(text)

            except Exception:
                continue

        # Also check native HTML validation
        for locator in [
            self.employee_name,
            self.position_select,
            self.linkedin_field
        ]:

            try:

                field = self.driver.find_element(
                    *locator
                )

                validation = (
                    field.get_attribute(
                        "validationMessage"
                    )
                    or ""
                ).strip()

                if validation and validation not in messages:

                    messages.append(validation)

            except Exception:
                continue

        return messages

    # ============================================================
    # CHECK VALIDATION
    # ============================================================

    def is_validation_displayed(self):

        messages = self.get_validation_messages()

        return len(messages) > 0

    # ============================================================
    # GET SUCCESS MESSAGE
    # ============================================================

    def get_success_message(self):

        success_locators = [

            (
                By.XPATH,
                "//*[contains(translate(text(),'SUCCESS','success'),'success')]"
            ),

            (
                By.XPATH,
                "//*[contains(translate(text(),'UPDATED','updated'),'updated')]"
            ),

            (
                By.XPATH,
                "//*[contains(@class,'toast')]"
            ),

            (
                By.XPATH,
                "//*[contains(@class,'alert')]"
            )
        ]

        for locator in success_locators:

            try:

                element = WebDriverWait(
                    self.driver,
                    5
                ).until(
                    EC.visibility_of_element_located(
                        locator
                    )
                )

                text = element.text.strip()

                if text:
                    return text

            except TimeoutException:
                continue

        return ""

    # ============================================================
    # CHECK SUCCESS MESSAGE
    # ============================================================

    def is_success_message_displayed(self):

        return bool(
            self.get_success_message()
        )

    # ============================================================
    # GET BODY TEXT
    # ============================================================

    def get_page_text(self):

        return self.driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

    # ============================================================
    # VERIFY EMPLOYEE NAME IN TABLE
    # ============================================================

    def is_employee_name_in_table(
        self,
        employee_name
    ):

        try:

            locator = (
                By.XPATH,
                f"//*[normalize-space(text())="
                f"'{employee_name}']"
            )

            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    locator
                )
            )

            return element.is_displayed()

        except TimeoutException:

            return False

    # ============================================================
    # REFRESH PAGE
    # ============================================================

    def refresh_page(self):

        print("\nRefreshing Employee page...")

        self.driver.refresh()

        self.wait.until(
            lambda driver:
            driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        time.sleep(3)

        # IMPORTANT:
        # After refresh browser can retain the previous
        # scroll position. Explicitly return to the table.
        self.scroll_to_top()

        self.scroll_to_employee_table()

        print(
            "Employee page refreshed and table restored."
        )

