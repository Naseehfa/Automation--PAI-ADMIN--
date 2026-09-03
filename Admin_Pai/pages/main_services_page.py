import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainServicesPage:

    # ============================================================
    # INITIALIZATION
    # ============================================================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    # ============================================================
    # URL
    # ============================================================

    MAIN_SERVICES_URL = (
        "https://paiwebsiteqa.pineappleai.cloud/admin/main-services"
    )

    # ============================================================
    # LOCATORS
    # ============================================================

    # ------------------------------------------------------------
    # Main Services menu
    # ------------------------------------------------------------

    MAIN_SERVICES_MENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[3]/button/span'
    )

    MAIN_SERVICES_SUBMENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[3]/div/button[1]'
    )

    # ------------------------------------------------------------
    # Add Service Form
    # ------------------------------------------------------------

    SERVICE_NAME = (
        By.XPATH,
        '//*[@id="serviceName"]'
    )

    # File input
    # Used for valid image and invalid image testing
    SERVICE_FILE = (
        By.XPATH,
        '//input[@type="file"]'
    )

    SERVICE_NAME_SPAN = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div/div/form/div[1]/div[2]/div/span[1]'
    )

    DESCRIPTION = (
        By.XPATH,
        '//*[@id="description"]'
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div/div/form/div[4]/button'
    )

    # ============================================================
    # EDIT LOCATORS
    # ============================================================

    # Edit button - first service
    EDIT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[3]/div[1]/div[3]/div/button[1]/img'
    )

    # Edit service name
    EDIT_SERVICE_NAME = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/form/div[1]/input'
    )

    # Edit / Save button
    EDIT_SAVE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/form/div[5]/button'
    )

    # ============================================================
    # DELETE LOCATORS
    # ============================================================

    # Delete button - first service
    DELETE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[3]/div[1]/div[3]/div/button[2]/img'
    )

    # Delete confirmation modal - Close button
    DELETE_MODAL_CLOSE = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/button/img'
    )

    # Delete confirmation - Cancel
    DELETE_CANCEL_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/button[1]'
    )

    # Delete confirmation - Confirm/Delete
    DELETE_CONFIRM_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/button[2]'
    )

    # ============================================================
    # SECOND SERVICE DELETE
    # ============================================================

    SECOND_DELETE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[3]/div[4]/div[3]/div/button[2]/img'
    )

    # ============================================================
    # NAVIGATION
    # ============================================================

    def open_main_services(self):

        self.driver.get(
            self.MAIN_SERVICES_URL
        )

        self.wait.until(
            EC.url_contains(
                "/admin/main-services"
            )
        )

        time.sleep(3)

    def click_main_services_menu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.MAIN_SERVICES_MENU
            )
        )

        element.click()

        time.sleep(1)

    def click_main_services_submenu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.MAIN_SERVICES_SUBMENU
            )
        )

        element.click()

        self.wait.until(
            EC.url_contains(
                "/admin/main-services"
            )
        )

        time.sleep(3)

    def navigate_to_main_services(self):

        self.click_main_services_menu()

        self.click_main_services_submenu()

    # ============================================================
    # SERVICE NAME
    # ============================================================

    def enter_service_name(
        self,
        service_name
    ):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.SERVICE_NAME
            )
        )

        element.clear()

        element.send_keys(
            service_name
        )

        time.sleep(1)

    # ============================================================
    # FILE UPLOAD
    # ============================================================

    def upload_service_file(
        self,
        file_path
    ):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.SERVICE_FILE
            )
        )

        element.send_keys(
            file_path
        )

        time.sleep(2)

        print(
            "Selected file:",
            file_path
        )

    # ============================================================
    # DESCRIPTION
    # ============================================================

    def enter_description(
        self,
        description
    ):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.DESCRIPTION
            )
        )

        element.clear()

        element.send_keys(
            description
        )

        time.sleep(1)

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

        time.sleep(4)

    # ============================================================
    # FILL SERVICE FORM
    # ============================================================

    def fill_service_form(
        self,
        service_name,
        description,
        service_image
    ):

        self.enter_service_name(
            service_name
        )

        if service_image:

            self.upload_service_file(
                service_image
            )

        self.enter_description(
            description
        )

        time.sleep(2)

    # ============================================================
    # ADD SERVICE
    # ============================================================

    def add_service(
        self,
        service_name,
        description,
        service_image
    ):

        self.fill_service_form(
            service_name=service_name,
            description=description,
            service_image=service_image
        )

        self.click_submit()

        time.sleep(4)

    # ============================================================
    # EDIT SERVICE
    # ============================================================

    def click_edit_service(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_BUTTON
            )
        )

        element.click()

        time.sleep(3)

        print(
            "Edit button clicked."
        )

    def enter_edit_service_name(
        self,
        service_name
    ):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_SERVICE_NAME
            )
        )

        element.click()

        element.clear()

        element.send_keys(
            service_name
        )

        time.sleep(1)

        print(
            "Updated service name:",
            service_name
        )

    def save_edit_service(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_SAVE_BUTTON
            )
        )

        element.click()

        time.sleep(4)

        print(
            "Service edit saved."
        )

    def edit_service(
        self,
        service_name
    ):

        self.click_edit_service()

        self.enter_edit_service_name(
            service_name
        )

        self.save_edit_service()

    # ============================================================
    # DELETE SERVICE
    # ============================================================

    def click_delete_service(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_BUTTON
            )
        )

        element.click()

        time.sleep(3)

        print(
            "Delete button clicked."
        )

    # ------------------------------------------------------------
    # CLOSE DELETE MODAL
    # ------------------------------------------------------------

    def close_delete_modal(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_MODAL_CLOSE
            )
        )

        element.click()

        time.sleep(2)

        print(
            "Delete modal closed."
        )

    # ------------------------------------------------------------
    # CANCEL DELETE
    # ------------------------------------------------------------

    def cancel_delete(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_CANCEL_BUTTON
            )
        )

        element.click()

        time.sleep(2)

        print(
            "Delete cancelled."
        )

    # ------------------------------------------------------------
    # CONFIRM DELETE
    # ------------------------------------------------------------

    def confirm_delete(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_CONFIRM_BUTTON
            )
        )

        element.click()

        time.sleep(4)

        print(
            "Service deleted."
        )

    # ------------------------------------------------------------
    # DELETE SERVICE
    # ------------------------------------------------------------

    def delete_service(self):

        self.click_delete_service()

        self.confirm_delete()

    # ============================================================
    # DELETE SECOND SERVICE
    # ============================================================

    def delete_second_service(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.SECOND_DELETE_BUTTON
            )
        )

        element.click()

        time.sleep(3)

        self.confirm_delete()

