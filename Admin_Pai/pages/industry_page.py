import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndustryPage:

    # ============================================================
    # URL
    # ============================================================

    INDUSTRY_URL = (
        "https://paiwebsiteqa.pineappleai.cloud/admin/industry"
    )

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
    # LEFT MENU
    # ============================================================

    INDUSTRY_MENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[3]/button/span'
    )

    INDUSTRY_SUBMENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[3]/div/button[3]'
    )

    # ============================================================
    # ADD INDUSTRY FORM
    # ============================================================

    INDUSTRY_INPUT = (
        By.ID,
        "industryName"
    )

    IMAGE_INPUT = (
        By.XPATH,
        '//input[@type="file"]'
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div/div/form/div[3]/button'
    )

    # ============================================================
    # INDUSTRY CARDS
    # ============================================================

    INDUSTRY_CARDS = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[3]/div'
    )

    # ============================================================
    # EDIT FORM
    # ============================================================

    EDIT_INDUSTRY_INPUT = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/form/div[1]/input'
    )

    # ============================================================
    # EDIT OLD IMAGE DELETE BUTTON
    # ============================================================

    EDIT_OLD_IMAGE_DELETE = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/form/div[2]/div/span[1]'
    )

    # ============================================================
    # EDIT SAVE BUTTON
    # ============================================================

    EDIT_SAVE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/form/div[3]/button'
    )

    # ============================================================
    # EDIT FORM
    # ============================================================

    EDIT_FORM = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div/form'
    )

    # ============================================================
    # DELETE MODAL
    # ============================================================

    DELETE_CANCEL_BUTTON = (
        By.XPATH,
        '/html/body/div/div/div/div[2]/div[2]/div/div[2]/button[1]'
    )

    DELETE_CONFIRM_BUTTON = (
        By.XPATH,
        '/html/body/div/div/div/div[2]/div[2]/div/div[2]/button[2]'
    )

    # ============================================================
    # NAVIGATION
    # ============================================================

    def click_industry_menu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.INDUSTRY_MENU
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        time.sleep(1)

    # ============================================================

    def click_industry_submenu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.INDUSTRY_SUBMENU
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        self.wait.until(
            EC.url_contains(
                "/admin/industry"
            )
        )

        time.sleep(2)

    # ============================================================

    def navigate_to_industry(self):

        self.click_industry_menu()

        self.click_industry_submenu()

    # ============================================================
    # INDUSTRY INPUT
    # ============================================================

    def enter_industry(self, industry):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.INDUSTRY_INPUT
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        element.click()

        element.send_keys(
            Keys.CONTROL,
            "a"
        )

        element.send_keys(
            Keys.BACKSPACE
        )

        if industry is not None:

            element.send_keys(
                industry
            )

        time.sleep(0.5)

    # ============================================================
    # GET INDUSTRY VALUE
    # ============================================================

    def get_industry_value(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.INDUSTRY_INPUT
            )
        )

        return element.get_attribute(
            "value"
        )

    # ============================================================
    # GENERAL IMAGE UPLOAD
    # ============================================================

    def upload_image(self, image_path):

        image_path = os.path.abspath(
            image_path
        )

        print(
            "Uploading image:",
            image_path
        )

        if not os.path.isfile(image_path):

            raise FileNotFoundError(
                f"\nImage file not found:\n{image_path}"
            )

        file_input = self.wait.until(
            EC.presence_of_element_located(
                self.IMAGE_INPUT
            )
        )

        file_input.send_keys(
            image_path
        )

        time.sleep(1)

        print(
            "Image uploaded successfully"
        )

    # ============================================================
    # JPG UPLOAD
    # ============================================================

    def upload_jpg(self, image_path):

        image_path = os.path.abspath(
            image_path
        )

        if not os.path.isfile(image_path):

            raise FileNotFoundError(
                f"\nJPG file not found:\n{image_path}"
            )

        if not image_path.lower().endswith(
            (".jpg", ".jpeg")
        ):

            raise ValueError(
                f"Expected JPG/JPEG image, "
                f"but received:\n{image_path}"
            )

        print(
            "Uploading JPG:",
            image_path
        )

        file_input = self.wait.until(
            EC.presence_of_element_located(
                self.IMAGE_INPUT
            )
        )

        file_input.send_keys(
            image_path
        )

        time.sleep(1)

        print(
            "JPG uploaded successfully"
        )

    # ============================================================
    # PNG UPLOAD
    # ============================================================

    def upload_png(self, image_path):

        image_path = os.path.abspath(
            image_path
        )

        if not os.path.isfile(image_path):

            raise FileNotFoundError(
                f"\nPNG file not found:\n{image_path}"
            )

        if not image_path.lower().endswith(
            ".png"
        ):

            raise ValueError(
                f"Expected PNG image, "
                f"but received:\n{image_path}"
            )

        print(
            "Uploading PNG:",
            image_path
        )

        file_input = self.wait.until(
            EC.presence_of_element_located(
                self.IMAGE_INPUT
            )
        )

        file_input.send_keys(
            image_path
        )

        time.sleep(1)

        print(
            "PNG uploaded successfully"
        )

    # ============================================================
    # CHECK IMAGE UPLOADED
    # ============================================================

    def is_image_uploaded(self):

        try:

            file_input = self.wait.until(
                EC.presence_of_element_located(
                    self.IMAGE_INPUT
                )
            )

            value = file_input.get_attribute(
                "value"
            )

            return bool(value)

        except Exception:

            return False

    # ============================================================
    # SUBMIT
    # ============================================================

    def click_submit(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(3)

    # ============================================================
    # FORM DISPLAYED
    # ============================================================

    def is_form_displayed(self):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(
                    self.INDUSTRY_INPUT
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # ============================================================
    # ADD INDUSTRY - GENERAL
    # ============================================================

    def add_industry(
        self,
        industry,
        image_path
    ):

        self.enter_industry(
            industry
        )

        self.upload_image(
            image_path
        )

        self.click_submit()

    # ============================================================
    # ADD INDUSTRY - JPG
    # ============================================================

    def add_industry_jpg(
        self,
        industry,
        image_path
    ):

        self.enter_industry(
            industry
        )

        self.upload_jpg(
            image_path
        )

        self.click_submit()

    # ============================================================
    # ADD INDUSTRY - PNG
    # ============================================================

    def add_industry_png(
        self,
        industry,
        image_path
    ):

        self.enter_industry(
            industry
        )

        self.upload_png(
            image_path
        )

        self.click_submit()

    # ============================================================
    # GET INDUSTRY CARDS
    # ============================================================

    def get_industry_cards(self):

        try:

            self.wait.until(
                EC.presence_of_element_located(
                    self.INDUSTRY_CARDS
                )
            )

        except Exception:

            return []

        return self.driver.find_elements(
            *self.INDUSTRY_CARDS
        )

    # ============================================================
    # WAIT FOR CARDS TO LOAD
    # ============================================================

    def wait_until_cards_loaded(
        self,
        timeout=15
    ):

        end_time = (
            time.time() + timeout
        )

        while time.time() < end_time:

            cards = self.driver.find_elements(
                *self.INDUSTRY_CARDS
            )

            if cards:

                return True

            time.sleep(0.5)

        return False

    # ============================================================
    # GET INDUSTRY NAME FROM CARD
    # ============================================================

    def get_industry_name_from_card(
        self,
        card
    ):

        try:

            text = card.text.strip()

            if not text:

                return None

            lines = [
                line.strip()
                for line in text.splitlines()
                if line.strip()
            ]

            ignored = {
                "edit",
                "delete",
                "cancel",
                "save",
                "close"
            }

            for line in lines:

                if line.lower() not in ignored:

                    return line

            return None

        except Exception:

            return None

    # ============================================================
    # GET ALL INDUSTRY NAMES
    # ============================================================

    def get_all_industry_names(self):

        names = []

        cards = self.get_industry_cards()

        for index, card in enumerate(
            cards,
            start=1
        ):

            name = (
                self.get_industry_name_from_card(
                    card
                )
            )

            if name:

                names.append(
                    name
                )

                print(
                    f"Industry {index}: {name}"
                )

        return names

    # ============================================================
    # GET FIRST EXISTING INDUSTRY
    # ============================================================

    def get_first_existing_industry(self):

        names = (
            self.get_all_industry_names()
        )

        if not names:

            raise AssertionError(
                "No existing industry found"
            )

        print(
            "Selected existing industry:",
            names[0]
        )

        return names[0]

    # ============================================================
    # FIND INDUSTRY CARD
    # ============================================================

    def find_industry_card(
        self,
        industry
    ):

        expected = (
            industry.strip().lower()
        )

        cards = self.get_industry_cards()

        for card in cards:

            card_industry = (
                self.get_industry_name_from_card(
                    card
                )
            )

            if not card_industry:

                continue

            actual = (
                card_industry.strip().lower()
            )

            if actual == expected:

                return card

        return None

    # ============================================================
    # CHECK INDUSTRY PRESENT
    # ============================================================

    def is_industry_present(
        self,
        industry
    ):

        return (
            self.find_industry_card(
                industry
            )
            is not None
        )

    # ============================================================
    # WAIT INDUSTRY PRESENT
    # ============================================================

    def wait_until_industry_present(
        self,
        industry,
        timeout=15
    ):

        end_time = (
            time.time() + timeout
        )

        expected = (
            industry.strip().lower()
        )

        while time.time() < end_time:

            if self.is_industry_present(
                industry
            ):

                return True

            time.sleep(0.5)

        return False

    # ============================================================
    # CLICK EDIT FOR SPECIFIC INDUSTRY
    # ============================================================

    def click_edit_for_industry(
        self,
        industry
    ):

        card = self.find_industry_card(
            industry
        )

        if card is None:

            raise AssertionError(
                f"Industry card not found: "
                f"{industry}"
            )

        try:

            edit_button = card.find_element(
                By.XPATH,
                './/div[2]/div/button[1]'
            )

        except Exception:

            edit_button = card.find_element(
                By.XPATH,
                './/button[1]'
            )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            edit_button
        )

        self.wait.until(
            lambda d:
            edit_button.is_displayed()
            and edit_button.is_enabled()
        )

        self.driver.execute_script(
            "arguments[0].click();",
            edit_button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_INDUSTRY_INPUT
            )
        )

        time.sleep(1)

        print(
            "Edit clicked for:",
            industry
        )

    # ============================================================
    # GET EDIT INPUT
    # ============================================================

    def get_edit_industry_input(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_INDUSTRY_INPUT
            )
        )

    # ============================================================
    # GET EDIT INDUSTRY VALUE
    # ============================================================

    def get_edit_industry_value(self):

        element = (
            self.get_edit_industry_input()
        )

        return (
            element.get_attribute(
                "value"
            )
        )

    # ============================================================
    # EDIT INDUSTRY NAME
    # ============================================================

    def edit_industry_name(
        self,
        new_name
    ):

        element = (
            self.get_edit_industry_input()
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        element.click()

        element.send_keys(
            Keys.CONTROL,
            "a"
        )

        time.sleep(0.2)

        element.send_keys(
            Keys.BACKSPACE
        )

        time.sleep(0.5)

        element.send_keys(
            new_name
        )

        time.sleep(0.8)

        actual_value = (
            element.get_attribute(
                "value"
            )
        )

        print(
            "New Industry Name:",
            actual_value
        )

        assert (
            actual_value == new_name
        ), (
            f"Edit input failed.\n"
            f"Expected: {new_name}\n"
            f"Actual: {actual_value}"
        )

    # ============================================================
    # NEW FUNCTION 1
    # EDIT EXISTING INDUSTRY NAME ONLY
    # ============================================================

    def edit_existing_industry_name(
        self,
        old_name,
        new_name
    ):

        print(
            "\nEditing existing industry name..."
        )

        self.click_edit_for_industry(
            old_name
        )

        assert self.is_edit_form_displayed(), (
            "Edit form was not displayed"
        )

        current_name = (
            self.get_edit_industry_value()
        )

        print(
            "Current Industry Name:",
            current_name
        )

        assert (
            current_name.strip().lower()
            == old_name.strip().lower()
        ), (
            f"Wrong industry opened.\n"
            f"Expected: {old_name}\n"
            f"Actual: {current_name}"
        )

        self.edit_industry_name(
            new_name
        )

        self.click_edit_save()

        assert self.wait_until_edit_form_closed(
            timeout=15
        ), (
            "Edit form did not close after save"
        )

        assert self.wait_until_industry_present(
            new_name,
            timeout=15
        ), (
            f"Updated industry was not found: "
            f"{new_name}"
        )

        assert not self.is_industry_present(
            old_name
        ), (
            f"Old industry name still exists: "
            f"{old_name}"
        )

        print(
            "Industry name updated successfully"
        )

    # ============================================================
    # NEW FUNCTION 2
    # EDIT INDUSTRY WITHOUT CHANGING IMAGE
    # ============================================================

    def edit_industry_without_changing_image(
        self,
        old_name,
        new_name
    ):

        print(
            "\nEditing industry without changing image..."
        )

        self.click_edit_for_industry(
            old_name
        )

        assert self.is_edit_form_displayed(), (
            "Edit form was not displayed"
        )

        current_name = (
            self.get_edit_industry_value()
        )

        print(
            "Current Industry Name:",
            current_name
        )

        assert (
            current_name.strip().lower()
            == old_name.strip().lower()
        ), (
            f"Wrong industry opened.\n"
            f"Expected: {old_name}\n"
            f"Actual: {current_name}"
        )

        # --------------------------------------------------------
        # DO NOT DELETE OLD IMAGE
        # DO NOT UPLOAD NEW IMAGE
        # --------------------------------------------------------

        print(
            "Existing image will remain unchanged"
        )

        self.edit_industry_name(
            new_name
        )

        self.click_edit_save()

        assert self.wait_until_edit_form_closed(
            timeout=15
        ), (
            "Edit form did not close after save"
        )

        assert self.wait_until_industry_present(
            new_name,
            timeout=15
        ), (
            f"Updated industry was not found: "
            f"{new_name}"
        )

        assert not self.is_industry_present(
            old_name
        ), (
            f"Old industry name still exists: "
            f"{old_name}"
        )

        print(
            "Industry name updated without changing image"
        )

    # ============================================================
    # EDIT FORM DISPLAYED
    # ============================================================

    def is_edit_form_displayed(self):

        try:

            element = (
                self.get_edit_industry_input()
            )

            return (
                element.is_displayed()
                and element.is_enabled()
            )

        except Exception:

            return False

    # ============================================================
    # DELETE OLD EDIT IMAGE
    # ============================================================

    def delete_old_edit_image(self):

        delete_image_button = self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_OLD_IMAGE_DELETE
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            delete_image_button
        )

        time.sleep(0.5)

        self.driver.execute_script(
            "arguments[0].click();",
            delete_image_button
        )

        time.sleep(1)

        print(
            "Old edit image delete button clicked"
        )

    # ============================================================
    # UPLOAD EDIT JPG
    # ============================================================

    def upload_edit_jpg(
        self,
        image_path
    ):

        image_path = os.path.abspath(
            image_path
        )

        if not os.path.isfile(image_path):

            raise FileNotFoundError(
                f"\nEdit JPG file not found:\n"
                f"{image_path}"
            )

        if not image_path.lower().endswith(
            (".jpg", ".jpeg")
        ):

            raise ValueError(
                f"Edit image must be JPG/JPEG:\n"
                f"{image_path}"
            )

        edit_file_inputs = self.driver.find_elements(
            By.XPATH,
            '//*[@id="root"]/div/div/div[2]/div[2]/div/form//input[@type="file"]'
        )

        if not edit_file_inputs:

            edit_file_inputs = self.driver.find_elements(
                *self.IMAGE_INPUT
            )

        if not edit_file_inputs:

            raise AssertionError(
                "No file input found in edit form"
            )

        file_input = edit_file_inputs[-1]

        self.driver.execute_script(
            "arguments[0].style.display='block';",
            file_input
        )

        file_input.send_keys(
            image_path
        )

        time.sleep(1)

        print(
            "Edit JPG uploaded:",
            image_path
        )

    # ============================================================
    # SAVE EDIT
    # ============================================================

    def click_edit_save(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_SAVE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        print(
            "Industry edit save button clicked"
        )

    # ============================================================
    # WAIT UNTIL EDIT FORM CLOSES
    # ============================================================

    def wait_until_edit_form_closed(
        self,
        timeout=15
    ):

        try:

            WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.invisibility_of_element_located(
                    self.EDIT_FORM
                )
            )

            print(
                "Edit form closed"
            )

            return True

        except Exception:

            return False

    # ============================================================
    # REFRESH INDUSTRY PAGE
    # ============================================================

    def refresh_industry_page(self):

        print(
            "Refreshing Industry page..."
        )

        self.driver.refresh()

        self.wait.until(
            EC.url_contains(
                "/admin/industry"
            )
        )

        self.wait_until_cards_loaded(
            timeout=15
        )

        time.sleep(2)

        print(
            "Industry page refreshed"
        )

    # ============================================================
    # CLICK FIRST EDIT
    # ============================================================

    def click_first_edit(self):

        cards = self.get_industry_cards()

        if not cards:

            raise AssertionError(
                "No industry cards found"
            )

        first_card = cards[0]

        edit_button = first_card.find_element(
            By.XPATH,
            './/div[2]/div/button[1]'
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            edit_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            edit_button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_INDUSTRY_INPUT
            )
        )

        time.sleep(1)

        print(
            "First Industry Edit button clicked"
        )

    # ============================================================
    # CLICK DELETE FOR SPECIFIC INDUSTRY
    # ============================================================

    def click_delete_for_industry(
        self,
        industry
    ):

        card = self.find_industry_card(
            industry
        )

        if card is None:

            raise AssertionError(
                f"Industry card not found: "
                f"{industry}"
            )

        try:

            delete_button = card.find_element(
                By.XPATH,
                './/div[2]/div/button[2]'
            )

        except Exception:

            delete_button = card.find_element(
                By.XPATH,
                './/button[2]'
            )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            delete_button
        )

        self.wait.until(
            lambda d:
            delete_button.is_displayed()
            and delete_button.is_enabled()
        )

        self.driver.execute_script(
            "arguments[0].click();",
            delete_button
        )

        time.sleep(2)

        print(
            "Delete clicked for:",
            industry
        )

    # ============================================================
    # CLICK FIRST DELETE
    # ============================================================

    def click_first_delete(self):

        cards = self.get_industry_cards()

        if not cards:

            raise AssertionError(
                "No industry cards found"
            )

        first_card = cards[0]

        delete_button = first_card.find_element(
            By.XPATH,
            './/div[2]/div/button[2]'
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            delete_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            delete_button
        )

        time.sleep(2)

        print(
            "First Industry Delete button clicked"
        )

    # ============================================================
    # DELETE MODAL DISPLAYED
    # ============================================================

    def is_delete_modal_displayed(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.DELETE_CANCEL_BUTTON
                )
            )

            self.wait.until(
                EC.visibility_of_element_located(
                    self.DELETE_CONFIRM_BUTTON
                )
            )

            return True

        except Exception:

            return False

    # ============================================================
    # CANCEL DELETE
    # ============================================================

    def cancel_delete(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_CANCEL_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(2)

        print(
            "Delete cancelled"
        )

    # ============================================================
    # CONFIRM DELETE
    # ============================================================

    def confirm_delete(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_CONFIRM_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(3)

        print(
            "Delete confirmed"
        )

    # ============================================================
    # WAIT UNTIL INDUSTRY DELETED
    # ============================================================

    def wait_until_industry_deleted(
        self,
        industry,
        timeout=15
    ):

        end_time = (
            time.time() + timeout
        )

        while time.time() < end_time:

            if not self.is_industry_present(
                industry
            ):

                print(
                    "Industry successfully deleted:",
                    industry
                )

                return True

            time.sleep(0.5)

        raise AssertionError(
            f"Industry was not deleted: "
            f"'{industry}'"
        )