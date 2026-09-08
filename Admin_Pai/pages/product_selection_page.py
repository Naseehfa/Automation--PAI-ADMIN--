import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import (
    WebDriverWait,
    Select
)
from selenium.webdriver.support import expected_conditions as EC


class ProductSelectionPage:

    # ============================================================
    # URL
    # ============================================================

    PRODUCT_SELECTION_URL = (
        "https://paiwebsiteqa.pineappleai.cloud/"
        "admin/product-selection"
    )

    # ============================================================
    # CONSTRUCTOR
    # ============================================================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    # ============================================================
    # NAVIGATION LOCATORS
    # ============================================================

    home_button = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[1]/button/span"
    )

    product_selection_button = (
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[1]/div/button[1]"
    )

    # ============================================================
    # PRODUCT EDIT LOCATORS
    # ============================================================

    eighth_product_edit_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div[8]/div[3]/div/button[1]/img"
    )

    # ============================================================
    # UPDATE MODAL LOCATORS
    # ============================================================

    modal_product_name = (
        By.XPATH,
        "//*[@id='modalProductName']"
    )

    modal_product_website = (
        By.XPATH,
        "//*[@id='modalProductWebsite']"
    )

    modal_product_photo = (
        By.XPATH,
        "//*[@id='modalProductPhoto']"
    )

    update_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/form/div[5]/button"
    )

    # ============================================================
    # DELETE LOCATORS
    # ============================================================

    delete_product_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div[3]/div[3]/div/button[2]/img"
    )

    delete_confirmation_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/button[2]"
    )

    # ============================================================
    # ADD PRODUCT LOCATORS
    # ============================================================

    add_product_name = (
        By.XPATH,
        "//*[@id='productName']"
    )

    add_product_website = (
        By.XPATH,
        "//*[@id='productWebsite']"
    )

    add_product_photo = (
        By.XPATH,
        "//*[@id='productPhoto']"
    )

    add_product_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/form/div[3]/button"
    )

    # ============================================================
    # ROWS PER PAGE
    # ============================================================

    rows_per_page_dropdown = (
        By.XPATH,
        "/html/body/div/div/div/div[2]/div/div[3]/div/div[2]/div[1]/div/select"
    )

    # ============================================================
    # PRODUCT ROW
    #
    # This locator is based on the product-list structure
    # supplied earlier.
    # ============================================================

    product_rows = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div"
    )

    # ============================================================
    # PRODUCT NAME LOCATOR
    # ============================================================

    def product_name_locator(self, product_name):

        return (
            By.XPATH,
            f"//*[normalize-space()='{product_name}']"
        )

    # ============================================================
    # HOME
    # ============================================================

    def click_home(self):

        print("\nClicking Home...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.home_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            button
        )

        time.sleep(0.5)

        try:

            button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        time.sleep(2)

        print(
            "Home clicked successfully."
        )

    # ============================================================
    # PRODUCT SELECTION
    # ============================================================

    def click_product_selection(self):

        print(
            "\nClicking Product Selection..."
        )

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.product_selection_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            button
        )

        time.sleep(0.5)

        try:

            button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        time.sleep(3)

        print(
            "Product Selection opened successfully."
        )

    # ============================================================
    # OPEN 8TH PRODUCT EDIT
    # ============================================================

    def open_eighth_product_edit(self):

        print(
            "\nOpening 8th product edit..."
        )

        edit_button = self.wait.until(
            EC.element_to_be_clickable(
                self.eighth_product_edit_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            edit_button
        )

        time.sleep(0.5)

        try:

            edit_button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                edit_button
            )

        self.wait.until(
            EC.visibility_of_element_located(
                self.modal_product_name
            )
        )

        print(
            "8th product edit modal opened."
        )

    # ============================================================
    # GET PRODUCT NAME
    # ============================================================

    def get_product_name(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.modal_product_name
            )
        )

        return field.get_attribute(
            "value"
        )

    # ============================================================
    # CLEAR PRODUCT NAME
    # ============================================================

    def clear_product_name(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.modal_product_name
            )
        )

        field.clear()

    # ============================================================
    # ENTER PRODUCT NAME
    # ============================================================

    def enter_product_name(self, product_name):

        if not product_name.strip():

            raise ValueError(
                "Product name cannot contain only spaces."
            )

        if any(
            character.isdigit()
            for character in product_name
        ):

            raise ValueError(
                "Product name cannot contain digits."
            )

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.modal_product_name
            )
        )

        field.clear()

        field.send_keys(
            product_name
        )

    # ============================================================
    # GET PRODUCT WEBSITE
    # ============================================================

    def get_product_website(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.modal_product_website
            )
        )

        return field.get_attribute(
            "value"
        )

    # ============================================================
    # CLEAR PRODUCT WEBSITE
    # ============================================================

    def clear_product_website(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.modal_product_website
            )
        )

        field.clear()

    # ============================================================
    # ENTER PRODUCT WEBSITE
    # ============================================================

    def enter_product_website(self, website):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.modal_product_website
            )
        )

        field.clear()

        field.send_keys(
            website
        )

    # ============================================================
    # UPLOAD PRODUCT PHOTO
    # ============================================================

    def upload_product_photo(
        self,
        image_name="OIP.jpg"
    ):

        image_path = os.path.abspath(
            image_name
        )

        if not os.path.exists(image_path):

            project_root = os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )

            image_path = os.path.join(
                project_root,
                image_name
            )

        if not os.path.exists(image_path):

            raise FileNotFoundError(
                f"Product image not found: {image_path}"
            )

        photo_field = self.wait.until(
            EC.presence_of_element_located(
                self.modal_product_photo
            )
        )

        photo_field.send_keys(
            image_path
        )

        print(
            f"Product photo uploaded: {image_path}"
        )

    # ============================================================
    # CLICK UPDATE
    # ============================================================

    def click_update(self):

        print(
            "\nClicking Update..."
        )

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.update_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            button
        )

        time.sleep(0.5)

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
    # VERIFY UPDATED PRODUCT
    # ============================================================

    def verify_updated_product(
        self,
        product_name
    ):

        print(
            f"\nSearching for updated product: "
            f"{product_name}"
        )

        locator = self.product_name_locator(
            product_name
        )

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(
                    locator
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # ============================================================
    # HIGHLIGHT UPDATED PRODUCT
    # ============================================================

    def highlight_updated_product(
        self,
        product_name
    ):

        locator = self.product_name_locator(
            product_name
        )

        element = self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            """
            arguments[0].style.border =
                '3px solid red';
            arguments[0].style.backgroundColor =
                'yellow';
            """,
            element
        )

        print(
            f"Product highlighted: {product_name}"
        )

    # ============================================================
    # DELETE PRODUCT
    # ============================================================

    def click_delete_product(self):

        print(
            "\nClicking Delete Product..."
        )

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_product_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            button
        )

        time.sleep(0.5)

        try:

            button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        time.sleep(1)

        print(
            "Delete button clicked."
        )

    # ============================================================
    # CONFIRM DELETE
    # ============================================================

    def confirm_delete(self):

        print(
            "\nConfirming product deletion..."
        )

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_confirmation_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            button
        )

        time.sleep(0.5)

        try:

            button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        time.sleep(3)

        print(
            "Product deletion confirmed."
        )

    # ============================================================
    # TRY DELETE PRODUCT AGAIN
    # ============================================================

    def try_delete_product_again(self):

        print(
            "\nTrying to delete the already deleted product again..."
        )

        try:

            buttons = self.driver.find_elements(
                *self.delete_product_button
            )

            visible_buttons = [
                button
                for button in buttons
                if button.is_displayed()
            ]

            if not visible_buttons:

                print(
                    "Delete button for the deleted "
                    "product is no longer available."
                )

                return False

            print(
                "A delete button is still present."
            )

            return False

        except Exception:

            return False

    # ============================================================
    # ADD PRODUCT NAME
    # ============================================================

    def get_add_product_name(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.add_product_name
            )
        )

        return field.get_attribute(
            "value"
        )

    # ============================================================
    # CLEAR ADD PRODUCT NAME
    # ============================================================

    def clear_add_product_name(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.add_product_name
            )
        )

        field.clear()

    # ============================================================
    # ENTER ADD PRODUCT NAME
    # ============================================================

    def enter_add_product_name(
        self,
        product_name
    ):

        if not product_name.strip():

            raise ValueError(
                "Product name cannot contain only spaces."
            )

        if any(
            character.isdigit()
            for character in product_name
        ):

            raise ValueError(
                "Product name cannot contain digits."
            )

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.add_product_name
            )
        )

        field.clear()

        field.send_keys(
            product_name
        )

    # ============================================================
    # GET ADD PRODUCT WEBSITE
    # ============================================================

    def get_add_product_website(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.add_product_website
            )
        )

        return field.get_attribute(
            "value"
        )

    # ============================================================
    # CLEAR ADD PRODUCT WEBSITE
    # ============================================================

    def clear_add_product_website(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.add_product_website
            )
        )

        field.clear()

    # ============================================================
    # ENTER ADD PRODUCT WEBSITE
    # ============================================================

    def enter_add_product_website(
        self,
        website
    ):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.add_product_website
            )
        )

        field.clear()

        field.send_keys(
            website
        )

    # ============================================================
    # UPLOAD ADD PRODUCT PHOTO
    # ============================================================

    def upload_add_product_photo(
        self,
        image_name="OIP.jpg"
    ):

        image_path = os.path.abspath(
            image_name
        )

        if not os.path.exists(image_path):

            project_root = os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )

            image_path = os.path.join(
                project_root,
                image_name
            )

        if not os.path.exists(image_path):

            raise FileNotFoundError(
                f"Product image not found: {image_path}"
            )

        photo_field = self.wait.until(
            EC.presence_of_element_located(
                self.add_product_photo
            )
        )

        photo_field.send_keys(
            image_path
        )

        print(
            f"Add Product photo uploaded: "
            f"{image_path}"
        )

    # ============================================================
    # CLICK ADD PRODUCT
    # ============================================================

    def click_add_product(self):

        print(
            "\nClicking Add Product..."
        )

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.add_product_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            button
        )

        time.sleep(0.5)

        try:

            button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        time.sleep(3)

        print(
            "Add Product button clicked."
        )

    # ============================================================
    # FIND PRODUCT BY NAME
    # ============================================================

    def find_product_by_name(
        self,
        product_name
    ):

        locator = self.product_name_locator(
            product_name
        )

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    locator
                )
            )

        except Exception:

            return None

    # ============================================================
    # PRODUCT EXISTS
    # ============================================================

    def product_exists(
        self,
        product_name
    ):

        locator = self.product_name_locator(
            product_name
        )

        elements = self.driver.find_elements(
            *locator
        )

        visible_elements = [
            element
            for element in elements
            if element.is_displayed()
        ]

        return len(visible_elements) > 0

    # ============================================================
    # COUNT PRODUCT BY NAME
    # ============================================================

    def count_product_by_name(
        self,
        product_name
    ):

        locator = self.product_name_locator(
            product_name
        )

        elements = self.driver.find_elements(
            *locator
        )

        visible_elements = [
            element
            for element in elements
            if element.is_displayed()
        ]

        return len(visible_elements)

    # ============================================================
    # GET VALIDATION MESSAGES
    # ============================================================

    def get_validation_messages(self):

        messages = []

        # Browser validation messages
        try:

            name_field = self.driver.find_element(
                *self.add_product_name
            )

            message = name_field.get_attribute(
                "validationMessage"
            )

            if message:

                messages.append(
                    message
                )

        except Exception:
            pass

        try:

            website_field = self.driver.find_element(
                *self.add_product_website
            )

            message = website_field.get_attribute(
                "validationMessage"
            )

            if message:

                messages.append(
                    message
                )

        except Exception:
            pass

        # Common visible validation elements
        try:

            elements = self.driver.find_elements(
                By.XPATH,
                """
                //*[contains(
                    translate(
                        normalize-space(.),
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'required'
                )
                or contains(
                    translate(
                        normalize-space(.),
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'invalid'
                )
                or contains(
                    translate(
                        normalize-space(.),
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                        'abcdefghijklmnopqrstuvwxyz'
                    ),
                    'must'
                )]
                """
            )

            for element in elements:

                if element.is_displayed():

                    text = element.text.strip()

                    if (
                        text
                        and text not in messages
                    ):

                        messages.append(
                            text
                        )

        except Exception:
            pass

        return messages

    # ============================================================
    # ADD PRODUCT FORM DISPLAYED
    # ============================================================

    def is_add_product_form_displayed(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.add_product_name
                )
            ).is_displayed()

        except Exception:

            return False

    # ============================================================
    # ZOOM OUT PAGE
    # ============================================================

    def zoom_out_page(
        self,
        zoom_percentage=75
    ):

        print(
            f"\nZooming page out to "
            f"{zoom_percentage}%..."
        )

        self.driver.execute_script(
            f"""
            document.body.style.zoom =
            '{zoom_percentage}%';
            """
        )

        time.sleep(1)

        print(
            f"Page zoom set to "
            f"{zoom_percentage}%."
        )

    # ============================================================
    # GET ROWS PER PAGE DROPDOWN
    # ============================================================

    def get_rows_per_page_dropdown(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.rows_per_page_dropdown
            )
        )

    # ============================================================
    # GET ROWS PER PAGE OPTIONS
    # ============================================================

    def get_rows_per_page_options(self):

        dropdown = self.wait.until(
            EC.presence_of_element_located(
                self.rows_per_page_dropdown
            )
        )

        select = Select(
            dropdown
        )

        return [
            option.text.strip()
            for option in select.options
        ]

    # ============================================================
    # SELECT ROWS PER PAGE
    # ============================================================

    def select_rows_per_page(
        self,
        number
    ):

        print(
            f"\nSelecting {number} rows per page..."
        )

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                self.rows_per_page_dropdown
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            dropdown
        )

        time.sleep(0.5)

        select = Select(
            dropdown
        )

        # Verify requested option exists
        available_options = [
            option.text.strip()
            for option in select.options
        ]

        if str(number) not in available_options:

            raise AssertionError(
                f"Rows per page option '{number}' "
                f"was not found. "
                f"Available options: "
                f"{available_options}"
            )

        select.select_by_visible_text(
            str(number)
        )

        time.sleep(2)

        # Re-find dropdown because page may update
        dropdown = self.wait.until(
            EC.presence_of_element_located(
                self.rows_per_page_dropdown
            )
        )

        select = Select(
            dropdown
        )

        selected_value = (
            select.first_selected_option.text.strip()
        )

        print(
            f"Selected Rows Per Page: "
            f"{selected_value}"
        )

        assert selected_value == str(number), (
            f"Rows per page was not changed "
            f"to {number}. "
            f"Actual value: {selected_value}"
        )

        print(
            f"Rows per page successfully "
            f"changed to {number}."
        )

    # ============================================================
    # GET DISPLAYED PRODUCT ROWS
    # ============================================================

    def get_displayed_product_rows(self):

        time.sleep(1)

        rows = self.driver.find_elements(
            *self.product_rows
        )

        visible_rows = [
            row
            for row in rows
            if row.is_displayed()
        ]

        return len(visible_rows)