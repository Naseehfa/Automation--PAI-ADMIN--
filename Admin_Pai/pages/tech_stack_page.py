
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class TechStackPage:

    # ============================================================
    # URL
    # ============================================================

    TECH_STACK_URL = (
        "https://paiwebsiteqa.pineappleai.cloud/admin/tech-stack"
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

    TECH_STACK_MENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[3]/button/span'
    )

    TECH_STACK_SUBMENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[3]/div/button[2]'
    )

    # ============================================================
    # ADD FORM
    # ============================================================

    TECHNOLOGY_INPUT = (
        By.ID,
        "technology"
    )

    CATEGORY_DROPDOWN = (
        By.XPATH,
        '/html/body/div/div/div/div[2]/div/div/form/div[1]/div[2]/select'
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
    # TECHNOLOGY CARDS
    # ============================================================

    TECHNOLOGY_CARDS = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[3]/div'
    )

    # ============================================================
    # EDIT
    # ============================================================

    # Exact edit button structure supplied by user.
    # The card number is intentionally NOT hardcoded.
    EDIT_BUTTON_INSIDE_CARD = (
        By.XPATH,
        './/div[3]/div/button[1]'
    )

    # Exact edit technology input supplied by user.
    EDIT_TECHNOLOGY_INPUT = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[3]/div/form/div[1]/input'
    )

    # Exact edit category dropdown supplied by user.
    EDIT_CATEGORY_DROPDOWN = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[3]/div/form/div[2]/select'
    )

    # Exact save button supplied by user.
    EDIT_SAVE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[3]/div/form/div[5]/button'
    )

    # Edit form
    EDIT_FORM = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[3]/div/form'
    )

    # ============================================================
    # DELETE MODAL
    # ============================================================

    DELETE_CANCEL_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[3]/div/div[2]/button[1]'
    )

    DELETE_CONFIRM_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[3]/div/div[2]/button[2]'
    )

    # ============================================================
    # NAVIGATION
    # ============================================================

    def click_tech_stack_menu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.TECH_STACK_MENU
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

    def click_tech_stack_submenu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.TECH_STACK_SUBMENU
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
                "/admin/tech-stack"
            )
        )

        time.sleep(2)

    # ============================================================

    def navigate_to_tech_stack(self):

        self.click_tech_stack_menu()

        self.click_tech_stack_submenu()

    # ============================================================
    # ADD TECHNOLOGY
    # ============================================================

    def enter_technology(self, technology):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.TECHNOLOGY_INPUT
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

        if technology is not None:

            element.send_keys(
                technology
            )

        time.sleep(0.5)

    # ============================================================

    def get_technology_value(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.TECHNOLOGY_INPUT
            )
        )

        return element.get_attribute(
            "value"
        )

    # ============================================================
    # CATEGORY
    # ============================================================

    def get_category_dropdown(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.CATEGORY_DROPDOWN
            )
        )

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
            "\nAvailable Tech Stack Categories:"
        )

        for option in select.options:

            print(
                "-",
                option.text.strip(),
                "| value =",
                option.get_attribute("value")
            )

    # ============================================================

    def select_category(self, category):

        dropdown = self.get_category_dropdown()

        select = Select(
            dropdown
        )

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

            available = [
                option.text.strip()
                for option in select.options
                if option.text.strip()
            ]

            raise ValueError(
                f"Invalid Tech Stack Category: "
                f"'{category}'. "
                f"Available categories: {available}"
            )

        select.select_by_visible_text(
            matching_text
        )

        time.sleep(0.5)

        selected = (
            select.first_selected_option
            .text
            .strip()
        )

        assert (
            selected.lower()
            == matching_text.lower()
        ), (
            f"Category selection failed. "
            f"Expected: {matching_text}, "
            f"Actual: {selected}"
        )

        print(
            "Selected Category:",
            selected
        )

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
    # IMAGE
    # ============================================================

    def upload_image(self, image_path):

        image_path = os.path.abspath(
            image_path
        )

        if not os.path.isfile(image_path):

            raise FileNotFoundError(
                f"Image file not found:\n{image_path}"
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
            "Tech Stack image uploaded:",
            image_path
        )

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

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON
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

        time.sleep(3)

    # ============================================================
    # FORM
    # ============================================================

    def is_form_displayed(self):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(
                    self.TECHNOLOGY_INPUT
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # ============================================================
    # FILL FORM
    # ============================================================

    def fill_tech_stack_form(
        self,
        technology=None,
        category=None,
        image_path=None
    ):

        if technology is not None:

            self.enter_technology(
                technology
            )

        if category is not None:

            self.select_category(
                category
            )

        if image_path is not None:

            self.upload_image(
                image_path
            )

    # ============================================================
    # ADD TECH STACK
    # ============================================================

    def add_tech_stack(
        self,
        technology,
        category,
        image_path
    ):

        self.fill_tech_stack_form(
            technology=technology,
            category=category,
            image_path=image_path
        )

        self.click_submit()

    # ============================================================
    # URL
    # ============================================================

    def is_on_tech_stack_page(self):

        return (
            "/admin/tech-stack"
            in self.driver.current_url
        )

    # ============================================================
    # GET CARDS
    # ============================================================

    def get_technology_cards(self):

        try:

            self.wait.until(
                EC.presence_of_element_located(
                    self.TECHNOLOGY_CARDS
                )
            )

        except Exception:

            return []

        return self.driver.find_elements(
            *self.TECHNOLOGY_CARDS
        )

    # ============================================================
    # GET TECHNOLOGY NAME FROM CARD
    # ============================================================

    def get_technology_name_from_card(
        self,
        card
    ):

        try:

            lines = [
                line.strip()
                for line in card.text.splitlines()
                if line.strip()
            ]

            print(
                "Card lines:",
                lines
            )

            ignored = {
                "edit",
                "delete",
                "cancel",
                "save",
                "close"
            }

            meaningful_lines = [
                line
                for line in lines
                if line.lower() not in ignored
            ]

            if len(meaningful_lines) >= 1:

                return meaningful_lines[0]

            return None

        except Exception:

            return None

    # ============================================================
    # GET FIRST EXISTING TECHNOLOGY
    # ============================================================

    def get_first_existing_technology(self):

        cards = self.get_technology_cards()

        if not cards:

            raise AssertionError(
                "No technology cards found"
            )

        for index, card in enumerate(
            cards,
            start=1
        ):

            print(
                f"\nTechnology Card {index}:"
            )

            print(
                card.text
            )

            technology = (
                self.get_technology_name_from_card(
                    card
                )
            )

            if technology:

                print(
                    "Selected existing technology:",
                    technology
                )

                return technology

        raise AssertionError(
            "Could not identify technology name"
        )

    # ============================================================
    # FIND TECHNOLOGY CARD
    # ============================================================

    def find_technology_card(
        self,
        technology
    ):

        expected = (
            technology.strip().lower()
        )

        cards = self.get_technology_cards()

        for card in cards:

            card_technology = (
                self.get_technology_name_from_card(
                    card
                )
            )

            if not card_technology:

                continue

            actual = (
                card_technology.strip().lower()
            )

            if actual == expected:

                return card

        return None

    # ============================================================
    # CHECK TECHNOLOGY
    # ============================================================

    def is_technology_present(
        self,
        technology
    ):

        return (
            self.find_technology_card(
                technology
            )
            is not None
        )

    # ============================================================
    # CLICK EDIT FOR SPECIFIC TECHNOLOGY
    # ============================================================

    def click_edit_for_technology(
        self,
        technology
    ):

        print(
            "\nFinding technology for edit:",
            technology
        )

        card = self.find_technology_card(
            technology
        )

        if card is None:

            raise AssertionError(
                f"Technology card not found: "
                f"'{technology}'"
            )

        # --------------------------------------------------------
        # Exact structure:
        #
        # div[3]/div/button[1]/img
        #
        # We click the BUTTON, not the IMG.
        # --------------------------------------------------------

        edit_button = card.find_element(
            *self.EDIT_BUTTON_INSIDE_CARD
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

        time.sleep(0.5)

        self.driver.execute_script(
            "arguments[0].click();",
            edit_button
        )

        # --------------------------------------------------------
        # Wait for exact edit input
        # --------------------------------------------------------

        self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_TECHNOLOGY_INPUT
            )
        )

        time.sleep(1)

        print(
            "Edit clicked for:",
            technology
        )

    # ============================================================
    # GET EDIT TECHNOLOGY INPUT
    # ============================================================

    def get_edit_technology_input(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_TECHNOLOGY_INPUT
            )
        )

        self.wait.until(
            lambda d:
            element.is_displayed()
            and element.is_enabled()
        )

        return element

    # ============================================================
    # GET EDIT TECHNOLOGY VALUE
    # ============================================================

    def get_edit_technology_value(self):

        element = (
            self.get_edit_technology_input()
        )

        return (
            element.get_attribute(
                "value"
            )
        )

    # ============================================================
    # EDIT TECHNOLOGY NAME
    # ============================================================

    def edit_technology_name(
        self,
        new_name
    ):

        element = (
            self.get_edit_technology_input()
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

        time.sleep(0.3)

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
            "New edit technology value:",
            actual_value
        )

        assert (
            actual_value == new_name
        ), (
            f"Technology input update failed.\n"
            f"Expected: '{new_name}'\n"
            f"Actual: '{actual_value}'"
        )

        print(
            "New Technology Name:",
            new_name
        )

    # ============================================================
    # EDIT FORM DISPLAYED
    # ============================================================

    def is_edit_form_displayed(self):

        try:

            element = (
                self.get_edit_technology_input()
            )

            return (
                element.is_displayed()
                and element.is_enabled()
            )

        except Exception:

            return False

    # ============================================================
    # GET EDIT CATEGORY DROPDOWN
    # ============================================================

    def get_edit_category_dropdown(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_CATEGORY_DROPDOWN
            )
        )

    # ============================================================
    # GET CURRENT EDIT CATEGORY
    # ============================================================

    def get_edit_selected_category(self):

        dropdown = (
            self.get_edit_category_dropdown()
        )

        select = Select(
            dropdown
        )

        return (
            select.first_selected_option
            .text
            .strip()
        )

    # ============================================================
    # SELECT EDIT CATEGORY
    # ============================================================

    def select_edit_category(
        self,
        category
    ):

        dropdown = (
            self.get_edit_category_dropdown()
        )

        self.wait.until(
            lambda d:
            dropdown.is_enabled()
        )

        select = Select(
            dropdown
        )

        category = category.strip()

        matching_text = None

        for option in select.options:

            option_text = (
                option.text.strip()
            )

            if (
                option_text.lower()
                == category.lower()
            ):

                matching_text = option_text

                break

        if matching_text is None:

            available = [
                option.text.strip()
                for option in select.options
                if option.text.strip()
            ]

            raise ValueError(
                f"Invalid Edit Category: "
                f"'{category}'. "
                f"Available categories: {available}"
            )

        select.select_by_visible_text(
            matching_text
        )

        time.sleep(0.5)

        selected = (
            select.first_selected_option
            .text
            .strip()
        )

        assert (
            selected.lower()
            == matching_text.lower()
        ), (
            f"Edit category selection failed.\n"
            f"Expected: {matching_text}\n"
            f"Actual: {selected}"
        )

        print(
            "Edit Category Selected:",
            selected
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

        time.sleep(0.5)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        print(
            "Technology edit save button clicked"
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
    # NEW FUNCTION 1
    # EDIT EXISTING TECHNOLOGY NAME
    # ============================================================

    def edit_existing_technology_name(
        self,
        old_name,
        new_name
    ):

        print(
            "\n========== "
            "EDIT EXISTING TECHNOLOGY NAME "
            "=========="
        )

        self.click_edit_for_technology(
            old_name
        )

        assert self.is_edit_form_displayed(), (
            "Edit form was not displayed"
        )

        current_name = (
            self.get_edit_technology_value()
        )

        print(
            "Current Technology Name:",
            current_name
        )

        assert (
            current_name.strip().lower()
            == old_name.strip().lower()
        ), (
            f"Wrong technology opened.\n"
            f"Expected: {old_name}\n"
            f"Actual: {current_name}"
        )

        self.edit_technology_name(
            new_name
        )

        self.click_edit_save()

        assert self.wait_until_edit_form_closed(
            timeout=15
        ), (
            "Edit form did not close after save"
        )

        assert self.wait_until_technology_present(
            new_name,
            timeout=15
        ), (
            f"Updated technology was not found: "
            f"{new_name}"
        )

        assert not self.is_technology_present(
            old_name
        ), (
            f"Old technology name still exists: "
            f"{old_name}"
        )

        print(
            "Technology name updated successfully"
        )

    # ============================================================
    # NEW FUNCTION 2
    # EDIT TECHNOLOGY WITHOUT CHANGING IMAGE
    # ============================================================

    def edit_technology_without_changing_image(
        self,
        old_name,
        new_name
    ):

        print(
            "\n========== "
            "EDIT WITHOUT CHANGING IMAGE "
            "=========="
        )

        self.click_edit_for_technology(
            old_name
        )

        assert self.is_edit_form_displayed(), (
            "Edit form was not displayed"
        )

        current_name = (
            self.get_edit_technology_value()
        )

        print(
            "Current Technology Name:",
            current_name
        )

        assert (
            current_name.strip().lower()
            == old_name.strip().lower()
        ), (
            f"Wrong technology opened.\n"
            f"Expected: {old_name}\n"
            f"Actual: {current_name}"
        )

        # --------------------------------------------------------
        # IMPORTANT:
        #
        # DO NOT DELETE OLD IMAGE
        # DO NOT UPLOAD NEW IMAGE
        #
        # The existing image remains unchanged.
        # --------------------------------------------------------

        print(
            "Existing image will remain unchanged"
        )

        self.edit_technology_name(
            new_name
        )

        self.click_edit_save()

        assert self.wait_until_edit_form_closed(
            timeout=15
        ), (
            "Edit form did not close after save"
        )

        assert self.wait_until_technology_present(
            new_name,
            timeout=15
        ), (
            f"Updated technology was not found: "
            f"{new_name}"
        )

        assert not self.is_technology_present(
            old_name
        ), (
            f"Old technology still exists: "
            f"{old_name}"
        )

        print(
            "Technology updated without changing image"
        )

    # ============================================================
    # NEW FUNCTION 3
    # EDIT TECHNOLOGY CATEGORY
    # ============================================================

    def edit_technology_category(
        self,
        technology,
        new_category
    ):

        print(
            "\n========== "
            "EDIT TECHNOLOGY CATEGORY "
            "=========="
        )

        self.click_edit_for_technology(
            technology
        )

        assert self.is_edit_form_displayed(), (
            "Edit form was not displayed"
        )

        current_name = (
            self.get_edit_technology_value()
        )

        assert (
            current_name.strip().lower()
            == technology.strip().lower()
        ), (
            f"Wrong technology opened.\n"
            f"Expected: {technology}\n"
            f"Actual: {current_name}"
        )

        current_category = (
            self.get_edit_selected_category()
        )

        print(
            "Current Category:",
            current_category
        )

        self.select_edit_category(
            new_category
        )

        self.click_edit_save()

        assert self.wait_until_edit_form_closed(
            timeout=15
        ), (
            "Edit form did not close after category save"
        )

        assert self.wait_until_technology_present(
            technology,
            timeout=15
        ), (
            f"Technology was not found after "
            f"category update: {technology}"
        )

        print(
            "Technology category updated successfully"
        )

    # ============================================================
    # REFRESH PAGE
    # ============================================================

    def refresh_tech_stack_page(self):

        print(
            "Refreshing Tech Stack page..."
        )

        self.driver.refresh()

        self.wait.until(
            EC.url_contains(
                "/admin/tech-stack"
            )
        )

        self.wait_until_cards_loaded(
            timeout=15
        )

        time.sleep(2)

        print(
            "Tech Stack page refreshed"
        )

    # ============================================================
    # WAIT TECHNOLOGY PRESENT
    # ============================================================

    def wait_until_technology_present(
        self,
        technology,
        timeout=15
    ):

        end_time = (
            time.time() + timeout
        )

        while time.time() < end_time:

            if self.is_technology_present(
                technology
            ):

                return True

            time.sleep(0.5)

        return False

    # ============================================================
    # DELETE
    # ============================================================

    def click_delete_for_technology(
        self,
        technology
    ):

        card = self.find_technology_card(
            technology
        )

        if card is None:

            raise AssertionError(
                f"Technology card not found: "
                f"{technology}"
            )

        delete_button = card.find_element(
            By.XPATH,
            './/div[3]/div/button[2]'
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
            technology
        )

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
            "arguments[0].click();",
            button
        )

        time.sleep(3)

        print(
            "Delete confirmed"
        )

    # ============================================================
    # WAIT DELETE
    # ============================================================

    def wait_until_technology_deleted(
        self,
        technology,
        timeout=15
    ):

        end_time = (
            time.time() + timeout
        )

        while time.time() < end_time:

            if not self.is_technology_present(
                technology
            ):

                print(
                    "Technology successfully deleted:",
                    technology
                )

                return

            time.sleep(0.5)

        raise AssertionError(
            f"Technology was not deleted: "
            f"'{technology}'"
        )

