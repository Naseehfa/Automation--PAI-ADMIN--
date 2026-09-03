import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClientReviewPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ============================================================
    # LOCATORS
    # ============================================================

    # ------------------------------------------------------------
    # Main menu / Home dropdown
    # ------------------------------------------------------------

    main_menu = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[1]/button/span"
    )

    # ------------------------------------------------------------
    # Client Review menu
    # ------------------------------------------------------------

    client_review_menu = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[1]/div/button[2]"
    )

    # ============================================================
    # ADD CLIENT REVIEW FORM
    # ============================================================

    client_name = (
        By.ID,
        "clientName"
    )

    client_role = (
        By.ID,
        "clientRole"
    )

    client_photo = (
        By.ID,
        "clientPhoto"
    )

    review_text = (
        By.ID,
        "reviewText"
    )

    add_client_review_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/form/div[4]/button"
    )

    # ============================================================
    # EDIT CLIENT REVIEW
    # ============================================================

    # Edit button of first client review
    edit_client_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div[6]/div[4]/div/button[1]/img"
    )

    # ------------------------------------------------------------
    # Edit Client Name
    # ------------------------------------------------------------

    edit_client_name = (
        By.ID,
        "editClientName"
    )

    # ------------------------------------------------------------
    # Edit Client Role
    # ------------------------------------------------------------

    edit_client_role = (
        By.ID,
        "editClientRole"
    )

    # ------------------------------------------------------------
    # Edit Client Photo
    # ------------------------------------------------------------

    edit_client_photo = (
        By.ID,
        "editClientPhoto"
    )

    # ------------------------------------------------------------
    # Edit Review Text
    # ------------------------------------------------------------

    edit_review_text = (
        By.ID,
        "editReviewText"
    )

    # ------------------------------------------------------------
    # Update button
    # ------------------------------------------------------------

    update_client_btn = (
        By.XPATH,
        "/html/body/div[2]/div/form/div[5]/button"
    )

    # ============================================================
    # DELETE CLIENT REVIEW
    # ============================================================

    # Delete icon for the client review
    delete_client_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div[9]/div[4]/div/button[2]/img"
    )

    # Confirmation modal
    confirm_delete_modal = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div"
    )

    # Confirmation modal - Delete button
    confirm_delete_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/button[2]"
    )

    # Confirmation modal - Cancel button
    cancel_delete_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/button[1]"
    )

    # ============================================================
    # NAVIGATION
    # ============================================================

    def click_main_menu(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.main_menu
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        time.sleep(1)

        button.click()

        time.sleep(1)

    # ------------------------------------------------------------

    def click_client_review(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.client_review_menu
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        time.sleep(1)

        button.click()

        time.sleep(2)

        self.wait.until(
            EC.url_contains(
                "/admin/client-review"
            )
        )

    # ------------------------------------------------------------

    def navigate_to_client_review(self):

        self.click_main_menu()

        self.click_client_review()

        time.sleep(2)

    # ============================================================
    # CLIENT NAME
    # ============================================================

    def enter_client_name(self, name):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.client_name
            )
        )

        field.clear()

        field.send_keys(name)

        time.sleep(0.5)

    # ============================================================
    # CLIENT ROLE
    # ============================================================

    def enter_client_role(self, role):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.client_role
            )
        )

        field.clear()

        field.send_keys(role)

        time.sleep(0.5)

    # ============================================================
    # CLIENT PHOTO
    # ============================================================

    def upload_client_photo(self, image_path):

        photo = self.wait.until(
            EC.presence_of_element_located(
                self.client_photo
            )
        )

        photo.send_keys(image_path)

        time.sleep(1)

    # ============================================================
    # REVIEW TEXT
    # ============================================================

    def enter_review_text(self, review):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.review_text
            )
        )

        field.clear()

        field.send_keys(review)

        time.sleep(0.5)

    # ============================================================
    # ADD CLIENT REVIEW
    # ============================================================

    def click_add_client_review(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.add_client_review_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        time.sleep(1)

        button.click()

        time.sleep(2)

    # ============================================================
    # FILL COMPLETE ADD FORM
    # ============================================================

    def fill_client_review_form(
        self,
        name,
        role,
        photo,
        review
    ):

        self.enter_client_name(name)

        self.enter_client_role(role)

        self.upload_client_photo(photo)

        self.enter_review_text(review)

        time.sleep(1)

    # ============================================================
    # GET FIELD VALUES
    # ============================================================

    def get_client_name_value(self):

        return self.driver.find_element(
            *self.client_name
        ).get_attribute("value")

    # ------------------------------------------------------------

    def get_client_role_value(self):

        return self.driver.find_element(
            *self.client_role
        ).get_attribute("value")

    # ------------------------------------------------------------

    def get_review_text_value(self):

        return self.driver.find_element(
            *self.review_text
        ).get_attribute("value")

    # ============================================================
    # VALIDATION CHECKS
    # ============================================================

    def is_client_name_error(self):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.client_name
            )
        )

        class_name = element.get_attribute("class") or ""

        return "error" in class_name

    # ------------------------------------------------------------

    def is_client_role_error(self):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.client_role
            )
        )

        class_name = element.get_attribute("class") or ""

        return "error" in class_name

    # ------------------------------------------------------------

    def is_review_text_error(self):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.review_text
            )
        )

        class_name = element.get_attribute("class") or ""

        return "error" in class_name

    # ============================================================
    # EDIT CLIENT REVIEW
    # ============================================================

    def click_edit_client(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.edit_client_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        time.sleep(1)

        button.click()

        time.sleep(2)

    # ============================================================
    # CLEAR FIELD COMPLETELY
    # ============================================================

    def clear_field(self, locator):

        field = self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

        field.click()

        field.send_keys(
            Keys.CONTROL,
            "a"
        )

        field.send_keys(
            Keys.BACKSPACE
        )

        time.sleep(0.5)

    # ============================================================
    # EDIT CLIENT NAME
    # ============================================================

    def enter_edit_client_name(self, name):

        self.clear_field(
            self.edit_client_name
        )

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.edit_client_name
            )
        )

        field.send_keys(name)

        time.sleep(0.5)

    # ============================================================
    # EDIT CLIENT ROLE
    # ============================================================

    def enter_edit_client_role(self, role):

        self.clear_field(
            self.edit_client_role
        )

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.edit_client_role
            )
        )

        field.send_keys(role)

        time.sleep(0.5)

    # ============================================================
    # EDIT REVIEW TEXT
    # ============================================================

    def enter_edit_review_text(self, review):

        self.clear_field(
            self.edit_review_text
        )

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.edit_review_text
            )
        )

        field.send_keys(review)

        time.sleep(0.5)

    # ============================================================
    # EDIT CLIENT PHOTO
    # ============================================================

    def upload_edit_client_photo(self, image_path):

        photo = self.wait.until(
            EC.presence_of_element_located(
                self.edit_client_photo
            )
        )

        photo.send_keys(image_path)

        time.sleep(1)

    # ============================================================
    # UPDATE CLIENT REVIEW
    # ============================================================

    def click_update_client(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.update_client_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        time.sleep(1)

        button.click()

        time.sleep(2)

    # ============================================================
    # UPDATE ALL CLIENT REVIEW FIELDS
    # ============================================================

    def update_client_review(
        self,
        name=None,
        role=None,
        photo=None,
        review=None
    ):

        self.click_edit_client()

        # --------------------------------------------------------
        # Update Client Name
        # --------------------------------------------------------

        if name is not None:

            self.enter_edit_client_name(
                name
            )

        # --------------------------------------------------------
        # Update Client Role
        # --------------------------------------------------------

        if role is not None:

            self.enter_edit_client_role(
                role
            )

        # --------------------------------------------------------
        # Update Client Photo
        # --------------------------------------------------------

        if photo is not None:

            self.upload_edit_client_photo(
                photo
            )

        # --------------------------------------------------------
        # Update Review
        # --------------------------------------------------------

        if review is not None:

            self.enter_edit_review_text(
                review
            )

        # --------------------------------------------------------
        # Save changes
        # --------------------------------------------------------

        self.click_update_client()

        time.sleep(2)

    # ============================================================
    # UPDATE ONLY CLIENT NAME
    # ============================================================

    def update_client_name(self, name):

        self.click_edit_client()

        self.enter_edit_client_name(
            name
        )

        self.click_update_client()

        time.sleep(2)

    # ============================================================
    # UPDATE ONLY CLIENT ROLE
    # ============================================================

    def update_client_role(self, role):

        self.click_edit_client()

        self.enter_edit_client_role(
            role
        )

        self.click_update_client()

        time.sleep(2)

    # ============================================================
    # UPDATE ONLY REVIEW
    # ============================================================

    def update_client_review_text(self, review):

        self.click_edit_client()

        self.enter_edit_review_text(
            review
        )

        self.click_update_client()

        time.sleep(2)

    # ============================================================
    # UPDATE ONLY PHOTO
    # ============================================================

    def update_client_photo(self, photo):

        self.click_edit_client()

        self.upload_edit_client_photo(
            photo
        )

        self.click_update_client()

        time.sleep(2)

    # ============================================================
    # DELETE CLIENT REVIEW
    # ============================================================

    def click_delete_client(self):

        # --------------------------------------------------------
        # Locate delete icon
        # --------------------------------------------------------

        delete_icon = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_client_btn
            )
        )

        # --------------------------------------------------------
        # Scroll to delete icon
        # --------------------------------------------------------

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            delete_icon
        )

        time.sleep(1)

        # --------------------------------------------------------
        # Click delete icon
        # --------------------------------------------------------

        delete_icon.click()

        # --------------------------------------------------------
        # Wait for confirmation modal
        # --------------------------------------------------------

        self.wait.until(
            EC.visibility_of_element_located(
                self.confirm_delete_modal
            )
        )

        time.sleep(1)

    # ============================================================
    # VERIFY DELETE CONFIRMATION POPUP
    # ============================================================

    def is_delete_confirmation_displayed(self):

        try:

            modal = self.wait.until(
                EC.visibility_of_element_located(
                    self.confirm_delete_modal
                )
            )

            return modal.is_displayed()

        except Exception:

            return False

    # ============================================================
    # CONFIRM DELETE
    # ============================================================

    def confirm_delete_client(self):

        confirm_button = self.wait.until(
            EC.element_to_be_clickable(
                self.confirm_delete_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            confirm_button
        )

        time.sleep(0.5)

        confirm_button.click()

        # --------------------------------------------------------
        # Wait for confirmation modal to disappear
        # --------------------------------------------------------

        self.wait.until(
            EC.invisibility_of_element_located(
                self.confirm_delete_modal
            )
        )

        time.sleep(2)

    # ============================================================
    # CANCEL DELETE
    # ============================================================

    def cancel_delete_client(self):

        cancel_button = self.wait.until(
            EC.element_to_be_clickable(
                self.cancel_delete_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            cancel_button
        )

        time.sleep(0.5)

        cancel_button.click()

        # --------------------------------------------------------
        # Wait for confirmation modal to disappear
        # --------------------------------------------------------

        self.wait.until(
            EC.invisibility_of_element_located(
                self.confirm_delete_modal
            )
        )

        time.sleep(1)

    # ============================================================
    # CHECK DELETE COMPLETED
    # ============================================================

    def is_delete_completed(self):

        try:

            # The confirmation popup should disappear
            # after successful confirmation.

            self.wait.until(
                EC.invisibility_of_element_located(
                    self.confirm_delete_modal
                )
            )

            return True

        except Exception:

            return False

    # ============================================================
    # COMPLETE DELETE
    # ============================================================

    def delete_client_review(self):

        # Click delete icon
        self.click_delete_client()

        # Confirm deletion
        self.confirm_delete_client()

        # Verify completed
        return self.is_delete_completed()