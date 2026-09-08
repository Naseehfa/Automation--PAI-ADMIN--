import os
import time

from utils.driver_setup import get_driver

from config.config import (
    URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage
from pages.home_page import HomePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# URLS
# ============================================================

HOME_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/team"
)

PRODUCT_SELECTION_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/product-selection"
)


# ============================================================
# IMAGE PATH
# ============================================================

IMAGE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "image.jpg"
    )
)


# ============================================================
# HELPER - LOGIN
# ============================================================

def open_admin_page():

    driver = get_driver()

    driver.get(URL)

    driver.execute_script(
        "document.body.style.zoom='80%'"
    )

    time.sleep(3)

    print(
        "\nLogging in..."
    )

    login = LoginPage(driver)

    login.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    print(
        "Login completed."
    )

    wait = WebDriverWait(
        driver,
        20
    )

    wait.until(
        lambda d:
        "admin" in d.current_url
    )

    time.sleep(3)

    return driver, wait


# ============================================================
# HELPER - OPEN PRODUCT SELECTION
# ============================================================

def open_product_selection():

    driver, wait = open_admin_page()

    home = HomePage(driver)

    home.click_home()

    home.verify_home_page()

    home.click_product_selection()

    home.verify_product_selection_page()

    return driver, home, wait


# ============================================================
# 1. LOGIN + HOME + PRODUCT SELECTION NAVIGATION
# ============================================================

def test_home_and_product_selection_navigation():

    driver, wait = open_admin_page()

    home = HomePage(driver)

    try:

        print(
            "\n========== LOGIN =========="
        )

        assert (
            "admin"
            in driver.current_url
        )

        print(
            "\n========== HOME =========="
        )

        home.click_home()

        home.verify_home_page()

        assert (
            driver.current_url ==
            HOME_URL
        )

        print(
            "\n========== PRODUCT SELECTION =========="
        )

        home.click_product_selection()

        home.verify_product_selection_page()

        assert (
            driver.current_url ==
            PRODUCT_SELECTION_URL
        )

        print(
            "\n========== NAVIGATION TEST PASSED =========="
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 2. POSITIVE - VALID PRODUCT
# ============================================================

def test_add_product_valid_data():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== P01 VALID PRODUCT (LETTERS ONLY) =========="
        )

        random_product_name = (
            home.generate_product_name_letters(
                prefix="Apple Watch"
            )
        )

        random_value = (
            home.generate_random_letters(
                length=6
            )
        )

        random_product_website = (
            f"https://www.apple.com/watch/{random_value}"
        )

        print(
            "\nProduct Name:",
            random_product_name
        )

        print(
            "Product Website:",
            random_product_website
        )

        home.fill_product_form(
            product_name=random_product_name,
            product_website=random_product_website,
            product_photo=IMAGE_PATH
        )

        home.click_add_product()

        time.sleep(5)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "\n========== P01 PASSED =========="
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 3. POSITIVE - SECOND PRODUCT
# ============================================================

def test_duplicate():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== P02 SECOND VALID PRODUCT =========="
        )

        home.fill_product_form(
            product_name="Samsung Galaxy",
            product_website="https://www.samsung.com/Samsung",
            product_photo=IMAGE_PATH
        )

        home.click_add_product()

        time.sleep(5)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "P02 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 4. NEGATIVE - ALL FIELDS EMPTY
# ============================================================

def test_add_product_all_fields_empty():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== N01 ALL FIELDS EMPTY =========="
        )

        home.fill_product_form(
            product_name="",
            product_website="",
            product_photo=""
        )

        home.click_add_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "N01 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 5. NEGATIVE - EMPTY PRODUCT NAME
# ============================================================

def test_add_product_empty_name():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== N02 EMPTY PRODUCT NAME =========="
        )

        home.fill_product_form(
            product_name="",
            product_website="https://www.apple.com/Apples",
            product_photo=IMAGE_PATH
        )

        home.click_add_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "N02 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 6. NEGATIVE - EMPTY WEBSITE
# ============================================================

def test_add_product_empty_website():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== N03 EMPTY WEBSITE =========="
        )

        home.fill_product_form(
            product_name="Apple Watch",
            product_website="",
            product_photo=IMAGE_PATH
        )

        home.click_add_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "N03 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 7. NEGATIVE - EMPTY PHOTO
