import os
import string
import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import (
    WebDriverWait,
    Select
)
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.product_selection_page import ProductSelectionPage
from utils.driver_setup import get_driver


# ============================================================
# TEST DATA
# ============================================================

LOGIN_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/login"
)

USERNAME = "admin@pineappleai.com"

PASSWORD = "SecureAdmin123!"


# ============================================================
# IMAGE PATH
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

IMAGE_PATH = os.path.join(
    PROJECT_ROOT,
    "OIP.jpg"
)


# ============================================================
# HELPER FUNCTION
# ============================================================

def generate_letters(length=8):

    """
    Generate letters only.

    Example:
        AbCdEfGh

    No numbers.
    No spaces.
    No special characters.
    """

    return "".join(
        random.choices(
            string.ascii_letters,
            k=length
        )
    )


# ============================================================
# HELPER FUNCTION
# ============================================================

def generate_timestamp():

    return str(
        int(
            time.time()
        )
    )













# ============================================================
# TEST 2
# Verify repeated deletion of an already deleted
# product is prevented
# ============================================================

def test_verify_repeated_deletion_of_already_deleted_product_is_prevented():

    driver = get_driver()

    try:

        print(
            "\n============================================================"
        )

        print(
            "TEST 2: Verify Repeated Deletion "
            "Of Already Deleted Product Is Prevented"
        )

        print(
            "============================================================"
        )

        wait = WebDriverWait(
            driver,
            20
        )

        # --------------------------------------------------------
        # STEP 1
        # Open Login Page
        # --------------------------------------------------------

        print(
            "\nSTEP 1: Open Login Page"
        )

        driver.get(
            LOGIN_URL
        )

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "email")
            )
        )

        # --------------------------------------------------------
        # STEP 2
        # Login
        # --------------------------------------------------------

        print(
            "\nSTEP 2: Login as Admin"
        )

        login_page = LoginPage(
            driver
        )

        login_page.login(
            USERNAME,
            PASSWORD
        )

        time.sleep(3)

        print(
            "Admin login successful."
        )

        # --------------------------------------------------------
        # STEP 3
        # Create Page Object
        # --------------------------------------------------------

        product_page = ProductSelectionPage(
            driver
        )

        # --------------------------------------------------------
        # STEP 4
        # Home
        # --------------------------------------------------------

        print(
            "\nSTEP 4: Navigate to Home"
        )

        product_page.click_home()

        # --------------------------------------------------------
        # STEP 5
        # Product Selection
        # --------------------------------------------------------

        print(
            "\nSTEP 5: Open Product Selection"
        )

        product_page.click_product_selection()

        # --------------------------------------------------------
        # STEP 6
        # Delete Product
        # --------------------------------------------------------

        print(
            "\nSTEP 6: Click Delete"
        )

        product_page.click_delete_product()

        # --------------------------------------------------------
        # STEP 7
        # Confirm Delete
        # --------------------------------------------------------

        print(
            "\nSTEP 7: Confirm Delete"
        )

        product_page.confirm_delete()

        time.sleep(3)

        # --------------------------------------------------------
        # STEP 8
        # Try Delete Again
        # --------------------------------------------------------

        print(
            "\nSTEP 8: Try To Delete Already Deleted Product Again"
        )

        result = (
            product_page.try_delete_product_again()
        )

        # --------------------------------------------------------
        # STEP 9
        # Verify Prevention
        # --------------------------------------------------------

        print(
            "\nSTEP 9: Verify Repeated Deletion Is Prevented"
        )

        assert result is False, (
            "Repeated deletion was not prevented."
        )

        print(
            "\nTEST 2 PASSED"
        )

        print(
            "Repeated deletion of the already "
            "deleted product was prevented."
        )

    finally:

        print(
            "\nClosing browser..."
        )

        driver.quit()


# ============================================================
# TEST 3
# Verify product name containing only spaces
# is rejected
# ============================================================

