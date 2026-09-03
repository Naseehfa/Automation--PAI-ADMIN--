
import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ============================================================
    # HOME / PRODUCT NAVIGATION
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
    # ADD PRODUCT FORM
    # ============================================================

    product_name_input = (
        By.ID,
        "productName"
    )

    product_website_input = (
        By.ID,
        "productWebsite"
    )

    product_photo_input = (
        By.ID,
        "productPhoto"
    )

    add_product_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/form/div[3]/button"
    )

    # ============================================================
    # PRODUCT LIST / EDIT
    # ============================================================

    edit_product_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div[10]/div[3]/div/button[1]/img"
    )

    update_product_name_input = (
        By.ID,
        "modalProductName"
    )

    update_product_website_input = (
        By.ID,
        "modalProductWebsite"
    )

    update_product_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/form/div[5]/button"
    )

    # ============================================================
    # DELETE
    # ============================================================

    delete_product_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div[1]/div[3]/div/button[2]/img"
    )

    delete_confirm_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/button"
    )

    delete_confirm_button_1 = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/button[1]"
    )

    delete_confirm_button_2 = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/button[2]"
    )

    # ============================================================
    # PAGINATION
    # ============================================================

    # Next page button - exact XPath supplied by user
    next_page_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[3]/div/div[2]/div[2]/button[2]/img"
    )

    # Previous page button - exact XPath supplied by user
    previous_page_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[3]/div/div[2]/div[2]/button[1]/img"
    )

    # Parent button of Next Page image
    next_page_button_parent = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[3]/div/div[2]/div[2]/button[2]"
    )

    # Parent button of Previous Page image
    previous_page_button_parent = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[3]/div/div[2]/div[2]/button[1]"
    )

    # ============================================================
    # PRODUCT ROW LOCATOR
    # ============================================================

    # Product list container from the existing page structure.
    #
    # This locator identifies the direct product items inside
    # the product-list area.
    #
    # If your application uses a different structure, this is
    # the only locator that may need adjustment.
    product_rows = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div"
    )

    # ============================================================
    # RANDOM LETTER GENERATOR
    # ============================================================

    def generate_random_letters(self, length=6):

        if length < 1:
            raise ValueError(
                "Length must be at least 1"
            )

        value = ''.join(
            random.choices(
                string.ascii_letters,
                k=length
            )
        )

        print(
            "\nGenerated Random Letters:",
            value
        )

        return value

    # ============================================================
    # LETTERS-ONLY PRODUCT NAME
    # ============================================================

    def generate_product_name_letters(
        self,
        prefix="Product"
    ):

        random_value = (
            self.generate_random_letters(
                length=6
            )
        )

        product_name = (
            f"{prefix} {random_value}"
        )

        print(
            "\nGenerated Product Name:",
            product_name
        )

        return product_name

    # ============================================================
    # ALPHANUMERIC GENERATOR
    # ============================================================

    def generate_alphanumeric_value(
        self,
        length=6
    ):

        if length < 2:
            raise ValueError(
                "Length must be at least 2"
            )

        characters = (
            string.ascii_letters +
            string.digits
        )

        value = [
            random.choice(
                string.ascii_letters
            ),
            random.choice(
                string.digits
            )
        ]

        value.extend(
            random.choices(
                characters,
                k=length - 2
            )
        )

        random.shuffle(value)

        value = ''.join(value)

        print(
            "\nGenerated Alphanumeric Value:",
            value
        )

        return value

    # ============================================================
    # ALPHANUMERIC PRODUCT NAME
    # ============================================================

    def generate_product_name(
        self,
        prefix="Product"
    ):

        random_value = (
            self.generate_alphanumeric_value(
                length=6
            )
        )

        product_name = (
            f"{prefix}{random_value}"
        )

        print(
            "\nGenerated Alphanumeric Product Name:",
            product_name
        )

        return product_name

    # ============================================================
    # HOME
    # ============================================================

    def click_home(self):

        print(
            "Clicking Home..."
        )

        home = self.wait.until(
            EC.element_to_be_clickable(
                self.home_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            home
        )

        time.sleep(1)

        home.click()

        time.sleep(3)

        print(
            "Home clicked."
        )

    # ============================================================
    # VERIFY HOME
    # ============================================================

    def verify_home_page(self):

        expected_url = (
            "https://paiwebsiteqa.pineappleai.cloud/admin/team"
        )

        self.wait.until(
            lambda d:
            d.current_url == expected_url
        )

        assert (
            self.driver.current_url ==
            expected_url
        )

        print(
            "Home page verified."
        )

    # ============================================================
    # PRODUCT SELECTION
    # ============================================================

    def click_product_selection(self):

        print(
            "Clicking Product Selection..."
        )

        product_button = self.wait.until(
            EC.element_to_be_clickable(
                self.product_selection_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            product_button
        )

        time.sleep(1)

        product_button.click()

        time.sleep(4)

        print(
            "Product Selection clicked."
        )

    # ============================================================
    # VERIFY PRODUCT SELECTION
    # ============================================================

    def verify_product_selection_page(self):

        expected_url = (
            "https://paiwebsiteqa.pineappleai.cloud/admin/product-selection"
        )

        self.wait.until(
            lambda d:
            d.current_url == expected_url
        )

        assert (
            self.driver.current_url ==
            expected_url
        )

        print(
            "Product Selection page verified."
        )

    # ============================================================
    # FILL ADD PRODUCT FORM
    # ============================================================

    def fill_product_form(
        self,
        product_name="",
        product_website="",
        product_photo=""
    ):

        name_field = self.wait.until(
            EC.visibility_of_element_located(
                self.product_name_input
            )
        )

        name_field.clear()

        if product_name:
            name_field.send_keys(
                product_name
            )

        website_field = self.wait.until(
            EC.visibility_of_element_located(
                self.product_website_input
            )
        )

        website_field.clear()

        if product_website:
            website_field.send_keys(
                product_website
            )

        if product_photo:

            photo_field = self.wait.until(
                EC.presence_of_element_located(
                    self.product_photo_input
                )
            )

            photo_field.send_keys(
                product_photo
            )

            time.sleep(2)

        print(
            "Product form completed."
        )

    # ============================================================
    # ADD PRODUCT
    # ============================================================

    def click_add_product(self):

        print(
            "Clicking Add Product..."
        )

        add_button = self.wait.until(
            EC.presence_of_element_located(
                self.add_product_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            add_button
        )

        time.sleep(1)

        try:
            add_button.click()

        except Exception:
            self.driver.execute_script(
                "arguments[0].click();",
                add_button
            )

        time.sleep(5)

        print(
            "Add Product clicked."
        )

    # ============================================================
    # OPEN FIRST PRODUCT EDIT FORM
    # ============================================================

    def open_first_product_edit(self):

        print(
            "\nOpening first product edit form..."
        )

        edit_button = self.wait.until(
            EC.element_to_be_clickable(
                self.edit_product_button
            )
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

        edit_button.click()

        time.sleep(3)

        self.wait.until(
            EC.visibility_of_element_located(
                self.update_product_name_input
            )
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.update_product_website_input
            )
        )

        print(
            "Edit form opened successfully."
        )

    # ============================================================
    # GET EDIT PRODUCT NAME
    # ============================================================

    def get_edit_product_name(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.update_product_name_input
            )
        )

        return field.get_attribute(
            "value"
        )

    # ============================================================
    # GET EDIT PRODUCT WEBSITE
    # ============================================================

    def get_edit_product_website(self):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.update_product_website_input
            )
        )

        return field.get_attribute(
            "value"
        )

    # ============================================================
    # SET REACT INPUT
    # ============================================================

    def set_react_input(
        self,
        locator,
        value
    ):

        field = self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            """
            const element = arguments[0];
            const value = arguments[1];

            const setter =
                Object.getOwnPropertyDescriptor(
                    HTMLInputElement.prototype,
                    'value'
                ).set;

            setter.call(element, value);

            element.dispatchEvent(
                new Event(
                    'input',
                    { bubbles: true }
                )
            );

            element.dispatchEvent(
                new Event(
                    'change',
                    { bubbles: true }
                )
            );

            element.dispatchEvent(
                new Event(
                    'blur',
                    { bubbles: true }
                )
            );
            """,
            field,
            value
        )

        time.sleep(0.5)

    # ============================================================
    # CHECK UPDATE BUTTON
    # ============================================================

    def is_update_button_enabled(self):

        button = self.wait.until(
            EC.presence_of_element_located(
                self.update_product_button
            )
        )

        disabled_attribute = (
            button.get_attribute("disabled")
        )

        aria_disabled = (
            button.get_attribute(
                "aria-disabled"
            )
        )

        class_name = (
            button.get_attribute("class")
            or ""
        )

        if disabled_attribute is not None:
            return False

        if aria_disabled == "true":
            return False

        try:
            if not button.is_enabled():
                return False
        except Exception:
            pass

        disabled_words = [
            "disabled",
            "cursor-not-allowed"
        ]

        for word in disabled_words:
            if word.lower() in class_name.lower():
                return False

        return True

    # ============================================================
    # CLICK UPDATE BUTTON
    # ============================================================

    def click_update_product(self):

        print(
            "\nClicking Update button..."
        )

        update_button = self.wait.until(
            EC.presence_of_element_located(
                self.update_product_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            update_button
        )

        time.sleep(1)

        try:
            update_button.click()

        except Exception:
            self.driver.execute_script(
                "arguments[0].click();",
                update_button
            )

        time.sleep(5)

        print(
            "Update button clicked."
        )

    # ============================================================
    # UPDATE FIRST PRODUCT
    # ============================================================

    def update_first_product(
        self,
        new_name=None,
        new_website=None
    ):

        self.open_first_product_edit()

        if new_name is not None:

            self.set_react_input(
                self.update_product_name_input,
                new_name
            )

        if new_website is not None:

            self.set_react_input(
                self.update_product_website_input,
                new_website
            )

        time.sleep(1)

        self.click_update_product()

        print(
            "Product update completed."
        )

    # ============================================================
    # PRODUCT NAME SORT
    # ============================================================

    def click_product_name_sort(self):

        product_name_header = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//th[normalize-space()='Product Name']"
                    "|//button[normalize-space()='Product Name']"
                )
            )
        )

        product_name_header.click()

        time.sleep(3)

    # ============================================================
    # PRODUCT WEBSITE SORT
    # ============================================================

    def click_product_website_sort(self):

        product_website_header = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//th[normalize-space()='Product Website']"
                    "|//button[normalize-space()='Product Website']"
                )
            )
        )

        product_website_header.click()

        time.sleep(3)

    # ============================================================
    # VERIFY PRODUCT INFORMATION
    # ============================================================

    def verify_product_data_in_listing(
        self,
        product_name,
        product_website
    ):

        body_text = self.driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert product_name in body_text, (
            f"Product Name not found in listing: "
            f"{product_name}"
        )

        assert product_website in body_text, (
            f"Product Website not found in listing: "
            f"{product_website}"
        )

    # ============================================================
    # DELETE PRODUCT
    # ============================================================

    def delete_product_confirm(self):

        delete_button = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_product_button
            )
        )

        delete_button.click()

        time.sleep(2)

        confirm_button = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_confirm_button
            )
        )

        confirm_button.click()

        time.sleep(5)

    # ============================================================
    # DELETE BUTTON 1
    # ============================================================

    def delete_product_confirm_button_1(self):

        delete_button = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_product_button
            )
        )

        delete_button.click()

        time.sleep(2)

        confirm_button = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_confirm_button_1
            )
        )

        confirm_button.click()

        time.sleep(5)

    # ============================================================
    # DELETE BUTTON 2
    # ============================================================

    def delete_product_confirm_button_2(self):

        delete_button = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_product_button
            )
        )

        delete_button.click()

        time.sleep(2)

        confirm_button = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_confirm_button_2
            )
        )

        confirm_button.click()

        time.sleep(5)

    # ============================================================
    # PAGINATION - GET PRODUCT ROW COUNT
    # ============================================================

    def get_displayed_product_count(self):

        """
        Returns the number of product rows currently
        displayed on the current pagination page.
        """

        time.sleep(2)

        rows = self.driver.find_elements(
            *self.product_rows
        )

        visible_rows = []

        for row in rows:

            try:

                if row.is_displayed():

                    text = (
                        row.text
                        .strip()
                    )

                    # Ignore empty containers
                    if text:

                        visible_rows.append(
                            row
                        )

            except Exception:
                continue

        count = len(
            visible_rows
        )

        print(
            "\nDisplayed product count:",
            count
        )

        return count

    # ============================================================
    # PAGINATION - NEXT PAGE
    # ============================================================

    def click_next_page(self):

        print(
            "\nClicking Next Page..."
        )

        next_button = self.wait.until(
            EC.presence_of_element_located(
                self.next_page_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            next_button
        )

        time.sleep(1)

        try:

            next_button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                next_button
            )

        time.sleep(3)

        print(
            "Next Page clicked."
        )

    # ============================================================
    # PAGINATION - PREVIOUS PAGE
    # ============================================================

    def click_previous_page(self):

        print(
            "\nClicking Previous Page..."
        )

        previous_button = self.wait.until(
            EC.presence_of_element_located(
                self.previous_page_button
            )
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            previous_button
        )

        time.sleep(1)

        try:

            previous_button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                previous_button
            )

        time.sleep(3)

        print(
            "Previous Page clicked."
        )

    # ============================================================
    # PAGINATION - CHECK NEXT BUTTON
    # ============================================================

    def is_next_page_enabled(self):

        button = self.wait.until(
            EC.presence_of_element_located(
                self.next_page_button_parent
            )
        )

        disabled = (
            button.get_attribute("disabled")
        )

        aria_disabled = (
            button.get_attribute(
                "aria-disabled"
            )
        )

        if disabled is not None:
            return False

        if aria_disabled == "true":
            return False

        try:

            if not button.is_enabled():
                return False

        except Exception:
            pass

        return True

    # ============================================================
    # PAGINATION - CHECK PREVIOUS BUTTON
    # ============================================================

    def is_previous_page_enabled(self):

        button = self.wait.until(
            EC.presence_of_element_located(
                self.previous_page_button_parent
            )
        )

        disabled = (
            button.get_attribute("disabled")
        )

        aria_disabled = (
            button.get_attribute(
                "aria-disabled"
            )
        )

        if disabled is not None:
            return False

        if aria_disabled == "true":
            return False

        try:

            if not button.is_enabled():
                return False

        except Exception:
            pass

        return True