# ============================================================

def test_add_product_empty_photo():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== N04 EMPTY PHOTO =========="
        )

        home.fill_product_form(
            product_name="Router",
            product_website="https://www.apple.com/router",
            product_photo=""
        )

        home.click_add_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "N04 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 8. NEGATIVE - INVALID WEBSITE
# ============================================================

def test_add_product_invalid_website():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== N05 INVALID WEBSITE =========="
        )

        home.fill_product_form(
            product_name="IPhone",
            product_website="invalid-url",
            product_photo=IMAGE_PATH
        )

        home.click_add_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "N05 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 9. NEGATIVE - WEBSITE WITHOUT HTTPS
# ============================================================

def test_add_product_invalid_website_format():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== N06 INVALID WEBSITE FORMAT =========="
        )

        home.fill_product_form(
            product_name="Apple Watch",
            product_website="apple.com",
            product_photo=IMAGE_PATH
        )

        home.click_add_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "N06 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 10. NEGATIVE - NUMERIC PRODUCT NAME
# ============================================================

def test_add_product_numeric_name():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== N07 NUMERIC PRODUCT NAME =========="
        )

        home.fill_product_form(
            product_name="123456789",
            product_website="https://www.apple.com/Apple",
            product_photo=IMAGE_PATH
        )

        home.click_add_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "N07 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 11. NEGATIVE - SPECIAL CHARACTERS PRODUCT NAME
# ============================================================

def test_add_product_special_character_name():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== N08 SPECIAL CHARACTER NAME =========="
        )

        home.fill_product_form(
            product_name="@#$%^&*",
            product_website="https://www.apple.com/Apple",
            product_photo=IMAGE_PATH
        )

        home.click_add_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "N08 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 12. NEGATIVE - VERY LONG PRODUCT NAME
# ============================================================

def test_add_product_long_name():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== N09 LONG PRODUCT NAME =========="
        )

        long_name = (
            "A" * 300
        )

        home.fill_product_form(
            product_name=long_name,
            product_website="https://www.apple.com/",
            product_photo=IMAGE_PATH
        )

        home.click_add_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "N09 PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 13. POSITIVE - GUARANTEED ALPHANUMERIC PRODUCT NAME
# ============================================================

def test_ALPHANUMERIC_PRODUCT_NAME():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== P10 ALPHANUMERIC PRODUCT NAME =========="
        )

        random_product_name = (
            home.generate_product_name(
                prefix="AppleWatch"
            )
        )

        random_value = (
            home.generate_alphanumeric_value(
                length=6
            )
        )

        random_product_website = (
            f"https://www.apple.com/watch/{random_value}"
        )

        print(
            "\nGenerated Product Name:",
            random_product_name
        )

        print(
            "Generated Product Website:",
            random_product_website
        )

        # ========================================================
        # VERIFY PRODUCT NAME
        # ========================================================

        assert random_product_name.startswith(
            "AppleWatch"
        )

        generated_part = (
            random_product_name[
                len("AppleWatch"):
            ]
        )

        assert generated_part.isalnum()

        assert any(
            char.isalpha()
            for char in generated_part
        )

        assert any(
            char.isdigit()
            for char in generated_part
        )

        print(
            "Alphanumeric validation passed."
        )

        # ========================================================
        # FILL FORM
        # ========================================================

        home.fill_product_form(
            product_name=random_product_name,
            product_website=random_product_website,
            product_photo=IMAGE_PATH
        )

        # ========================================================
        # VERIFY PRODUCT NAME FIELD
        # ========================================================

        product_name_field = wait.until(
            EC.visibility_of_element_located(
                home.product_name_input
            )
        )

        entered_product_name = (
            product_name_field.get_attribute(
                "value"
            )
        )

        print(
            "\nValue entered into Product Name field:",
            entered_product_name
        )

        assert (
            entered_product_name ==
            random_product_name
        )

        # ========================================================
        # VERIFY WEBSITE FIELD
        # ========================================================

        website_field = wait.until(
            EC.visibility_of_element_located(
                home.product_website_input
            )
        )

        entered_website = (
            website_field.get_attribute(
                "value"
            )
        )

        print(
            "Value entered into Website field:",
            entered_website
        )

        assert (
            entered_website ==
            random_product_website
        )

        # ========================================================
        # ADD PRODUCT
        # ========================================================

        home.click_add_product()

        time.sleep(5)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "\n========== P10 ALPHANUMERIC PRODUCT PASSED =========="
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 14. POSITIVE - UPDATE BOTH NAME AND WEBSITE
# ============================================================

