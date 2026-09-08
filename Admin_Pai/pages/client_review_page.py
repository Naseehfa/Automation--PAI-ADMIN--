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

    main_menu = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[1]/button/span"
    )

    client_review_menu = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[1]/div/button[2]"
    )

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
    # EDIT LOCATORS
    # ============================================================

    edit_client_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div[6]/div[4]/div/button[1]/img"
    )

    edit_client_name = (
        By.ID,
        "editClientName"
    )

    edit_client_role = (
        By.ID,
        "editClientRole"
    )

    edit_client_photo = (
        By.ID,
        "editClientPhoto"
    )

    edit_review_text = (
        By.ID,
        "editReviewText"
    )

    update_client_btn = (
        By.XPATH,
        "/html/body/div[2]/div/form/div[5]/button"
    )

    # ============================================================
    # DELETE LOCATORS
    # ============================================================

    delete_client_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div[9]/div[4]/div/button[2]/img"
    )

    confirm_delete_modal = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div"
    )

    confirm_delete_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/button[2]"
    )

    cancel_delete_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/button[1]"
    )

    # ============================================================
    # NAVIGATION
    # ============================================================

    def navigate_to_client_review(self):

        menu = self.wait.until(
            EC.element_to_be_clickable(
                self.main_menu
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            menu
        )

        time.sleep(1)

        menu.click()

        client_review = self.wait.until(
            EC.element_to_be_clickable(
                self.client_review_menu
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            client_review
        )

        time.sleep(1)

        client_review.click()

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

    # ============================================================
    # CLIENT PHOTO
    # ============================================================

    def upload_client_photo(self, image_path):

        field = self.wait.until(
            EC.presence_of_element_located(
                self.client_photo
            )
        )

        field.send_keys(image_path)

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
    # GET CLIENT NAME VALUE
    # ============================================================

    def get_client_name_value(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.client_name
            )
        )

        return field.get_attribute("value")

    # ============================================================
    # GET CLIENT ROLE VALUE
    # ============================================================

    def get_client_role_value(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.client_role
            )
        )

        return field.get_attribute("value")

    # ============================================================
    # GET REVIEW TEXT VALUE
    # ============================================================

    def get_review_text_value(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.review_text
            )
        )

        return field.get_attribute("value")

    # ============================================================
    # CHECK VALIDATION MESSAGE
    # ============================================================

    def is_validation_message_displayed(self):

        try:

            validation = self.driver.find_elements(
                By.XPATH,
                "//*[contains(@class,'error') or contains(@class,'text-red')]"
            )

            return len(validation) > 0

        except Exception:

            return False

    # ============================================================
    # EDIT CLIENT REVIEW
    # ============================================================

    def click_edit_client(self):

        edit_icon = self.wait.until(
            EC.element_to_be_clickable(
                self.edit_client_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            edit_icon
        )

        time.sleep(1)

        edit_icon.click()

        time.sleep(2)

    # ============================================================
    # ENTER EDIT CLIENT NAME
    # ============================================================

    def enter_edit_client_name(self, name):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.edit_client_name
            )
        )

        field.click()

        field.send_keys(
            Keys.CONTROL,
            "a"
        )

        field.send_keys(name)

    # ============================================================
    # ENTER EDIT CLIENT ROLE
    # ============================================================

    def enter_edit_client_role(self, role):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.edit_client_role
            )
        )

        field.click()

        field.send_keys(
            Keys.CONTROL,
            "a"
        )

        field.send_keys(role)

    # ============================================================
    # UPLOAD EDIT CLIENT PHOTO
    # ============================================================

    def upload_edit_client_photo(self, image_path):

        field = self.wait.until(
            EC.presence_of_element_located(
                self.edit_client_photo
            )
        )

        field.send_keys(image_path)

    # ============================================================
    # ENTER EDIT REVIEW
    # ============================================================

    def enter_edit_review_text(self, review):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.edit_review_text
            )
        )

        field.click()

        field.send_keys(
            Keys.CONTROL,
            "a"
        )

        field.send_keys(review)

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
    # DELETE ICON ONLY
    #
    # IMPORTANT:
    # This method ONLY clicks the Delete icon.
    #
    # It does NOT click Yes/Delete.
    # It does NOT click No/Cancel.
    # ============================================================

    def click_delete_icon_only(self):

        delete_icon = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_client_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            delete_icon
        )

        time.sleep(1)

        delete_icon.click()

        time.sleep(1)

    # ============================================================
    # CLICK DELETE CLIENT
    #
    # Normal delete flow:
    # Click Delete icon and wait for confirmation popup.
    # ============================================================

    def click_delete_client(self):

        self.click_delete_icon_only()

        self.wait.until(
            EC.visibility_of_element_located(
                self.confirm_delete_modal
            )
        )

        time.sleep(1)

    # ============================================================
    # CHECK DELETE CONFIRMATION POPUP
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
    #
    # Click Yes/Delete button.
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

        self.wait.until(
            EC.invisibility_of_element_located(
                self.confirm_delete_modal
            )
        )

        time.sleep(2)

    # ============================================================
    # CANCEL DELETE
    #
    # Click No/Cancel button.
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

        self.wait.until(
            EC.invisibility_of_element_located(
                self.confirm_delete_modal
            )
        )

        time.sleep(1)

    # ============================================================
    # CHECK CLIENT REVIEW IS DISPLAYED
    #
    # This checks whether the Delete icon belonging to the
    # client review is still present.
    # ============================================================

    def is_client_review_displayed(self):

        try:

            element = self.wait.until(
                EC.presence_of_element_located(
                    self.delete_client_btn
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # ============================================================
    # CHECK CLIENT REVIEW IS DELETED
    # ============================================================

    def is_client_review_deleted(self):

        try:

            self.wait.until(
                EC.invisibility_of_element_located(
                    self.delete_client_btn
                )
            )

            return True

        except Exception:

            return False

    # ============================================================
    # CHECK DELETE COMPLETED
    #
    # Confirmation popup must disappear and client review
    # should no longer be displayed.
    # ============================================================

    def is_delete_completed(self):

        try:

            self.wait.until(
                EC.invisibility_of_element_located(
                    self.confirm_delete_modal
                )
            )

            time.sleep(1)

            return self.is_client_review_deleted()

        except Exception:

            return False

    # ============================================================
    # COMPLETE DELETE CLIENT REVIEW
    #
    # Delete icon
    #       ↓
    # Confirmation popup
    #       ↓
    # Yes/Delete
    #       ↓
    # Record deleted
    # ============================================================

    def delete_client_review(self):

        self.click_delete_client()

        self.confirm_delete_client()

        return self.is_delete_completed()