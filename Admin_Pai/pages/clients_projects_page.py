import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class ClientsProjectsPage:

    # ============================================================
    # URL
    # ============================================================

    CLIENTS_PROJECTS_URL = (
        "https://paiwebsiteqa.pineappleai.cloud/admin/clients-projects"
    )

    # ============================================================
    # INITIALIZE
    # ============================================================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    # ============================================================
    # LEFT SIDE MENU
    # ============================================================

    COMPANY_MENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[4]/button'
    )

    CLIENTS_PROJECTS_SUBMENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[4]/div/button[2]'
    )

    # ============================================================
    # PROJECT FORM
    # ============================================================

    PROJECT_NAME = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[1]/input'
    )

    PROJECT_CATEGORY = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/select'
    )

    PROJECT_CATEGORY_FALLBACK = (
        By.XPATH,
        '/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/select'
    )

    PROJECT_IMAGE_CONTAINER = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[3]/div/span'
    )

    PROJECT_IMAGE_INPUT = (
        By.XPATH,
        '//input[@type="file"]'
    )

    PROJECT_URL = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[4]/input'
    )

    PROJECT_DESCRIPTION = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[5]/textarea'
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/button'
    )

    # ============================================================
    # PROJECT TABLE
    # ============================================================

    PROJECT_TABLE = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]/div[4]'
    )

    PROJECT_TABLE_ROWS = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]/div[4]/div'
    )

    # ============================================================
    # EDIT PROJECT
    # ============================================================

    EDIT_PROJECT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]/div[13]/div[5]/button[1]/img'
    )

    EDIT_PROJECT_NAME = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/input'
    )

    EDIT_SAVE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[6]/button'
    )

    # ============================================================
    # DELETE PROJECT
    # ============================================================

    # Correct Delete button XPath provided
    DELETE_PROJECT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]/div[20]/div[5]/button[2]/img'
    )

    # Correct Delete confirmation button XPath provided
    DELETE_CONFIRM_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[3]/div/div[2]/button[2]'
    )

    # Delete confirmation modal
    DELETE_CONFIRM_MODAL = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[3]/div'
    )

    # ============================================================
    # NAVIGATION
    # ============================================================

    def click_company_menu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.COMPANY_MENU
            )
        )

        element.click()

        time.sleep(1)

    # ============================================================

    def click_clients_projects_submenu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.CLIENTS_PROJECTS_SUBMENU
            )
        )

        element.click()

        self.wait.until(
            EC.url_contains(
                "/admin/clients-projects"
            )
        )

        time.sleep(2)

    # ============================================================

    def navigate_to_clients_projects(self):

        self.click_company_menu()

        self.click_clients_projects_submenu()

    # ============================================================
    # PROJECT NAME
    # ============================================================

    def enter_project_name(
        self,
        project_name
    ):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.PROJECT_NAME
            )
        )

        element.clear()

        if project_name is not None:

            element.send_keys(
                project_name
            )

        time.sleep(0.5)

    # ============================================================
    # CATEGORY
    # ============================================================

    def get_category_dropdown(self):

        try:

            dropdown = self.wait.until(
                EC.presence_of_element_located(
                    self.PROJECT_CATEGORY
                )
            )

            return dropdown

        except Exception:

            dropdown = self.wait.until(
                EC.presence_of_element_located(
                    self.PROJECT_CATEGORY_FALLBACK
                )
            )

            return dropdown

    # ============================================================

    def get_available_categories(self):

        dropdown = self.get_category_dropdown()

        select = Select(
            dropdown
        )

        categories = []

        for option in select.options:

            text = option.text.strip()

            if text:

                categories.append(
                    text
                )

        return categories

    # ============================================================

    def print_available_categories(self):

        dropdown = self.get_category_dropdown()

        select = Select(
            dropdown
        )

        print(
            "\nAvailable Project Categories:"
        )

        for option in select.options:

            print(
                "-",
                option.text.strip(),
                "| value =",
                option.get_attribute("value")
            )

    # ============================================================

    def select_project_category(
        self,
        category
    ):

        dropdown = self.get_category_dropdown()

        select = Select(
            dropdown
        )

        self.print_available_categories()

        category = category.strip()

        matching_text = None

        for option in select.options:

            option_text = option.text.strip()

            if (
                option_text.lower()
                == category.lower()
            ):

                matching_text = option_text

                break

        if matching_text is None:

            available_categories = [
                option.text.strip()
                for option in select.options
                if option.text.strip()
            ]

            raise ValueError(
                f"\nInvalid Project Category: "
                f"'{category}'\n\n"
                f"Available categories:\n"
                f"{available_categories}\n\n"
                f"Use one of the actual dropdown values."
            )

        select.select_by_visible_text(
            matching_text
        )

        time.sleep(1)

        selected_option = (
            select.first_selected_option
        )

        selected_text = (
            selected_option.text.strip()
        )

        if (
            selected_text.lower()
            != matching_text.lower()
        ):

            raise AssertionError(
                f"Category selection failed. "
                f"Expected '{matching_text}', "
                f"but selected '{selected_text}'"
            )

        print(
            "Selected Project Category:",
            selected_text
        )

    # ============================================================
    # IMAGE UPLOAD
    # ============================================================

    def upload_project_image(
        self,
        image_path
    ):

        if not os.path.exists(image_path):

            raise FileNotFoundError(
                f"Image file not found:\n"
                f"{image_path}"
            )

        file_input = self.wait.until(
            EC.presence_of_element_located(
                self.PROJECT_IMAGE_INPUT
            )
        )

        file_input.send_keys(
            image_path
        )

        time.sleep(1)

        print(
            "Project image uploaded:",
            image_path
        )

    # ============================================================
    # PROJECT URL
    # ============================================================

    def enter_project_url(
        self,
        url
    ):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.PROJECT_URL
            )
        )

        element.clear()

        if url is not None:

            element.send_keys(
                url
            )

        time.sleep(0.5)

    # ============================================================
    # DESCRIPTION
    # ============================================================

    def enter_description(
        self,
        description
    ):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.PROJECT_DESCRIPTION
            )
        )

        element.clear()

        if description is not None:

            element.send_keys(
                description
            )

        time.sleep(0.5)

    # ============================================================
    # SUBMIT
    # ============================================================

    def click_submit(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON
            )
        )

        element.click()

        time.sleep(3)

    # ============================================================
    # CHECK FORM
    # ============================================================

    def is_form_displayed(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.PROJECT_NAME
                )
            )

            return True

        except Exception:

            return False

    # ============================================================
    # GET PROJECT NAME
    # ============================================================

    def get_project_name_value(self):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.PROJECT_NAME
            )
        )

        return element.get_attribute(
            "value"
        )

    # ============================================================
    # GET CATEGORY
    # ============================================================

    def get_selected_category(self):

        dropdown = self.get_category_dropdown()

        select = Select(
            dropdown
        )

        return (
            select.first_selected_option
            .text
            .strip()
        )

    # ============================================================
    # GET URL
    # ============================================================

    def get_project_url_value(self):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.PROJECT_URL
            )
        )

        return element.get_attribute(
            "value"
        )

    # ============================================================
    # GET DESCRIPTION
    # ============================================================

    def get_description_value(self):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.PROJECT_DESCRIPTION
            )
        )

        return element.get_attribute(
            "value"
        )

    # ============================================================
    # FILL COMPLETE FORM
    # ============================================================

    def fill_project_form(
        self,
        project_name=None,
        category=None,
        image_path=None,
        url=None,
        description=None
    ):

        if project_name is not None:

            self.enter_project_name(
                project_name
            )

        if category is not None:

            self.select_project_category(
                category
            )

        if image_path is not None:

            self.upload_project_image(
                image_path
            )

        if url is not None:

            self.enter_project_url(
                url
            )

        if description is not None:

            self.enter_description(
                description
            )

        time.sleep(1)

    # ============================================================
    # ADD PROJECT
    # ============================================================

    def add_project(
        self,
        project_name,
        category,
        image_path,
        url,
        description
    ):

        self.fill_project_form(
            project_name=project_name,
            category=category,
            image_path=image_path,
            url=url,
            description=description
        )

        self.click_submit()

        time.sleep(3)

    # ============================================================
    # EDIT PROJECT
    # ============================================================

    def click_edit_project(self):

        print(
            "\nClicking Edit Project button..."
        )

        edit_button = self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_PROJECT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            edit_button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            edit_button
        )

        time.sleep(2)

        print(
            "Edit button clicked."
        )

    # ============================================================
    # CHECK EDIT MODAL
    # ============================================================

    def is_edit_modal_displayed(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.EDIT_PROJECT_NAME
                )
            )

            return True

        except Exception:

            return False

    # ============================================================
    # GET OLD EDIT PROJECT NAME
    # ============================================================

    def get_edit_project_name(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_PROJECT_NAME
            )
        )

        return element.get_attribute(
            "value"
        )

    # ============================================================
    # ENTER NEW EDIT PROJECT NAME
    # ============================================================

    def enter_edit_project_name(
        self,
        project_name
    ):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_PROJECT_NAME
            )
        )

        element.clear()

        time.sleep(0.5)

        element.send_keys(
            project_name
        )

        time.sleep(0.5)

        print(
            "Updated Project Name:",
            project_name
        )

    # ============================================================
    # CLICK UPDATE BUTTON
    # ============================================================

    def click_edit_save(self):

        print(
            "Clicking Update button..."
        )

        update_button = self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_SAVE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            update_button
        )

        time.sleep(0.5)

        self.driver.execute_script(
            "arguments[0].click();",
            update_button
        )

        print(
            "Update button clicked."
        )

    # ============================================================
    # WAIT FOR EDIT MODAL TO CLOSE
    # ============================================================

    def wait_for_edit_modal_to_close(self):

        print(
            "Waiting for Update to complete..."
        )

        try:

            self.wait.until(
                EC.invisibility_of_element_located(
                    self.EDIT_PROJECT_NAME
                )
            )

            print(
                "Edit modal closed successfully."
            )

        except Exception:

            raise AssertionError(
                "Project was updated/clicked, "
                "but the Edit modal did not close."
            )

        time.sleep(2)

    # ============================================================
    # VERIFY UPDATED PROJECT NAME
    # ============================================================

    def verify_project_name_in_page(
        self,
        project_name
    ):

        print(
            "Verifying updated project name..."
        )

        project_name_locator = (
            By.XPATH,
            f'//*[normalize-space(text())="{project_name}"]'
        )

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    project_name_locator
                )
            )

            print(
                "Updated project name found:",
                project_name
            )

            return True

        except Exception:

            print(
                "Updated project name was not found:",
                project_name
            )

            return False

    # ============================================================
    # COMPLETE EDIT PROJECT
    # ============================================================

    def edit_project(
        self,
        new_project_name
    ):

        print(
            "\n========== EDIT PROJECT =========="
        )

        self.click_edit_project()

        assert (
            self.is_edit_modal_displayed()
        ), (
            "Edit Project modal "
            "was not displayed."
        )

        old_project_name = (
            self.get_edit_project_name()
        )

        print(
            "Old Project Name:",
            old_project_name
        )

        self.enter_edit_project_name(
            new_project_name
        )

        current_name = (
            self.get_edit_project_name()
        )

        assert (
            current_name
            == new_project_name
        ), (
            f"Project name was not updated "
            f"correctly in input.\n"
            f"Expected: {new_project_name}\n"
            f"Actual: {current_name}"
        )

        print(
            "New Project Name entered successfully."
        )

        self.click_edit_save()

        self.wait_for_edit_modal_to_close()

        assert (
            "/admin/clients-projects"
            in self.driver.current_url
        ), (
            "User is not on Clients Projects page "
            "after updating."
        )

        assert self.verify_project_name_in_page(
            new_project_name
        ), (
            f"Updated project name "
            f"'{new_project_name}' "
            f"was not found on the page."
        )

        print(
            "Edit Project completed successfully."
        )

    # ============================================================
    # DELETE PROJECT
    # ============================================================

    def click_delete_project(self):

        print(
            "\nClicking Delete Project button..."
        )

        delete_button = self.wait.until(
            EC.presence_of_element_located(
                self.DELETE_PROJECT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            delete_button
        )

        time.sleep(1)

        # Wait until button is clickable
        self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_PROJECT_BUTTON
            )
        )

        # Click Delete button
        self.driver.execute_script(
            "arguments[0].click();",
            delete_button
        )

        print(
            "Delete button clicked."
        )

        time.sleep(2)

    # ============================================================
    # CHECK DELETE CONFIRMATION MODAL
    # ============================================================

    def is_delete_confirmation_displayed(self):

        print(
            "\nChecking Delete confirmation modal..."
        )

        try:

            # Wait for confirmation modal
            self.wait.until(
                EC.visibility_of_element_located(
                    self.DELETE_CONFIRM_MODAL
                )
            )

            print(
                "Delete confirmation modal displayed."
            )

            # Wait for exact Confirm Delete button
            self.wait.until(
                EC.visibility_of_element_located(
                    self.DELETE_CONFIRM_BUTTON
                )
            )

            print(
                "Confirm Delete button displayed."
            )

            return True

        except Exception as error:

            print(
                "Delete confirmation modal "
                "was NOT displayed."
            )

            print(
                "Error:",
                error
            )

            return False

    # ============================================================
    # CONFIRM DELETE PROJECT
    # ============================================================

    def confirm_delete_project(self):

        print(
            "\nClicking Confirm Delete button..."
        )

        confirm_button = self.wait.until(
            EC.presence_of_element_located(
                self.DELETE_CONFIRM_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            confirm_button
        )

        time.sleep(0.5)

        # Wait until clickable
        self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_CONFIRM_BUTTON
            )
        )

        # Click confirmation button
        self.driver.execute_script(
            "arguments[0].click();",
            confirm_button
        )

        print(
            "Confirm Delete button clicked."
        )

        time.sleep(3)

    # ============================================================
    # VERIFY PROJECT DELETED
    # ============================================================

    def verify_project_deleted(
        self,
        project_name
    ):

        print(
            "\nVerifying project was deleted..."
        )

        project_locator = (
            By.XPATH,
            f'//*[normalize-space(text())="{project_name}"]'
        )

        try:

            self.wait.until(
                EC.invisibility_of_element_located(
                    project_locator
                )
            )

            print(
                "Project deleted successfully:",
                project_name
            )

            return True

        except Exception:

            print(
                "Project still exists:",
                project_name
            )

            return False

    # ============================================================
    # COMPLETE DELETE PROJECT
    # ============================================================

    def delete_project(
        self,
        project_name=None
    ):

        print(
            "\n========== DELETE PROJECT =========="
        )

        # --------------------------------------------------------
        # STEP 1 - CLICK DELETE
        # --------------------------------------------------------

        self.click_delete_project()

        # --------------------------------------------------------
        # STEP 2 - VERIFY CONFIRMATION MODAL
        # --------------------------------------------------------

        assert (
            self.is_delete_confirmation_displayed()
        ), (
            "Delete confirmation modal "
            "was not displayed."
        )

        # --------------------------------------------------------
        # STEP 3 - CONFIRM DELETE
        # --------------------------------------------------------

        self.confirm_delete_project()

        # --------------------------------------------------------
        # STEP 4 - VERIFY PAGE URL
        # --------------------------------------------------------

        self.wait.until(
            EC.url_contains(
                "/admin/clients-projects"
            )
        )

        assert (
            "/admin/clients-projects"
            in self.driver.current_url
        ), (
            "User is not on Clients Projects page "
            "after deleting."
        )

        # --------------------------------------------------------
        # STEP 5 - VERIFY PROJECT DELETED
        # --------------------------------------------------------

        if project_name is not None:

            assert (
                self.verify_project_deleted(
                    project_name
                )
            ), (
                f"Project '{project_name}' "
                f"was not deleted."
            )

        print(
            "Delete Project completed successfully."
        )

    # ============================================================
    # URL CHECK
    # ============================================================

    def is_on_clients_projects_page(self):

        return (
            "/admin/clients-projects"
            in self.driver.current_url
        )