def test_verify_product_name_containing_only_spaces_is_rejected():

    driver = get_driver()

    try:

        print(
            "\n============================================================"
        )

        print(
            "TEST 3: Verify Product Name Containing "
            "Only Spaces Is Rejected"
        )

        print(
            "============================================================"
        )

        wait = WebDriverWait(
            driver,
            20
        )

        # --------------------------------------------------------
        # STEP 1
        # Open Login Page
        # --------------------------------------------------------

        print(
            "\nSTEP 1: Open Login Page"
        )

        driver.get(
            LOGIN_URL
        )

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "email")
            )
        )

        # --------------------------------------------------------
        # STEP 2
        # Login
        # --------------------------------------------------------

        print(
            "\nSTEP 2: Login"
        )

        login_page = LoginPage(
            driver
        )

        login_page.login(
            USERNAME,
            PASSWORD
        )

        time.sleep(3)

        # --------------------------------------------------------
        # STEP 3
        # Create Product Page
        # --------------------------------------------------------

        product_page = ProductSelectionPage(
            driver
        )

        # --------------------------------------------------------
        # STEP 4
        # Home
        # --------------------------------------------------------

        print(
            "\nSTEP 4: Navigate to Home"
        )

        product_page.click_home()

        # --------------------------------------------------------
        # STEP 5
        # Product Selection
        # --------------------------------------------------------

        print(
            "\nSTEP 5: Open Product Selection"
        )

        product_page.click_product_selection()

        # --------------------------------------------------------
        # STEP 6
        # Product Name
        # --------------------------------------------------------

        print(
            "\nSTEP 6: Enter Spaces Only"
        )

        product_name_field = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[@id='productName']"
                )
            )
        )

        product_name_field.clear()

        product_name_field.send_keys(
            "     "
        )

        # --------------------------------------------------------
        # STEP 7
        # Website
        # --------------------------------------------------------

        print(
            "\nSTEP 7: Enter Valid Website"
        )

        website_field = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[@id='productWebsite']"
                )
            )
        )

        website_field.clear()

        website_field.send_keys(
            "https://spacesvalidationtest.com"
        )

        # --------------------------------------------------------
        # STEP 8
        # Upload Photo
        # --------------------------------------------------------

        print(
            "\nSTEP 8: Upload Photo"
        )

        product_photo = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[@id='productPhoto']"
                )
            )
        )

        product_photo.send_keys(
            IMAGE_PATH
        )

        # --------------------------------------------------------
        # STEP 9
        # Click Add
        # --------------------------------------------------------

        print(
            "\nSTEP 9: Click Add Product"
        )

        add_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[@id='root']/div/div/div[2]/div/form/div[3]/button"
                )
            )
        )

        driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            add_button
        )

        time.sleep(0.5)

        try:

            add_button.click()

        except Exception:

            driver.execute_script(
                "arguments[0].click();",
                add_button
            )

        time.sleep(3)

        # --------------------------------------------------------
        # STEP 10
        # Get Validation Messages
        # --------------------------------------------------------

        print(
            "\nSTEP 10: Check Validation"
        )

        validation_messages = (
            product_page.get_validation_messages()
        )

        if validation_messages:

            print(
                "\nValidation message(s):"
            )

            for message in validation_messages:

                print(
                    f" - {message}"
                )

        else:

            print(
                "No browser validation message found."
            )

        # --------------------------------------------------------
        # STEP 11
        # Verify Form Still Exists
        # --------------------------------------------------------

        print(
            "\nSTEP 11: Verify Invalid Product Was Not Added"
        )

        form_displayed = (
            product_page.is_add_product_form_displayed()
        )

        assert form_displayed, (
            "Add Product form disappeared after "
            "submitting spaces-only product name. "
            "The application may have accepted the invalid value."
        )

        print(
            "Add Product form is still displayed."
        )

        print(
            "\nTEST 3 PASSED"
        )

        print(
            "Spaces-only product name was rejected."
        )

    finally:

        print(
            "\nClosing browser..."
        )

        driver.quit()