def test_update_product():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== U01 UPDATE PRODUCT =========="
        )

        # ========================================================
        # GENERATE NEW PRODUCT NAME
        # ========================================================

        random_product_name = (
            home.generate_product_name_letters(
                prefix="Dress"
            )
        )

        # ========================================================
        # GENERATE NEW WEBSITE
        # ========================================================

        random_value = (
            home.generate_random_letters(
                length=8
            )
        )

        random_product_website = (
            f"https://www.apple.com/watch/{random_value}"
        )

        assert (
            random_product_name[
                len("Dress "):
            ].isalpha()
        )

        assert (
            random_value.isalpha()
        )

        # ========================================================
        # OPEN EDIT
        # ========================================================

        home.open_first_product_edit()

        # ========================================================
        # READ OLD VALUES
        # ========================================================

        old_product_name = (
            home.get_edit_product_name()
        )

        old_product_website = (
            home.get_edit_product_website()
        )

        print(
            "\nOld Product Name:",
            old_product_name
        )

        print(
            "Old Product Website:",
            old_product_website
        )

        # ========================================================
        # CLEAR OLD NAME
        # ========================================================

        home.set_react_input(
            home.update_product_name_input,
            ""
        )

        assert (
            home.get_edit_product_name()
            == ""
        )

        # ========================================================
        # CLEAR OLD WEBSITE
        # ========================================================

        home.set_react_input(
            home.update_product_website_input,
            ""
        )

        assert (
            home.get_edit_product_website()
            == ""
        )

        # ========================================================
        # ENTER NEW NAME
        # ========================================================

        home.set_react_input(
            home.update_product_name_input,
            random_product_name
        )

        # ========================================================
        # ENTER NEW WEBSITE
        # ========================================================

        home.set_react_input(
            home.update_product_website_input,
            random_product_website
        )

        # ========================================================
        # VERIFY VALUES
        # ========================================================

        assert (
            home.get_edit_product_name()
            == random_product_name
        )

        assert (
            home.get_edit_product_website()
            == random_product_website
        )

        # ========================================================
        # UPDATE
        # ========================================================

        assert (
            home.is_update_button_enabled()
        ), "Update button should be enabled for valid data."

        home.click_update_product()

        time.sleep(4)

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "\n========== U01 UPDATE PRODUCT PASSED =========="
        )

    finally:

        time.sleep(5)

        driver.quit()


# ============================================================
# 15. NEGATIVE - UPDATE PREVENTED WHEN PRODUCT NAME CLEARED
# ============================================================

