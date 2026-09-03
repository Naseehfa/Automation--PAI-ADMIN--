import os
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
    # SIDEBAR LOCATORS
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
    # PRODUCT FORM LOCATORS
    # ============================================================

    product_name_input = (By.ID, "productName")
    product_website_input = (By.ID, "productWebsite")
    product_photo_input = (By.ID, "productPhoto")

    add_product_button = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/form/div[3]/button"
    )

    # ============================================================
    # PRODUCT LISTING
    # ============================================================

    # Header locators.
    # These use visible header text so they are less dependent
    # on changing div indexes.

    product_name_header = (
        By.XPATH,
        "//th[normalize-space()='Product Name']"
        "|//button[normalize-space()='Product Name']"
        "|//*[normalize-space()='Product Name']"
    )

    product_website_header = (
        By.XPATH,
        "//th[normalize-space()='Product Website']"
        "|//button[normalize-space()='Product Website']"
        "|//*[normalize-space()='Product Website']"
    )

    # Product listing rows.
    product_rows = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[2]/div[3]/div"
    )

    # ============================================================
    # UPDATE PRODUCT LOCATORS
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
    # DELETE PRODUCT LOCATORS
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
    # RANDOM LETTER GENERATOR
    # ============================================================

    def generate_random_letters(self, length=6):

        if length < 1:
            raise ValueError("Length must be at least 1")

        value = ''.join(
            random.choices(
                string.ascii_letters,
                k=length
            )
        )

        print("\nGenerated Random Letters:", value)

        return value

    # ============================================================
    # RANDOM ALPHANUMERIC GENERATOR
    # ============================================================

    def generate_alphanumeric_value(self, length=6):

        if length < 2:
            raise ValueError(
                "Length must be at least 2"
            )

        characters = (
            string.ascii_letters +
            string.digits
        )

        value = [
            random.choice(string.ascii_letters),
            random.choice(string.digits)
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
            "\nGenerated Guaranteed Alphanumeric Value:",
            value
        )

        return value

    # ============================================================
    # PRODUCT NAME - LETTERS ONLY
    # ============================================================

    def generate_product_name_letters(
        self,
        prefix="Product"
    ):

        random_value = (
            self.generate_random_letters(6)
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
    # PRODUCT NAME - ALPHANUMERIC
    # ============================================================

    def generate_product_name(
        self,
        prefix="Product"
    ):

        random_value = (
            self.generate_alphanumeric_value(6)
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
    # CLICK HOME
    # ============================================================

    def click_home(self):

        print("Clicking Home...")

        home = self.wait.until(
            EC.element_to_be_clickable(
                self.home_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            home
        )

        time.sleep(1)

        home.click()

        time.sleep(3)

        print("Home clicked.")

    # ============================================================
    # VERIFY HOME PAGE
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

        print("Home page verified.")

    # ============================================================
    # CLICK PRODUCT SELECTION
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
            "arguments[0].scrollIntoView({block:'center'});",
            product_button
        )

        time.sleep(1)

        product_button.click()

        time.sleep(4)

        print(
            "Product Selection clicked."
        )

    # ============================================================
    # VERIFY PRODUCT SELECTION PAGE
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
    # FILL PRODUCT FORM
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

            print(
                "Uploading product photo..."
            )

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
    # CLICK ADD PRODUCT
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
            "arguments[0].scrollIntoView({block:'center'});",
            add_button
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.add_product_button
            )
        )

        try:
            add_button.click()

        except Exception:
            self.driver.execute_script(
                "arguments[0].click();",
                add_button
            )

        time.sleep(5)

    # ============================================================
    # OPEN FIRST PRODUCT EDIT FORM
    # ============================================================

    def open_first_product_edit(self):

        print(
            "\nOpening first product for editing..."
        )

        edit_button = self.wait.until(
            EC.element_to_be_clickable(
                self.edit_product_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            edit_button
        )

        edit_button.click()

        time.sleep(3)

        self.wait.until(
            EC.visibility_of_element_located(
                self.update_product_name_input
            )
        )

        print(
            "Edit form opened."
        )

    # ============================================================
    # GET EDIT FORM PRODUCT NAME
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
    # GET EDIT FORM WEBSITE
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
    # SET REACT INPUT VALUE
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
                new Event('input', {bubbles: true})
            );

            element.dispatchEvent(
                new Event('change', {bubbles: true})
            );
            """,
            field,
            value
        )

    # ============================================================
    # UPDATE PRODUCT
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

        print(
            "Updated values entered."
        )

        update_button = self.wait.until(
            EC.element_to_be_clickable(
                self.update_product_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            update_button
        )

        update_button.click()

        time.sleep(6)

        print(
            "Update button clicked."
        )

    # ============================================================
    # SORT PRODUCT NAME
    # ============================================================

    def click_product_name_sort(self):

        header = self.wait.until(
            EC.element_to_be_clickable(
                self.product_name_header
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            header
        )

        header.click()

        time.sleep(3)

    # ============================================================
    # SORT PRODUCT WEBSITE
    # ============================================================

    def click_product_website_sort(self):

        header = self.wait.until(
            EC.element_to_be_clickable(
                self.product_website_header
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            header
        )

        header.click()

        time.sleep(3)

    # ============================================================
    # GET PRODUCT LISTING TEXT
    # ============================================================

    def get_product_listing_text(self):

        rows = self.driver.find_elements(
            *self.product_rows
        )

        values = []

        for row in rows:

            text = row.text.strip()

            if text:
                values.append(text)

        return values

    # ============================================================
    # VERIFY PRODUCT DATA IS DISPLAYED
    # ============================================================

    def verify_product_data_in_listing(
        self,
        product_name,
        product_website
    ):

        page_text = self.driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert product_name in page_text, (
            f"Product name not displayed: "
            f"{product_name}"
        )

        assert product_website in page_text, (
            f"Product website not displayed: "
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
    # DELETE - BUTTON 1
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
    # DELETE - BUTTON 2
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