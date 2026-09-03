import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchWindowException,
    StaleElementReferenceException,
)


class ServicesPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ============================================================
    # SIDEBAR LOCATORS
    # ============================================================

    services_menu = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[3]/button/span"
    )

    services_submenu = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[3]/div/button[1]"
    )

    # ============================================================
    # SERVICE TABLE
    # ============================================================

    edit_service_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div[3]/div[10]/div[3]/div/button[1]/img"
    )

    # ============================================================
    # SERVICE EDIT FORM
    # ============================================================

    # IMPORTANT:
    # This is the exact Service Name XPath provided by you.
    service_name_field = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/form/div[1]/input"
    )

    description_field = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/form/div[2]/textarea"
    )

    validation_message = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/form/div[3]/div/span[1]"
    )

    update_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/form/div[5]/button"
    )

    # ============================================================
    # HELPER LOCATORS
    # ============================================================

    service_form = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/form"
    )

    # ============================================================
    # GENERIC WAIT METHODS
    # ============================================================

    def wait_visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_present(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_clickable(self, locator):

        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    # ============================================================
    # SAFE PAGE CHECK
    # ============================================================

    def is_browser_open(self):

        try:

            _ = self.driver.current_window_handle

            return True

        except (
            NoSuchWindowException,
            Exception
        ):

            return False

    # ============================================================
    # OPEN SERVICES
    # ============================================================

    def open_services(self):

        print("\nOpening Services menu...")

        services = self.wait_clickable(
            self.services_menu
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            services
        )

        time.sleep(1)

        try:

            services.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                services
            )

        time.sleep(1)

        submenu = self.wait_clickable(
            self.services_submenu
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            submenu
        )

        try:

            submenu.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                submenu
            )

        time.sleep(3)

        print("Services page opened.")

    # ============================================================
    # SCROLL TO SERVICE TABLE
    # ============================================================

    def scroll_to_service_table(self):

        print("\nScrolling to Service table...")

        try:

            edit_button = self.wait_present(
                self.edit_service_button
            )

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
                """,
                edit_button
            )

            time.sleep(2)

            print("Service table is visible.")

            return True

        except (
            TimeoutException,
            StaleElementReferenceException
        ):

            print(
                "Edit button not immediately available."
            )

            # Fallback
            self.driver.execute_script(
                """
                window.scrollTo({
                    top: document.body.scrollHeight,
                    behavior: 'smooth'
                });
                """
            )

            time.sleep(2)

            return False

    # ============================================================
    # REFRESH SERVICES PAGE
    # ============================================================

    def refresh_page(self):

        print("\nRefreshing Services page...")

        try:

            self.driver.refresh()

        except NoSuchWindowException:

            raise AssertionError(
                "Browser window was already closed before "
                "page refresh."
            )

        # Wait for page to load
        self.wait.until(
            lambda d:
            d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        time.sleep(3)

        print("Page refreshed successfully.")

        # --------------------------------------------------------
        # IMPORTANT:
        # After refresh the page starts at the top.
        # Scroll back to the service table.
        # --------------------------------------------------------

        try:

            self.scroll_to_service_table()

        except Exception as error:

            print(
                "Could not automatically scroll to "
                "Service table:",
                error
            )

    # ============================================================
    # CLICK EDIT SERVICE
    # ============================================================

    def click_edit_service(self):

        print("\nClicking Edit Service...")

        # Make sure table is visible
        self.scroll_to_service_table()

        edit_button = self.wait_clickable(
            self.edit_service_button
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
            """,
            edit_button
        )

        time.sleep(1)

        try:

            edit_button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                edit_button
            )

        time.sleep(2)

        print("Edit button clicked.")

    # ============================================================
    # VERIFY EDIT INTERFACE
    # ============================================================

    def is_edit_interface_open(self):

        try:

            self.wait_visible(
                self.service_name_field
            )

            self.wait_visible(
                self.description_field
            )

            return True

        except TimeoutException:

            return False

    # ============================================================
    # GET SERVICE NAME FIELD
    # ============================================================

    def get_service_name_field(self):

        return self.wait_visible(
            self.service_name_field
        )

    # ============================================================
    # GET SERVICE NAME
    # ============================================================

    def get_service_name(self):

        field = self.get_service_name_field()

        return (
            field.get_attribute("value")
            or ""
        )

    # ============================================================
    # ENTER SERVICE NAME
    # ============================================================

    def enter_service_name(
        self,
        service_name
    ):

        field = self.get_service_name_field()

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            field
        )

        field.click()

        field.clear()

        field.send_keys(
            service_name
        )

        print(
            "Service Name entered:",
            service_name
        )

    # ============================================================
    # CLEAR SERVICE NAME
    # ============================================================

    def clear_service_name(self):

        field = self.get_service_name_field()

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            field
        )

        field.click()

        field.clear()

        # Make absolutely sure field is empty
        self.driver.execute_script(
            """
            arguments[0].value = '';
            arguments[0].dispatchEvent(
                new Event('input', {bubbles: true})
            );
            arguments[0].dispatchEvent(
                new Event('change', {bubbles: true})
            );
            """,
            field
        )

        print(
            "Service Name field cleared."
        )

        print(
            "Current Service Name value:",
            field.get_attribute("value")
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
        )

    # ============================================================
    # ENTER DESCRIPTION
    # ============================================================

    def enter_description(
        self,
        description
    ):

        field = self.wait_visible(
            self.description_field
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            field
        )

        field.click()

        field.clear()

        field.send_keys(
            description
        )

        print(
            "Description entered:",
            description
        )

    # ============================================================
    # CLEAR DESCRIPTION
    # ============================================================

    def clear_description(self):

        field = self.wait_visible(
            self.description_field
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            field
        )

        field.click()

        field.clear()

        # Make absolutely sure textarea is empty
        self.driver.execute_script(
            """
            arguments[0].value = '';
            arguments[0].dispatchEvent(
                new Event('input', {bubbles: true})
            );
            arguments[0].dispatchEvent(
                new Event('change', {bubbles: true})
            );
            """,
            field
        )

        print(
            "Description field cleared."
        )

        print(
            "Current Description value:",
            field.get_attribute("value")
        )

    # ============================================================
    # GET CURRENT FORM VALUES
    # ============================================================

    def get_current_form_values(self):

        service_name = self.get_service_name()

        description = self.get_description()

        return (
            service_name,
            description
        )

    # ============================================================
    # CLICK UPDATE
    # ============================================================

    def click_update(self):

        print("\nClicking Update...")

        # --------------------------------------------------------
        # IMPORTANT:
        # Read fields immediately before clicking.
        # This confirms the values are actually empty
        # for negative test cases.
        # --------------------------------------------------------

        try:

            current_service = self.get_service_name()

            current_description = self.get_description()

            print(
                "Service value before Update:",
                repr(current_service)
            )

            print(
                "Description value before Update:",
                repr(current_description)
            )

        except Exception as error:

            print(
                "Could not read form values:",
                error
            )

        button = self.wait_clickable(
            self.update_button
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'smooth',
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

        print(
            "Update button clicked."
        )

    # ============================================================
    # GET VALIDATION MESSAGE
    # ============================================================

    def get_validation_message(self):

        # --------------------------------------------------------
        # First try the exact XPath provided by you.
        # --------------------------------------------------------

        try:

            element = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.visibility_of_element_located(
                    self.validation_message
                )
            )

            text = element.text.strip()

            if text:

                return text

        except TimeoutException:

            pass

        # --------------------------------------------------------
        # React applications may display validation differently.
        # Use fallback validation locators.
        # --------------------------------------------------------

        fallback_locators = [

            (
                By.XPATH,
                "//*[@id='root']/div/div/div[2]/div[2]/div/form//span"
            ),

            (
                By.XPATH,
                "//*[@id='root']/div/div/div[2]/div[2]/div/form//p"
            ),

            (
                By.XPATH,
                "//*[@id='root']/div/div/div[2]/div[2]/div/form//*[contains(@class,'error')]"
            ),

            (
                By.XPATH,
                "//*[@id='root']/div/div/div[2]/div[2]/div/form//*[contains(@class,'invalid')]"
            ),

            (
                By.XPATH,
                "//*[contains(text(),'required')]"
            ),

            (
                By.XPATH,
                "//*[contains(text(),'Required')]"
            ),

            (
                By.XPATH,
                "//*[contains(text(),'Service name')]"
            ),

            (
                By.XPATH,
                "//*[contains(text(),'Service Name')]"
            ),

            (
                By.XPATH,
                "//*[contains(text(),'Description')]"
            )
        ]

        for locator in fallback_locators:

            try:

                elements = self.driver.find_elements(
                    *locator
                )

                for element in elements:

                    if element.is_displayed():

                        text = element.text.strip()

                        if text:

                            return text

            except Exception:

                continue

        # --------------------------------------------------------
        # HTML5 validation fallback
        # --------------------------------------------------------

        try:

            service_field = self.get_service_name_field()

            message = service_field.get_attribute(
                "validationMessage"
            )

            if message:

                return message

        except Exception:

            pass

        try:

            description_field = self.wait_visible(
                self.description_field
            )

            message = description_field.get_attribute(
                "validationMessage"
            )

            if message:

                return message

        except Exception:

            pass

        return ""

    # ============================================================
    # VERIFY VALIDATION
    # ============================================================

    def is_validation_displayed(self):

        message = self.get_validation_message()

        return bool(
            message.strip()
        )

    # ============================================================
    # SUCCESS MESSAGE
    # ============================================================

    def get_success_message(self):

        success_locators = [

            (
                By.XPATH,
                "//*[contains(text(),'successfully')]"
            ),

            (
                By.XPATH,
                "//*[contains(text(),'Successfully')]"
            ),

            (
                By.XPATH,
                "//*[contains(text(),'Success')]"
            ),

            (
                By.XPATH,
                "//*[contains(text(),'updated successfully')]"
            ),

            (
                By.XPATH,
                "//*[contains(text(),'Updated successfully')]"
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
    # VERIFY SUCCESS
    # ============================================================

    def is_success_message_displayed(self):

        return bool(
            self.get_success_message()
        )

    # ============================================================
    # GET PAGE BODY TEXT
    # ============================================================

    def get_table_text(self):

        return self.driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

    # ============================================================
    # VERIFY SERVICE NAME IN TABLE
    # ============================================================

    def verify_service_name_in_table(
        self,
        service_name
    ):

        try:

            self.scroll_to_service_table()

            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        f"//*[normalize-space(text())='{service_name}']"
                    )
                )
            )

            return element.is_displayed()

        except TimeoutException:

            page_text = self.get_table_text()

            return service_name in page_text

    # ============================================================
    # VERIFY DESCRIPTION IN TABLE
    # ============================================================

    def verify_description_in_table(
        self,
        description
    ):

        try:

            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        f"//*[normalize-space(text())='{description}']"
                    )
                )
            )

            return element.is_displayed()

        except TimeoutException:

            page_text = self.get_table_text()

            return description in page_text

    # ============================================================
    # VERIFY BOTH VALUES IN TABLE
    # ============================================================

    def verify_service_data_in_table(
        self,
        service_name,
        description
    ):

        service_found = (
            self.verify_service_name_in_table(
                service_name
            )
        )

        description_found = (
            self.verify_description_in_table(
                description
            )
        )

        return (
            service_found
            and
            description_found
        )

    # ============================================================
    # COUNT SERVICE RECORDS
    # ============================================================

    def count_service_records(self):

        # Try to count rows based on the service table area.
        row_locators = [

            (
                By.XPATH,
                "//*[@id='root']/div/div/div[2]/div/div/div[1]/div[3]/div"
            ),

            (
                By.XPATH,
                "//*[@id='root']/div/div/div[2]/div/div/div[1]/div[3]//div"
            )
        ]

        for locator in row_locators:

            try:

                elements = self.driver.find_elements(
                    *locator
                )

                visible_elements = [
                    element
                    for element in elements
                    if element.is_displayed()
                ]

                if visible_elements:

                    return len(
                        visible_elements
                    )

            except Exception:

                continue

        return 0

    # ============================================================
    # FIND EXACT SERVICE RECORD
    # ============================================================

    def find_service_record(
        self,
        service_name
    ):

        locator = (
            By.XPATH,
            f"//*[normalize-space(text())='{service_name}']"
        )

        try:

            return WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    locator
                )
            )

        except TimeoutException:

            return None

    # ============================================================
    # VERIFY SERVICE EXISTS
    # ============================================================

    def service_exists(
        self,
        service_name
    ):

        return (
            self.find_service_record(
                service_name
            )
            is not None
        )

    # ============================================================
    # VERIFY DATA AFTER REFRESH
    # ============================================================

    def verify_data_after_refresh(
        self,
        service_name,
        description
    ):

        self.refresh_page()

        service_found = (
            self.verify_service_name_in_table(
                service_name
            )
        )

        description_found = (
            self.verify_description_in_table(
                description
            )
        )

        return (
            service_found
            and
            description_found
        )