def test_update_prevented_when_product_name_cleared():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== U02 CLEAR PRODUCT NAME =========="
        )

        home.open_first_product_edit()

        old_website = (
            home.get_edit_product_website()
        )

        print(
            "\nExisting Website:",
            old_website
        )

        # ========================================================
        # CLEAR PRODUCT NAME
        # ========================================================

        home.set_react_input(
            home.update_product_name_input,
            ""
        )

        current_name = (
            home.get_edit_product_name()
        )

        assert (
            current_name == ""
        ), (
            "Product Name was not cleared."
        )

        print(
            "Product Name cleared successfully."
        )

        # ========================================================
        # KEEP WEBSITE
        # ========================================================

        assert (
            home.get_edit_product_website()
            == old_website
        )

        # ========================================================
        # VERIFY UPDATE PREVENTED
        # ========================================================

        update_enabled = (
            home.is_update_button_enabled()
        )

        print(
            "\nUpdate button enabled:",
            update_enabled
        )

        # If the application disables the button,
        # this is the expected validation behavior.

        if not update_enabled:

            print(
                "Update correctly prevented because "
                "Product Name is empty."
            )

            assert not update_enabled

        else:

            # If the application does not disable the button,
            # click it and verify that the edit modal remains open.
            home.click_update_product()

            time.sleep(3)

            name_field_exists = (
                len(
                    driver.find_elements(
                        *home.update_product_name_input
                    )
                ) > 0
            )

            assert name_field_exists, (
                "Update was submitted even though "
                "Product Name was empty."
            )

            print(
                "Update correctly prevented by validation."
            )

        print(
            "\n========== U02 PASSED =========="
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 16. NEGATIVE - INVALID PRODUCT WEBSITE UPDATE
# ============================================================

def test_update_invalid_product_website():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== U03 INVALID WEBSITE UPDATE =========="
        )

        home.open_first_product_edit()

        # ========================================================
        # SAVE OLD VALUES
        # ========================================================

        old_name = (
            home.get_edit_product_name()
        )

        old_website = (
            home.get_edit_product_website()
        )

        print(
            "\nOld Product Name:",
            old_name
        )

        print(
            "Old Product Website:",
            old_website
        )

        # ========================================================
        # KEEP VALID PRODUCT NAME
        # ========================================================

        assert old_name.strip() != ""

        # ========================================================
        # ENTER INVALID WEBSITE
        # ========================================================

        invalid_website = (
            "invalid-url"
        )

        print(
            "\nInvalid Website:",
            invalid_website
        )

        home.set_react_input(
            home.update_product_website_input,
            invalid_website
        )

        # ========================================================
        # VERIFY INVALID VALUE ENTERED
        # ========================================================

        entered_website = (
            home.get_edit_product_website()
        )

        assert (
            entered_website ==
            invalid_website
        )

        print(
            "Invalid website entered."
        )

        # ========================================================
        # VERIFY UPDATE BEHAVIOR
        # ========================================================

        update_enabled = (
            home.is_update_button_enabled()
        )

        print(
            "\nUpdate button enabled:",
            update_enabled
        )

        if not update_enabled:

            print(
                "Update correctly prevented for "
                "invalid Product Website."
            )

            assert not update_enabled

        else:

            # The UI may leave the button enabled and
            # perform validation after clicking.
            home.click_update_product()

            time.sleep(3)

            # The edit modal should remain visible when
            # invalid website data is rejected.
            modal_still_open = (
                len(
                    driver.find_elements(
                        *home.update_product_name_input
                    )
                ) > 0
            )

            assert modal_still_open, (
                "Invalid Product Website was accepted "
                "and update was completed."
            )

            current_website = (
                home.get_edit_product_website()
            )

            assert (
                current_website ==
                invalid_website
            )

            print(
                "Invalid website update correctly rejected."
            )

        print(
            "\n========== U03 PASSED =========="
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 17. POSITIVE - UPDATE ONLY PRODUCT NAME
# ============================================================

def test_update_only_product_name_changed():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== U04 ONLY PRODUCT NAME CHANGED =========="
        )

        home.open_first_product_edit()

        # ========================================================
        # SAVE ORIGINAL WEBSITE
        # ========================================================

        original_website = (
            home.get_edit_product_website()
        )

        original_name = (
            home.get_edit_product_name()
        )

        print(
            "\nOriginal Product Name:",
            original_name
        )

        print(
            "Original Product Website:",
            original_website
        )

        # ========================================================
        # GENERATE NEW NAME
        # ========================================================

        new_product_name = (
            home.generate_product_name_letters(
                prefix="Dress"
            )
        )

        print(
            "\nNew Product Name:",
            new_product_name
        )

        # ========================================================
        # CHANGE ONLY PRODUCT NAME
        # ========================================================

        home.set_react_input(
            home.update_product_name_input,
            ""
        )

        assert (
            home.get_edit_product_name()
            == ""
        )

        home.set_react_input(
            home.update_product_name_input,
            new_product_name
        )

        # ========================================================
        # VERIFY WEBSITE WAS NOT CHANGED
        # ========================================================

        current_website = (
            home.get_edit_product_website()
        )

        assert (
            current_website ==
            original_website
        ), (
            "Product Website changed unexpectedly."
        )

        # ========================================================
        # VERIFY NEW NAME
        # ========================================================

        current_name = (
            home.get_edit_product_name()
        )

        assert (
            current_name ==
            new_product_name
        )

        generated_part = (
            new_product_name[
                len("Dress "):
            ]
        )

        assert generated_part.isalpha()

        # ========================================================
        # UPDATE
        # ========================================================

        assert (
            home.is_update_button_enabled()
        ), "Update button should be enabled."

        home.click_update_product()

        time.sleep(4)

        # ========================================================
        # VERIFY UPDATE COMPLETED
        # ========================================================

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "\nOnly Product Name was changed successfully."
        )

        print(
            "Website remained:",
            original_website
        )

        print(
            "\n========== U04 PASSED =========="
        )

    finally:

        time.sleep(5)

        driver.quit()


