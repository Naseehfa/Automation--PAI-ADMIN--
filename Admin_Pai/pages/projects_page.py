import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException
)


class ProjectsPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    # ============================================================
    # ZOOM
    # ============================================================

    def set_zoom_out(self):

        self.driver.execute_script(
            """
            document.body.style.zoom = '85%';
            """
        )

        time.sleep(1)

    # ============================================================
    # SIDEBAR NAVIGATION
    # ============================================================

    client_projects_menu = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[4]/button/span"
    )

    client_projects_submenu = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[4]/div/button[2]"
    )

    # ============================================================
    # PROJECT TABLE
    # ============================================================

    # Edit icon
    edit_project_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div[2]/div[2]/div[39]/div[5]/button[1]/img"
    )

    # Delete icon
    delete_project_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div[2]/div[2]/div[35]/div[5]/button[2]/img"
    )

    # ============================================================
    # EDIT MODAL
    # ============================================================

    project_name_input = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[1]/input"
    )

    project_category_select = (
        By.XPATH,
        "/html/body/div/div/div/div[2]/div[2]/div/div[2]/select"
    )

    project_website_input = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[4]/input"
    )

    project_description_textarea = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[5]/textarea"
    )

    update_project_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[6]/button"
    )

    # ============================================================
    # DELETE CONFIRMATION
    # ============================================================

    # NO button
    delete_no_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[3]/div/div[2]/button[1]"
    )

    # YES button
    delete_yes_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[3]/div/div[2]/button[2]"
    )

    # ============================================================
    # GENERIC WAIT METHODS
    # ============================================================

    def wait_visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

    def wait_present(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

    def wait_clickable(self, locator):

        return self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )

    # ============================================================
    # SCROLL TO PROJECT TABLE
    # ============================================================

    def scroll_to_project_table(self):

        print(
            "Scrolling to project table..."
        )

        self.driver.execute_script(
            """
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'instant'
            });
            """
        )

        time.sleep(2)

        print(
            "Project table scroll completed."
        )

    # ============================================================
    # OPEN CLIENT PROJECTS
    # ============================================================

    def open_projects(self):

        print(
            "\nOpening Client Projects module..."
        )

        self.set_zoom_out()

        menu = self.wait_clickable(
            self.client_projects_menu
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            menu
        )

        time.sleep(1)

        try:

            menu.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                menu
            )

        time.sleep(1)

        submenu = self.wait_clickable(
            self.client_projects_submenu
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            submenu
        )

        time.sleep(1)

        try:

            submenu.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                submenu
            )

        time.sleep(4)

        self.set_zoom_out()

        self.scroll_to_project_table()

        print(
            "Client Projects module opened."
        )

    # ============================================================
    # REFRESH PROJECTS PAGE
    # ============================================================

    def refresh_projects_page(self):

        print(
            "\nRefreshing Client Projects page..."
        )

        self.driver.refresh()

        # Wait until browser finishes loading body
        self.wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        time.sleep(4)

        self.set_zoom_out()

        self.scroll_to_project_table()

        print(
            "Client Projects page refreshed successfully."
        )

    # ============================================================
    # EDIT ICON
    # ============================================================

    def click_edit_project(self):

        print(
            "\nClicking Edit icon..."
        )

        self.scroll_to_project_table()

        edit_button = self.wait_clickable(
            self.edit_project_button
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
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

        time.sleep(3)

        print(
            "Edit icon clicked."
        )

    # ============================================================
    # VERIFY EDIT MODAL OPEN
    # ============================================================

    def is_edit_modal_open(self):

        try:

            self.wait_visible(
                self.project_name_input
            )

            return True

        except TimeoutException:

            return False

    # ============================================================
    # GET PROJECT NAME
    # ============================================================

    def get_project_name(self):

        field = self.wait_visible(
            self.project_name_input
        )

        return (
            field.get_attribute("value")
            or ""
        ).strip()

    # ============================================================
    # GET PROJECT CATEGORY
    # ============================================================

    def get_project_category(self):

        field = self.wait_visible(
            self.project_category_select
        )

        return (
            field.get_attribute("value")
            or ""
        ).strip()

    # ============================================================
    # GET WEBSITE
    # ============================================================

    def get_project_website(self):

        field = self.wait_visible(
            self.project_website_input
        )

        return (
            field.get_attribute("value")
            or ""
        ).strip()

    # ============================================================
    # GET DESCRIPTION
    # ============================================================

    def get_project_description(self):

        field = self.wait_visible(
            self.project_description_textarea
        )

        return (
            field.get_attribute("value")
            or ""
        ).strip()

    # ============================================================
    # CLEAR PROJECT NAME
    # ============================================================

    def clear_project_name(self):

        field = self.wait_visible(
            self.project_name_input
        )

        field.click()

        field.clear()

        # Extra CTRL+A + BACKSPACE to make sure
        # React controlled input is completely empty

        field.send_keys(
            "\ue009a"
        )

        field.send_keys(
            "\ue003"
        )

        time.sleep(1)

        print(
            "Project Name completely cleared."
        )

    # ============================================================
    # CLEAR DESCRIPTION
    # ============================================================

    def clear_project_description(self):

        field = self.wait_visible(
            self.project_description_textarea
        )

        field.click()

        field.clear()

        field.send_keys(
            "\ue009a"
        )

        field.send_keys(
            "\ue003"
        )

        time.sleep(1)

        print(
            "Project Description completely cleared."
        )

    # ============================================================
    # ENTER PROJECT NAME
    # ============================================================

    def enter_project_name(
        self,
        project_name
    ):

        field = self.wait_visible(
            self.project_name_input
        )

        field.click()

        field.clear()

        field.send_keys(
            project_name
        )

        print(
            "Project Name entered:",
            project_name
        )

    # ============================================================
    # ENTER DESCRIPTION
    # ============================================================

    def enter_project_description(
        self,
        description
    ):

        field = self.wait_visible(
            self.project_description_textarea
        )

        field.click()

        field.clear()

        field.send_keys(
            description
        )

        print(
            "Project Description entered:",
            description
        )

    # ============================================================
    # CLICK UPDATE
    # ============================================================

    def click_update_project(self):

        print(
            "\nClicking Update button..."
        )

        button = self.wait_clickable(
            self.update_project_button
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
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

        time.sleep(4)

        print(
            "Update button clicked."
        )

    # ============================================================
    # GET BODY TEXT
    # ============================================================

    def get_body_text(self):

        try:

            return self.driver.find_element(
                By.TAG_NAME,
                "body"
            ).text

        except Exception:

            return ""

    # ============================================================
    # VERIFY PROJECT NAME IN TABLE
    # ============================================================

    def is_project_name_present_in_table(
        self,
        project_name
    ):

        project_name = project_name.strip()

        if not project_name:

            return False

        try:

            # IMPORTANT:
            # Search only table rows.
            # Do NOT search entire body because the
            # deleted value could remain in a toast/modal.

            rows = self.driver.find_elements(
                By.XPATH,
                "//table//tbody//tr"
            )

            for row in rows:

                try:

                    if project_name in row.text:

                        print(
                            "Project found in table:",
                            project_name
                        )

                        return True

                except StaleElementReferenceException:

                    continue

            print(
                "Project not found in table:",
                project_name
            )

            return False

        except Exception as e:

            print(
                "Error checking project table:",
                e
            )

            return False

    # ============================================================
    # VERIFY PROJECT DOES NOT EXIST IN TABLE
    # ============================================================

    def is_project_deleted_from_table(
        self,
        project_name
    ):

        project_name = project_name.strip()

        if not project_name:

            return False

        # Give the application time to update
        end_time = time.time() + 15

        while time.time() < end_time:

            if not self.is_project_name_present_in_table(
                project_name
            ):

                return True

            time.sleep(1)

        return False

    # ============================================================
    # GET DELETE TARGET PROJECT NAME
    # ============================================================

    def get_delete_target_project_name(self):

        print(
            "\nGetting project data before deletion..."
        )

        self.scroll_to_project_table()

        # Your supplied delete XPath points to row 35.
        # We get the complete row containing that button.

        delete_button = self.wait_present(
            self.delete_project_button
        )

        row = delete_button.find_element(
            By.XPATH,
            "./ancestor::tr"
        )

        row_text = row.text.strip()

        print(
            "Delete target row:"
        )

        print(
            row_text
        )

        # Try to extract the first meaningful cell.
        cells = row.find_elements(
            By.XPATH,
            "./td"
        )

        if cells:

            for cell in cells:

                text = cell.text.strip()

                if text:

                    print(
                        "Detected project name:",
                        text
                    )

                    return text

        # Fallback to first non-empty line
        lines = [
            line.strip()
            for line in row_text.splitlines()
            if line.strip()
        ]

        if lines:

            return lines[0]

        return ""

    # ============================================================
    # CLICK DELETE
    # ============================================================

    def click_delete_project(self):

        print(
            "\nClicking Delete icon..."
        )

        self.scroll_to_project_table()

        delete_button = self.wait_clickable(
            self.delete_project_button
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            delete_button
        )

        time.sleep(1)

        try:

            delete_button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                delete_button
            )

        time.sleep(2)

        print(
            "Delete confirmation opened."
        )

    # ============================================================
    # VERIFY DELETE CONFIRMATION
    # ============================================================

    def is_delete_confirmation_open(self):

        try:

            self.wait_visible(
                self.delete_yes_button
            )

            self.wait_visible(
                self.delete_no_button
            )

            return True

        except TimeoutException:

            return False

    # ============================================================
    # CLICK NO
    # ============================================================

    def click_delete_no(self):

        print(
            "\nClicking NO on delete confirmation..."
        )

        button = self.wait_clickable(
            self.delete_no_button
        )

        try:

            button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        time.sleep(3)

        print(
            "NO button clicked."
        )

    # ============================================================
    # CLICK YES
    # ============================================================

    def click_delete_yes(self):

        print(
            "\nClicking YES to confirm deletion..."
        )

        button = self.wait_clickable(
            self.delete_yes_button
        )

        try:

            button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        time.sleep(5)

        print(
            "YES button clicked."
        )
        print(
            "Delete request submitted."
        )