# ============================================================
# TEST 4
# Verify Rows Per Page Functionality
#
# Values:
# 10
# 25
# 50
# 100
# ============================================================

def test_verify_rows_per_page_functionality():

    driver = get_driver()

    try:

        print(
            "\n============================================================"
        )

        print(
            "TEST 4: Verify Rows Per Page Functionality"
        )

        print(
            "============================================================"
        )

        wait = WebDriverWait(
            driver,
            20
        )

        # --------------------------------------------------------
        # STEP 1
        # Open Login Page
        # --------------------------------------------------------

        print(
            "\nSTEP 1: Open Login Page"
        )

        driver.get(
            LOGIN_URL
        )

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "email")
            )
        )

        print(
            "Login page opened successfully."
        )

        # --------------------------------------------------------
        # STEP 2
        # Login
        # --------------------------------------------------------

        print(
            "\nSTEP 2: Login as Admin"
        )

        login_page = LoginPage(
            driver
        )

        login_page.login(
            USERNAME,
            PASSWORD
        )

        time.sleep(3)

        print(
            "Admin login successful."
        )

        # --------------------------------------------------------
        # STEP 3
        # Create Product Selection Page
        # --------------------------------------------------------

        print(
            "\nSTEP 3: Create Product Selection Page"
        )

        product_page = ProductSelectionPage(
            driver
        )

        # --------------------------------------------------------
        # STEP 4
        # Navigate to Home
        # --------------------------------------------------------

        print(
            "\nSTEP 4: Navigate to Home"
        )

        product_page.click_home()

        print(
            "Home opened successfully."
        )

        # --------------------------------------------------------
        # STEP 5
        # Open Product Selection
        # --------------------------------------------------------

        print(
            "\nSTEP 5: Open Product Selection"
        )

        product_page.click_product_selection()

        print(
            "Product Selection opened successfully."
        )

        # --------------------------------------------------------
        # STEP 6
        # Zoom Out
        # --------------------------------------------------------

        print(
            "\nSTEP 6: Zoom Out Page To 75%"
        )

        product_page.zoom_out_page(
            75
        )

        # --------------------------------------------------------
        # STEP 7
        # Verify Dropdown
        # --------------------------------------------------------

        print(
            "\nSTEP 7: Verify Rows Per Page Dropdown"
        )

        dropdown = wait.until(
            EC.visibility_of_element_located(
                product_page.rows_per_page_dropdown
            )
        )

        assert dropdown.is_displayed(), (
            "Rows Per Page dropdown is not displayed."
        )

        print(
            "Rows Per Page dropdown displayed successfully."
        )

        # --------------------------------------------------------
        # STEP 8
        # Create Select Object
        #
        # IMPORTANT FIX:
        # Select is imported at the top:
        #
        # from selenium.webdriver.support.ui import (
        #     WebDriverWait,
        #     Select
        # )
        # --------------------------------------------------------

        print(
            "\nSTEP 8: Create Selenium Select Object"
        )

        select = Select(
            dropdown
        )

        print(
            "Select object created successfully."
        )

        # --------------------------------------------------------
        # STEP 9
        # Get Available Options
        # --------------------------------------------------------

        print(
            "\nSTEP 9: Get Available Rows Per Page Options"
        )

        available_options = [
            option.text.strip()
            for option in select.options
        ]

        print(
            f"Available options: "
            f"{available_options}"
        )

        # --------------------------------------------------------
        # STEP 10
        # Verify Expected Options
        # --------------------------------------------------------

        print(
            "\nSTEP 10: Verify Options"
        )

        expected_options = [
            "10",
            "25",
            "50",
            "100"
        ]

        for expected_option in expected_options:

            assert expected_option in available_options, (
                f"Expected Rows Per Page option "
                f"'{expected_option}' was not found. "
                f"Available options: "
                f"{available_options}"
            )

            print(
                f"PASS: {expected_option} option is available."
            )

        # --------------------------------------------------------
        # STEP 11
        # Select 10
        # --------------------------------------------------------

        print(
            "\nSTEP 11: Select 10 Rows Per Page"
        )

        product_page.select_rows_per_page(
            10
        )

        dropdown = wait.until(
            EC.presence_of_element_located(
                product_page.rows_per_page_dropdown
            )
        )

        select = Select(
            dropdown
        )

        selected_value = (
            select.first_selected_option.text.strip()
        )

        assert selected_value == "10", (
            f"Expected selected value 10, "
            f"but got {selected_value}"
        )

        displayed_rows = (
            product_page.get_displayed_product_rows()
        )

        print(
            f"Displayed product rows: "
            f"{displayed_rows}"
        )

        assert displayed_rows <= 10, (
            f"More than 10 product rows are displayed: "
            f"{displayed_rows}"
        )

        print(
            "PASS: 10 rows per page."
        )

        # --------------------------------------------------------
        # STEP 12
        # Select 25
        # --------------------------------------------------------

        print(
            "\nSTEP 12: Select 25 Rows Per Page"
        )

        product_page.select_rows_per_page(
            25
        )

        dropdown = wait.until(
            EC.presence_of_element_located(
                product_page.rows_per_page_dropdown
            )
        )

        select = Select(
            dropdown
        )

        selected_value = (
            select.first_selected_option.text.strip()
        )

        assert selected_value == "25", (
            f"Expected selected value 25, "
            f"but got {selected_value}"
        )

        displayed_rows = (
            product_page.get_displayed_product_rows()
        )

        print(
            f"Displayed product rows: "
            f"{displayed_rows}"
        )

        assert displayed_rows <= 25, (
            f"More than 25 product rows are displayed: "
            f"{displayed_rows}"
        )

        print(
            "PASS: 25 rows per page."
        )

        # --------------------------------------------------------
        # STEP 13
        # Select 50
        # --------------------------------------------------------

        print(
            "\nSTEP 13: Select 50 Rows Per Page"
        )

        product_page.select_rows_per_page(
            50
        )

        dropdown = wait.until(
            EC.presence_of_element_located(
                product_page.rows_per_page_dropdown
            )
        )

        select = Select(
            dropdown
        )

        selected_value = (
            select.first_selected_option.text.strip()
        )

        assert selected_value == "50", (
            f"Expected selected value 50, "
            f"but got {selected_value}"
        )

        displayed_rows = (
            product_page.get_displayed_product_rows()
        )

        print(
            f"Displayed product rows: "
            f"{displayed_rows}"
        )

        assert displayed_rows <= 50, (
            f"More than 50 product rows are displayed: "
            f"{displayed_rows}"
        )

        print(
            "PASS: 50 rows per page."
        )

        # --------------------------------------------------------
        # STEP 14
        # Select 100
        # --------------------------------------------------------

        print(
            "\nSTEP 14: Select 100 Rows Per Page"
        )

        product_page.select_rows_per_page(
            100
        )

        dropdown = wait.until(
            EC.presence_of_element_located(
                product_page.rows_per_page_dropdown
            )
        )

        select = Select(
            dropdown
        )

        selected_value = (
            select.first_selected_option.text.strip()
        )

        assert selected_value == "100", (
            f"Expected selected value 100, "
            f"but got {selected_value}"
        )

        displayed_rows = (
            product_page.get_displayed_product_rows()
        )

        print(
            f"Displayed product rows: "
            f"{displayed_rows}"
        )

        assert displayed_rows <= 100, (
            f"More than 100 product rows are displayed: "
            f"{displayed_rows}"
        )

        print(
            "PASS: 100 rows per page."
        )

        # --------------------------------------------------------
        # FINAL RESULT
        # --------------------------------------------------------

        print(
            "\n============================================================"
        )

        print(
            "TEST 4 PASSED"
        )

        print(
            "Rows Per Page functionality successfully "
            "verified for:"
        )

        print(
            "10, 25, 50 and 100"
        )

        print(
            "============================================================"
        )

    finally:

        print(
            "\nClosing browser..."
        )

        driver.quit()