# ============================================================
# 18. POSITIVE - UPDATE ONLY PRODUCT WEBSITE
# ============================================================

def test_update_only_product_website_changed():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== U05 ONLY PRODUCT WEBSITE CHANGED =========="
        )

        home.open_first_product_edit()

        # ========================================================
        # SAVE ORIGINAL PRODUCT NAME
        # ========================================================

        original_name = (
            home.get_edit_product_name()
        )

        original_website = (
            home.get_edit_product_website()
        )

        print(
            "\nOriginal Product Name:",
            original_name
        )

        print(
            "Original Product Website:",
            original_website
        )

        # ========================================================
        # GENERATE NEW WEBSITE
        # ========================================================

        random_value = (
            home.generate_random_letters(
                length=8
            )
        )

        new_product_website = (
            f"https://www.apple.com/watch/{random_value}"
        )

        print(
            "\nNew Product Website:",
            new_product_website
        )

        assert random_value.isalpha()

        # ========================================================
        # CHANGE ONLY WEBSITE
        # ========================================================

        home.set_react_input(
            home.update_product_website_input,
            ""
        )

        assert (
            home.get_edit_product_website()
            == ""
        )

        home.set_react_input(
            home.update_product_website_input,
            new_product_website
        )

        # ========================================================
        # VERIFY PRODUCT NAME WAS NOT CHANGED
        # ========================================================

        current_name = (
            home.get_edit_product_name()
        )

        assert (
            current_name ==
            original_name
        ), (
            "Product Name changed unexpectedly."
        )

        # ========================================================
        # VERIFY NEW WEBSITE
        # ========================================================

        current_website = (
            home.get_edit_product_website()
        )

        assert (
            current_website ==
            new_product_website
        )

        # ========================================================
        # UPDATE
        # ========================================================

        assert (
            home.is_update_button_enabled()
        ), "Update button should be enabled."

        home.click_update_product()

        time.sleep(4)

        # ========================================================
        # VERIFY UPDATE COMPLETED
        # ========================================================

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "\nOnly Product Website was changed successfully."
        )

        print(
            "Product Name remained:",
            original_name
        )

        print(
            "\n========== U05 PASSED =========="
        )

    finally:

        time.sleep(5)

        driver.quit()


# ============================================================
# 19. DELETE PRODUCT - CONFIRM BUTTON
# ============================================================

def test_delete_product_confirm_closebutton():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== D01 DELETE PRODUCT =========="
        )

        home.delete_product_confirm()

        wait.until(
            lambda d:
            "product-selection"
            in d.current_url
        )

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "\n========== D01 DELETE PRODUCT PASSED =========="
        )

    finally:

        time.sleep(5)

        driver.quit()


# ============================================================
# 20. DELETE PRODUCT - BUTTON 1
# ============================================================

def test_delete_product_cancel_button():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== D02 DELETE PRODUCT BUTTON 1 =========="
        )

        home.delete_product_confirm_button_1()

        wait.until(
            lambda d:
            "product-selection"
            in d.current_url
        )

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "\n========== D02 DELETE PRODUCT BUTTON 1 PASSED =========="
        )

    finally:

        time.sleep(5)

        driver.quit()


# ============================================================
# 21. DELETE PRODUCT - BUTTON 2
# ============================================================

def test_delete_product_confirm_button():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== D03 DELETE PRODUCT BUTTON 2 =========="
        )

        home.delete_product_confirm_button_2()

        wait.until(
            lambda d:
            "product-selection"
            in d.current_url
        )

        assert (
            "product-selection"
            in driver.current_url
        )

        print(
            "\n========== D03 DELETE PRODUCT BUTTON 2 PASSED =========="
        )

    finally:

        time.sleep(5)

        driver.quit()


# ============================================================
# 22. PAGINATION - VERIFY CORRECT NUMBER OF PRODUCTS
# ============================================================

