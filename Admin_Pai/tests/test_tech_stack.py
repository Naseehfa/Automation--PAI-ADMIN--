import os
import random
import string
import time

from utils.driver_setup import get_driver

from config.config import (
    URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage
from pages.tech_stack_page import TechStackPage

from selenium.webdriver.support.ui import WebDriverWait


# ============================================================
# URL
# ============================================================

TECH_STACK_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/tech-stack"
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
# VALID CATEGORY
# ============================================================

VALID_CATEGORY = "Frontend"


# ============================================================
# EXISTING TECHNOLOGY FOR EDIT
# ============================================================

EXISTING_TECHNOLOGY = "Seleniumuto"


# ============================================================
# RANDOM TEXT
# ============================================================

def generate_random_text(length=8):

    letters = string.ascii_letters

    return "".join(
        random.choice(letters)
        for _ in range(length)
    )


# ============================================================
# GENERATE TECHNOLOGY
# ============================================================

def generate_technology():

    random_text = generate_random_text()

    return (
        f"Selenium Automation {random_text}"
    )


# ============================================================
# LOGIN
# ============================================================

def open_admin_page():

    driver = get_driver()

    driver.get(URL)

    driver.execute_script(
        "document.body.style.zoom='80%'"
    )

    time.sleep(2)

    print(
        "\n========== LOGIN =========="
    )

    login = LoginPage(
        driver
    )

    login.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    wait = WebDriverWait(
        driver,
        20
    )

    wait.until(
        lambda d:
        "login" not in d.current_url.lower()
    )

    time.sleep(2)

    print(
        "Login completed"
    )

    print(
        "Current URL:",
        driver.current_url
    )

    return (
        driver,
        wait
    )


# ============================================================
# OPEN TECH STACK
# ============================================================

def open_tech_stack():

    driver, wait = (
        open_admin_page()
    )

    tech_stack = TechStackPage(
        driver
    )

    tech_stack.navigate_to_tech_stack()

    wait.until(
        lambda d:
        "/admin/tech-stack"
        in d.current_url
    )

    assert (
        "/admin/tech-stack"
        in driver.current_url
    )

    time.sleep(2)

    return (
        driver,
        tech_stack,
        wait
    )


# ============================================================
# 01 - NAVIGATION
# ============================================================

def test_tech_stack_navigation():

    driver, wait = (
        open_admin_page()
    )

    try:

        print(
            "\n========== "
            "TECH STACK NAVIGATION "
            "=========="
        )

        tech_stack = TechStackPage(
            driver
        )

        tech_stack.navigate_to_tech_stack()

        wait.until(
            lambda d:
            "/admin/tech-stack"
            in d.current_url
        )

        assert (
            driver.current_url
            == TECH_STACK_URL
        )

        print(
            "TECH STACK NAVIGATION PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 02 - PRINT AVAILABLE CATEGORIES
# ============================================================

def test_print_available_categories():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "AVAILABLE CATEGORIES "
            "=========="
        )

        categories = (
            tech_stack.get_available_categories()
        )

        assert len(categories) > 0, (
            "No Tech Stack categories found"
        )

        print(
            "Categories:",
            categories
        )

        print(
            "CATEGORY LIST PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 03 - POSITIVE VALID TECH STACK
# ============================================================

def test_add_tech_stack_valid_data():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "P01 VALID TECH STACK "
            "=========="
        )

        technology = generate_technology()

        tech_stack.add_tech_stack(
            technology=technology,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH
        )

        assert (
            driver.current_url
            == TECH_STACK_URL
        )

        print(
            "Technology:",
            technology
        )

        print(
            "Category:",
            VALID_CATEGORY
        )

        print(
            "P01 VALID TECH STACK PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 04 - POSITIVE SELENIUM
# ============================================================

def test_add_selenium_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "P02 SELENIUM "
            "=========="
        )

        technology = (
            f"Selenium "
            f"{generate_random_text()}"
        )

        tech_stack.add_tech_stack(
            technology=technology,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH
        )

        assert (
            driver.current_url
            == TECH_STACK_URL
        )

        print(
            "P02 SELENIUM PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 05 - POSITIVE PYTHON
# ============================================================

def test_add_python_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "P03 PYTHON "
            "=========="
        )

        technology = (
            f"Python "
            f"{generate_random_text()}"
        )

        tech_stack.add_tech_stack(
            technology=technology,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH
        )

        assert (
            driver.current_url
            == TECH_STACK_URL
        )

        print(
            "P03 PYTHON PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 06 - POSITIVE MULTI WORD
# ============================================================

def test_add_multi_word_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "P04 MULTI WORD TECHNOLOGY "
            "=========="
        )

        technology = (
            "Test Automation Framework "
            f"{generate_random_text()}"
        )

        tech_stack.add_tech_stack(
            technology=technology,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH
        )

        assert (
            driver.current_url
            == TECH_STACK_URL
        )

        print(
            "P04 MULTI WORD PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 07 - POSITIVE MIXED CASE
# ============================================================

def test_add_mixed_case_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "P05 MIXED CASE "
            "=========="
        )

        technology = (
            f"SeLeNiUm "
            f"{generate_random_text()}"
        )

        tech_stack.add_tech_stack(
            technology=technology,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH
        )

        assert (
            driver.current_url
            == TECH_STACK_URL
        )

        print(
            "P05 MIXED CASE PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 08 - POSITIVE NUMBERS + TEXT
# ============================================================

def test_add_technology_with_numbers():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "P06 NUMBERS + TEXT "
            "=========="
        )

        technology = (
            f"HTML5 Automation "
            f"{generate_random_text()}"
        )

        tech_stack.add_tech_stack(
            technology=technology,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH
        )

        assert (
            driver.current_url
            == TECH_STACK_URL
        )

        print(
            "P06 NUMBERS + TEXT PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 09 - POSITIVE LONG TECHNOLOGY
# ============================================================

def test_add_long_valid_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "P07 LONG VALID TECHNOLOGY "
            "=========="
        )

        technology = (
            "Enterprise Software "
            "Testing Automation Framework "
            f"{generate_random_text()}"
        )

        tech_stack.add_tech_stack(
            technology=technology,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH
        )

        assert (
            driver.current_url
            == TECH_STACK_URL
        )

        print(
            "P07 LONG TECHNOLOGY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 10 - NEGATIVE ALL EMPTY
# ============================================================

def test_add_tech_stack_all_empty():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N01 ALL EMPTY "
            "=========="
        )

        tech_stack.enter_technology("")

        tech_stack.click_submit()

        time.sleep(2)

        assert tech_stack.is_form_displayed(), (
            "Form was not displayed after empty submission"
        )

        print(
            "N01 ALL EMPTY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 11 - NEGATIVE EMPTY TECHNOLOGY
# ============================================================

def test_add_empty_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N02 EMPTY TECHNOLOGY "
            "=========="
        )

        tech_stack.enter_technology("")

        tech_stack.select_category(
            VALID_CATEGORY
        )

        tech_stack.upload_image(
            IMAGE_PATH
        )

        tech_stack.click_submit()

        time.sleep(2)

        assert tech_stack.is_form_displayed(), (
            "Form was not displayed after empty technology"
        )

        print(
            "N02 EMPTY TECHNOLOGY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 12 - NEGATIVE EMPTY CATEGORY
# ============================================================

def test_add_empty_category():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N03 EMPTY CATEGORY "
            "=========="
        )

        technology = generate_technology()

        tech_stack.enter_technology(
            technology
        )

        tech_stack.upload_image(
            IMAGE_PATH
        )

        tech_stack.click_submit()

        time.sleep(2)

        assert tech_stack.is_form_displayed(), (
            "Form was not displayed after empty category"
        )

        print(
            "N03 EMPTY CATEGORY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 13 - NEGATIVE EMPTY IMAGE
# ============================================================

def test_add_empty_image():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N04 EMPTY IMAGE "
            "=========="
        )

        technology = generate_technology()

        tech_stack.enter_technology(
            technology
        )

        tech_stack.select_category(
            VALID_CATEGORY
        )

        tech_stack.click_submit()

        time.sleep(2)

        assert tech_stack.is_form_displayed(), (
            "Form was not displayed after empty image"
        )

        print(
            "N04 EMPTY IMAGE PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 14 - NEGATIVE SPACES ONLY
# ============================================================

def test_add_spaces_only_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N05 SPACES ONLY "
            "=========="
        )

        tech_stack.enter_technology(
            "     "
        )

        tech_stack.select_category(
            VALID_CATEGORY
        )

        tech_stack.upload_image(
            IMAGE_PATH
        )

        tech_stack.click_submit()

        time.sleep(2)

        assert tech_stack.is_form_displayed(), (
            "Form was not displayed after spaces-only input"
        )

        print(
            "N05 SPACES ONLY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 15 - NEGATIVE NUMERIC ONLY
# ============================================================

def test_add_numeric_only_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N06 NUMERIC ONLY "
            "=========="
        )

        tech_stack.enter_technology(
            "123456789"
        )

        tech_stack.select_category(
            VALID_CATEGORY
        )

        tech_stack.upload_image(
            IMAGE_PATH
        )

        tech_stack.click_submit()

        time.sleep(2)

        assert tech_stack.is_form_displayed(), (
            "Form was not displayed after numeric-only input"
        )

        print(
            "N06 NUMERIC ONLY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 16 - NEGATIVE SPECIAL CHARACTERS
# ============================================================

def test_add_special_character_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N07 SPECIAL CHARACTERS "
            "=========="
        )

        tech_stack.enter_technology(
            "@#$%^&*"
        )

        tech_stack.select_category(
            VALID_CATEGORY
        )

        tech_stack.upload_image(
            IMAGE_PATH
        )

        tech_stack.click_submit()

        time.sleep(2)

        assert tech_stack.is_form_displayed(), (
            "Form was not displayed after special characters"
        )

        print(
            "N07 SPECIAL CHARACTERS PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 17 - NEGATIVE VERY LONG TECHNOLOGY
# ============================================================

def test_add_very_long_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N09 VERY LONG TECHNOLOGY "
            "=========="
        )

        long_technology = (
            "A" * 30
        )

        tech_stack.enter_technology(
            long_technology
        )

        tech_stack.select_category(
            VALID_CATEGORY
        )

        tech_stack.upload_image(
            IMAGE_PATH
        )

        tech_stack.click_submit()

        time.sleep(2)

        assert tech_stack.is_form_displayed(), (
            "Form was not displayed after very long technology"
        )

        print(
            "N09 VERY LONG TECHNOLOGY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 18 - NEGATIVE INVALID CATEGORY
# ============================================================

def test_add_invalid_category():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N13 INVALID CATEGORY "
            "=========="
        )

        technology = generate_technology()

        tech_stack.enter_technology(
            technology
        )

        try:

            tech_stack.select_category(
                "Invalid Category XYZ"
            )

            assert False, (
                "Invalid category was accepted"
            )

        except ValueError:

            print(
                "Invalid category correctly rejected"
            )

        print(
            "N13 INVALID CATEGORY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 19 - NEGATIVE DUPLICATE TECHNOLOGY
# ============================================================

def test_add_duplicate_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N14 DUPLICATE TECHNOLOGY "
            "=========="
        )

        duplicate_name = (
            "Selenium Duplicate Test "
            f"{generate_random_text()}"
        )

        tech_stack.add_tech_stack(
            technology=duplicate_name,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH
        )

        time.sleep(2)

        tech_stack.enter_technology(
            duplicate_name
        )

        tech_stack.select_category(
            VALID_CATEGORY
        )

        tech_stack.upload_image(
            IMAGE_PATH
        )

        tech_stack.click_submit()

        time.sleep(2)

        print(
            "Duplicate submission executed"
        )

        print(
            "N14 DUPLICATE TECHNOLOGY COMPLETED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 20 - NEGATIVE INVALID IMAGE PATH
# ============================================================

def test_add_invalid_image_path():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N15 INVALID IMAGE PATH "
            "=========="
        )

        technology = generate_technology()

        tech_stack.enter_technology(
            technology
        )

        tech_stack.select_category(
            VALID_CATEGORY
        )

        invalid_image = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "invalid_image.jpg"
            )
        )

        try:

            tech_stack.upload_image(
                invalid_image
            )

            assert False, (
                "Invalid image path was accepted"
            )

        except FileNotFoundError:

            print(
                "Invalid image path correctly rejected"
            )

        print(
            "N15 INVALID IMAGE PATH PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 21 - NEGATIVE SYMBOLS ONLY
# ============================================================

def test_add_symbols_only_technology():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "N16 SYMBOLS ONLY "
            "=========="
        )

        tech_stack.enter_technology(
            "!!!!!!"
        )

        tech_stack.select_category(
            VALID_CATEGORY
        )

        tech_stack.upload_image(
            IMAGE_PATH
        )

        tech_stack.click_submit()

        time.sleep(2)

        assert tech_stack.is_form_displayed(), (
            "Form was not displayed after symbols-only input"
        )

        print(
            "N16 SYMBOLS ONLY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()

# ============================================================
# EDIT TESTS
# ============================================================

# ------------------------------------------------------------
# EDIT 01 - EDIT EXISTING TECHNOLOGY NAME
# ------------------------------------------------------------

def test_edit_existing_technology_name():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "E01 EDIT EXISTING TECHNOLOGY NAME "
            "=========="
        )

        old_name = (
            tech_stack.get_first_existing_technology()
        )

        new_name = (
            f"Updated Technology "
            f"{generate_random_text()}"
        )

        print(
            "Old Technology:",
            old_name
        )

        print(
            "New Technology:",
            new_name
        )

        assert tech_stack.is_technology_present(
            old_name
        ), (
            f"Existing technology not found: "
            f"{old_name}"
        )

        tech_stack.edit_existing_technology_name(
            old_name,
            new_name
        )

        assert tech_stack.is_technology_present(
            new_name
        ), (
            f"Updated technology not found: "
            f"{new_name}"
        )

        assert not tech_stack.is_technology_present(
            old_name
        ), (
            f"Old technology still exists: "
            f"{old_name}"
        )

        print(
            "E01 EDIT EXISTING TECHNOLOGY NAME PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ------------------------------------------------------------
# EDIT 02 - EDIT WITHOUT CHANGING IMAGE
# ------------------------------------------------------------

def test_edit_technology_without_changing_image():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "E02 EDIT WITHOUT CHANGING IMAGE "
            "=========="
        )

        old_name = (
            tech_stack.get_first_existing_technology()
        )

        new_name = (
            f"Updated Without Image "
            f"{generate_random_text()}"
        )

        print(
            "Old Technology:",
            old_name
        )

        print(
            "New Technology:",
            new_name
        )

        assert tech_stack.is_technology_present(
            old_name
        ), (
            f"Existing technology not found: "
            f"{old_name}"
        )

        # --------------------------------------------------------
        # IMPORTANT:
        #
        # This function changes ONLY the technology name.
        #
        # No image is deleted.
        # No new image is uploaded.
        # Existing image remains unchanged.
        # --------------------------------------------------------

        tech_stack.edit_technology_without_changing_image(
            old_name,
            new_name
        )

        assert tech_stack.is_technology_present(
            new_name
        ), (
            f"Updated technology not found: "
            f"{new_name}"
        )

        assert not tech_stack.is_technology_present(
            old_name
        ), (
            f"Old technology still exists: "
            f"{old_name}"
        )

        print(
            "E02 EDIT WITHOUT CHANGING IMAGE PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ------------------------------------------------------------
# EDIT 03 - EDIT TECHNOLOGY CATEGORY
# ------------------------------------------------------------

def test_edit_technology_category():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "E03 EDIT TECHNOLOGY CATEGORY "
            "=========="
        )

        existing_technology = (
            tech_stack.get_first_existing_technology()
        )

        new_category = "Backend"

        print(
            "Technology:",
            existing_technology
        )

        print(
            "New Category:",
            new_category
        )

        assert tech_stack.is_technology_present(
            existing_technology
        ), (
            f"Technology not found: "
            f"{existing_technology}"
        )

        available_categories = (
            tech_stack.get_available_categories()
        )

        assert any(
            category.lower()
            == new_category.lower()
            for category in available_categories
        ), (
            f"Category '{new_category}' "
            f"was not found. "
            f"Available categories: "
            f"{available_categories}"
        )

        tech_stack.edit_technology_category(
            existing_technology,
            new_category
        )

        assert tech_stack.is_technology_present(
            existing_technology
        ), (
            "Technology disappeared after "
            "category update"
        )

        print(
            "E03 EDIT TECHNOLOGY CATEGORY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()



# ============================================================
# 23 - DELETE CANCEL
# ============================================================

def test_cancel_delete_existing_tech_stack():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "D01 DELETE CANCEL "
            "=========="
        )

        existing_technology = (
            tech_stack.get_first_existing_technology()
        )

        print(
            "Existing Technology:",
            existing_technology
        )

        assert tech_stack.is_technology_present(
            existing_technology
        ), (
            f"Technology not found: "
            f"{existing_technology}"
        )

        tech_stack.click_delete_for_technology(
            existing_technology
        )

        time.sleep(2)

        tech_stack.cancel_delete()

        time.sleep(2)

        assert tech_stack.is_technology_present(
            existing_technology
        ), (
            "Technology disappeared after "
            "delete cancellation"
        )

        print(
            "Technology still exists:",
            existing_technology
        )

        print(
            "D01 DELETE CANCEL PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 24 - DELETE EXISTING TECHNOLOGY
# ============================================================

def test_delete_existing_tech_stack():

    driver, tech_stack, wait = (
        open_tech_stack()
    )

    try:

        print(
            "\n========== "
            "D02 DELETE EXISTING TECH STACK "
            "=========="
        )

        existing_technology = (
            tech_stack.get_first_existing_technology()
        )

        print(
            "Technology to delete:",
            existing_technology
        )

        assert tech_stack.is_technology_present(
            existing_technology
        ), (
            f"Technology not found: "
            f"{existing_technology}"
        )

        tech_stack.click_delete_for_technology(
            existing_technology
        )

        time.sleep(2)

        tech_stack.confirm_delete()

        time.sleep(2)

        tech_stack.wait_until_technology_deleted(
            existing_technology
        )

        assert not tech_stack.is_technology_present(
            existing_technology
        ), (
            "Technology still exists after deletion"
        )

        print(
            "Deleted Technology:",
            existing_technology
        )

        print(
            "D02 DELETE EXISTING TECH STACK PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()