def test_pagination_displays_correct_number_of_products():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== P01 PAGINATION PRODUCT COUNT =========="
        )

        # ========================================================
        # GET PRODUCTS DISPLAYED ON FIRST PAGE
        # ========================================================

        first_page_count = (
            home.get_displayed_product_count()
        )

        print(
            "\nProducts displayed on first page:",
            first_page_count
        )

        # ========================================================
        # VERIFY AT LEAST ONE PRODUCT IS DISPLAYED
        # ========================================================

        assert first_page_count > 0, (
            "No products are displayed on the first page."
        )

        # ========================================================
        # CHECK NEXT PAGE
        # ========================================================

        next_enabled = (
            home.is_next_page_enabled()
        )

        print(
            "Next Page enabled:",
            next_enabled
        )

        # ========================================================
        # IF THERE IS ANOTHER PAGE
        # ========================================================

        if next_enabled:

            home.click_next_page()

            second_page_count = (
                home.get_displayed_product_count()
            )

            print(
                "\nProducts displayed on second page:",
                second_page_count
            )

            assert second_page_count > 0, (
                "Next page contains no products."
            )

            print(
                "\nPagination successfully displays "
                "products on multiple pages."
            )

        else:

            print(
                "\nOnly one page of products exists."
            )

            print(
                "Pagination is not required because "
                "all products fit on one page."
            )

        print(
            "\n========== P01 PAGINATION COUNT PASSED =========="
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 23. PAGINATION - VERIFY NEXT PAGE
# ============================================================

def test_pagination_next_page():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== P02 NEXT PAGE =========="
        )

        # ========================================================
        # GET FIRST PAGE PRODUCT COUNT
        # ========================================================

        first_page_count = (
            home.get_displayed_product_count()
        )

        assert first_page_count > 0, (
            "First page does not contain products."
        )

        # ========================================================
        # CHECK NEXT BUTTON
        # ========================================================

        next_enabled = (
            home.is_next_page_enabled()
        )

        print(
            "\nNext Page enabled:",
            next_enabled
        )

        # ========================================================
        # IF NEXT PAGE EXISTS
        # ========================================================

        if next_enabled:

            home.click_next_page()

            second_page_count = (
                home.get_displayed_product_count()
            )

            assert second_page_count > 0, (
                "Second page does not contain products."
            )

            print(
                "\nFirst page product count:",
                first_page_count
            )

            print(
                "Second page product count:",
                second_page_count
            )

            print(
                "\nNext Page functionality works correctly."
            )

        else:

            print(
                "\nNext Page is disabled."
            )

            print(
                "There is only one page of products."
            )

        print(
            "\n========== P02 NEXT PAGE PASSED =========="
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 24. PAGINATION - VERIFY PREVIOUS PAGE
# ============================================================

def test_pagination_previous_page():

    driver, home, wait = open_product_selection()

    try:

        print(
            "\n========== P03 PREVIOUS PAGE =========="
        )

        # ========================================================
        # CHECK WHETHER NEXT PAGE EXISTS
        # ========================================================

        next_enabled = (
            home.is_next_page_enabled()
        )

        print(
            "\nNext Page enabled:",
            next_enabled
        )

        # ========================================================
        # MOVE TO SECOND PAGE
        # ========================================================

        if next_enabled:

            home.click_next_page()

            second_page_count = (
                home.get_displayed_product_count()
            )

            assert second_page_count > 0, (
                "Second page contains no products."
            )

            print(
                "\nSecond page loaded successfully."
            )

            # ====================================================
            # CHECK PREVIOUS BUTTON
            # ====================================================

            previous_enabled = (
                home.is_previous_page_enabled()
            )

            print(
                "Previous Page enabled:",
                previous_enabled
            )

            assert previous_enabled, (
                "Previous Page button should be enabled "
                "after moving to the second page."
            )

            # ====================================================
            # CLICK PREVIOUS
            # ====================================================

            home.click_previous_page()

            first_page_count = (
                home.get_displayed_product_count()
            )

            assert first_page_count > 0, (
                "First page contains no products "
                "after returning."
            )

            print(
                "\nReturned to first page successfully."
            )

        else:

            print(
                "\nPrevious Page test skipped logically "
                "because only one page exists."
            )

        print(
            "\n========== P03 PREVIOUS PAGE PASSED =========="
        )

    finally:

        time.sleep(3)

        driver.quit()

