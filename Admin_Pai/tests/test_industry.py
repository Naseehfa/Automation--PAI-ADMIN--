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
from pages.industry_page import IndustryPage

from selenium.webdriver.support.ui import WebDriverWait


# ============================================================
# URL
# ============================================================

INDUSTRY_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/industry"
)


# ============================================================
# PROJECT ROOT
# ============================================================

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


# ============================================================
# ROOT FOLDER IMAGES
# ============================================================

JPG_IMAGE_PATH = os.path.join(
    ROOT_DIR,
    "image.jpg"
)

PNG_IMAGE_PATH = os.path.join(
    ROOT_DIR,
    "image.png"
)

EDIT_IMAGE_PATH = os.path.join(
    ROOT_DIR,
    "OIP.jpg"
)


# ============================================================
# INVALID IMAGE
# ============================================================

INVALID_IMAGE_PATH = os.path.join(
    ROOT_DIR,
    "sample_640×426.jpegs"
)


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
# GENERATE INDUSTRY
# ============================================================

def generate_industry():

    return (
        f"Industry "
        f"{generate_random_text()}"
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

    login = LoginPage(driver)

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

    return driver, wait


# ============================================================
# OPEN INDUSTRY
# ============================================================

def open_industry():

    driver, wait = open_admin_page()

    industry = IndustryPage(driver)

    industry.navigate_to_industry()

    wait.until(
        lambda d:
        "/admin/industry"
        in d.current_url
    )

    assert (
        "/admin/industry"
        in driver.current_url
    )

    time.sleep(2)

    return driver, industry, wait


# ============================================================
# 01 - NAVIGATION
# ============================================================

def test_industry_navigation():

    driver, wait = open_admin_page()

    try:

        print(
            "\n========== "
            "P01 INDUSTRY NAVIGATION "
            "=========="
        )

        industry = IndustryPage(driver)

        industry.navigate_to_industry()

        wait.until(
            lambda d:
            "/admin/industry"
            in d.current_url
        )

        assert (
            driver.current_url
            == INDUSTRY_URL
        )

        print(
            "P01 INDUSTRY NAVIGATION PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 02 - VALID INDUSTRY + JPG
# ============================================================

def test_add_industry_valid_data():

    driver, industry, wait = open_industry()

    try:

        print(
            "\n========== "
            "P02 VALID INDUSTRY + JPG "
            "=========="
        )

        assert os.path.isfile(
            JPG_IMAGE_PATH
        ), (
            f"Valid JPG does not exist:\n"
            f"{JPG_IMAGE_PATH}"
        )

        industry_name = generate_industry()

        industry.add_industry_jpg(
            industry_name,
            JPG_IMAGE_PATH
        )

        assert (
            driver.current_url
            == INDUSTRY_URL
        )

        assert industry.wait_until_industry_present(
            industry_name,
            timeout=15
        ), (
            f"New industry was not found: "
            f"{industry_name}"
        )

        print(
            "Industry:",
            industry_name
        )

        print(
            "P02 VALID INDUSTRY + JPG PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 09 - ALL EMPTY
# ============================================================

def test_add_industry_all_empty():

    driver, industry, wait = open_industry()

    try:

        industry.enter_industry("")

        industry.click_submit()

        time.sleep(2)

        assert industry.is_form_displayed()

        print(
            "N01 ALL EMPTY PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 10 - EMPTY INDUSTRY + JPG
# ============================================================

def test_add_empty_industry():

    driver, industry, wait = open_industry()

    try:

        industry.enter_industry("")

        industry.upload_jpg(
            JPG_IMAGE_PATH
        )

        industry.click_submit()

        time.sleep(2)

        assert industry.is_form_displayed()

        print(
            "N02 EMPTY INDUSTRY PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 11 - EMPTY IMAGE
# ============================================================

def test_add_empty_image():

    driver, industry, wait = open_industry()

    try:

        industry_name = generate_industry()

        industry.enter_industry(
            industry_name
        )

        industry.click_submit()

        time.sleep(2)

        assert industry.is_form_displayed()

        print(
            "N03 EMPTY IMAGE PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 12 - SPACES ONLY
# ============================================================

def test_add_spaces_only_industry():

    driver, industry, wait = open_industry()

    try:

        industry.enter_industry(
            "       "
        )

        industry.upload_jpg(
            JPG_IMAGE_PATH
        )

        industry.click_submit()

        time.sleep(2)

        assert industry.is_form_displayed()

        print(
            "N04 SPACES ONLY PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 13 - NUMERIC ONLY
# ============================================================

def test_add_numeric_only_industry():

    driver, industry, wait = open_industry()

    try:

        industry.enter_industry(
            "123456789"
        )

        industry.upload_jpg(
            JPG_IMAGE_PATH
        )

        industry.click_submit()

        time.sleep(2)

        assert industry.is_form_displayed()

        print(
            "N05 NUMERIC ONLY PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 14 - SPECIAL CHARACTERS
# ============================================================

def test_add_special_character_industry():

    driver, industry, wait = open_industry()

    try:

        industry.enter_industry(
            "@#$%^&*"
        )

        industry.upload_jpg(
            JPG_IMAGE_PATH
        )

        industry.click_submit()

        time.sleep(2)

        assert industry.is_form_displayed()

        print(
            "N06 SPECIAL CHARACTERS PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 15 - SYMBOLS ONLY
# ============================================================

def test_add_symbols_only_industry():

    driver, industry, wait = open_industry()

    try:

        industry.enter_industry(
            "!!!!!!"
        )

        industry.upload_jpg(
            JPG_IMAGE_PATH
        )

        industry.click_submit()

        time.sleep(2)

        assert industry.is_form_displayed()

        print(
            "N07 SYMBOLS ONLY PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 16 - VERY LONG INDUSTRY
# ============================================================

def test_add_very_long_industry():

    driver, industry, wait = open_industry()

    try:

        long_industry = "A" * 30

        industry.enter_industry(
            long_industry
        )

        industry.upload_jpg(
            JPG_IMAGE_PATH
        )

        industry.click_submit()

        time.sleep(2)

        assert industry.is_form_displayed()

        print(
            "N08 VERY LONG INDUSTRY PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()




# ============================================================
# 19 - INVALID IMAGE PATH
# ============================================================

def test_add_invalid_image_path():

    driver, industry, wait = open_industry()

    try:

        industry_name = generate_industry()

        industry.enter_industry(
            industry_name
        )

        invalid_path = os.path.join(
            ROOT_DIR,
            "file_that_does_not_exist.jpg"
        )

        try:

            industry.upload_image(
                invalid_path
            )

            raise AssertionError(
                "Invalid image path was accepted"
            )

        except FileNotFoundError:

            print(
                "Invalid image path correctly rejected"
            )

        print(
            "N11 INVALID IMAGE PATH PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 20 - EMPTY STRING
# ============================================================

def test_add_empty_string_industry():

    driver, industry, wait = open_industry()

    try:

        industry.enter_industry("")

        industry.upload_jpg(
            JPG_IMAGE_PATH
        )

        industry.click_submit()

        time.sleep(2)

        assert industry.is_form_displayed()

        print(
            "N12 EMPTY STRING PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 21 - EDIT EXISTING INDUSTRY NAME
# ============================================================

def test_edit_existing_industry_name():

    driver, industry, wait = open_industry()

    try:

        print(
            "\n================================================"
        )
        print(
            "E01 EDIT EXISTING INDUSTRY NAME"
        )
        print(
            "================================================"
        )

        # ----------------------------------------------------
        # GET EXISTING INDUSTRY
        # ----------------------------------------------------

        old_name = (
            industry.get_first_existing_industry()
        )

        # ----------------------------------------------------
        # GENERATE NEW NAME
        # ----------------------------------------------------

        new_name = (
            f"Updated Industry "
            f"{generate_random_text()}"
        )

        print(
            "Old Industry Name:",
            old_name
        )

        print(
            "New Industry Name:",
            new_name
        )

        # ----------------------------------------------------
        # EDIT NAME ONLY
        # IMAGE IS NOT TOUCHED
        # ----------------------------------------------------

        industry.edit_existing_industry_name(
            old_name,
            new_name
        )

        print(
            "E01 EDIT EXISTING INDUSTRY NAME PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 22 - EDIT INDUSTRY WITHOUT CHANGING IMAGE
# ============================================================

def test_edit_industry_without_changing_image():

    driver, industry, wait = open_industry()

    try:

        print(
            "\n================================================"
        )
        print(
            "E02 EDIT INDUSTRY WITHOUT CHANGING IMAGE"
        )
        print(
            "================================================"
        )

        # ----------------------------------------------------
        # GET EXISTING INDUSTRY
        # ----------------------------------------------------

        old_name = (
            industry.get_first_existing_industry()
        )

        # ----------------------------------------------------
        # GENERATE NEW NAME
        # ----------------------------------------------------

        new_name = (
            f"Image Preserved Industry "
            f"{generate_random_text()}"
        )

        print(
            "Old Industry Name:",
            old_name
        )

        print(
            "New Industry Name:",
            new_name
        )

        # ----------------------------------------------------
        # EDIT NAME
        #
        # NO IMAGE DELETE
        # NO IMAGE UPLOAD
        # ----------------------------------------------------

        industry.edit_industry_without_changing_image(
            old_name,
            new_name
        )

        print(
            "E02 EDIT WITHOUT CHANGING IMAGE PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 23 - EDIT INDUSTRY NAME + CHANGE IMAGE
# ============================================================

def test_edit_industry_name_and_photo():

    driver, industry, wait = open_industry()

    try:

        print(
            "\n================================================"
        )
        print(
            "E03 EDIT INDUSTRY NAME + CHANGE PHOTO"
        )
        print(
            "================================================"
        )

        # ----------------------------------------------------
        # IMPORTANT:
        # OIP.jpg IS IN PROJECT ROOT
        # ----------------------------------------------------

        assert os.path.isfile(
            EDIT_IMAGE_PATH
        ), (
            f"OIP.jpg was not found in project root:\n"
            f"{EDIT_IMAGE_PATH}"
        )

        print(
            "Edit image:",
            EDIT_IMAGE_PATH
        )

        # ----------------------------------------------------
        # GET EXISTING INDUSTRY
        # ----------------------------------------------------

        old_name = (
            industry.get_first_existing_industry()
        )

        new_name = (
            f"Updated Industry "
            f"{generate_random_text()}"
        )

        print(
            "Old Industry Name:",
            old_name
        )

        print(
            "New Industry Name:",
            new_name
        )

        # ----------------------------------------------------
        # CLICK EDIT
        # ----------------------------------------------------

        industry.click_edit_for_industry(
            old_name
        )

        assert industry.is_edit_form_displayed()

        # ----------------------------------------------------
        # CHANGE NAME
        # ----------------------------------------------------

        industry.edit_industry_name(
            new_name
        )

        # ----------------------------------------------------
        # DELETE OLD IMAGE
        # ----------------------------------------------------

        industry.delete_old_edit_image()

        # ----------------------------------------------------
        # UPLOAD OIP.jpg FROM PROJECT ROOT
        # ----------------------------------------------------

        industry.upload_edit_jpg(
            EDIT_IMAGE_PATH
        )

        # ----------------------------------------------------
        # SAVE
        # ----------------------------------------------------

        industry.click_edit_save()

        # ----------------------------------------------------
        # WAIT
        # ----------------------------------------------------

        assert industry.wait_until_edit_form_closed(
            timeout=15
        ), (
            "Edit form did not close after save"
        )

        # ----------------------------------------------------
        # VERIFY NEW NAME
        # ----------------------------------------------------

        assert industry.wait_until_industry_present(
            new_name,
            timeout=15
        ), (
            f"Updated industry was not found:\n"
            f"{new_name}"
        )

        # ----------------------------------------------------
        # VERIFY OLD NAME REMOVED
        # ----------------------------------------------------

        assert not industry.is_industry_present(
            old_name
        ), (
            f"Old industry name still exists:\n"
            f"{old_name}"
        )

        print(
            "E03 EDIT INDUSTRY NAME + CHANGE PHOTO PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 24 - DELETE CANCEL
# ============================================================

def test_cancel_delete_existing_industry():

    driver, industry, wait = open_industry()

    try:

        print(
            "\n========== "
            "D01 DELETE CANCEL "
            "=========="
        )

        existing_industry = (
            industry.get_first_existing_industry()
        )

        assert industry.is_industry_present(
            existing_industry
        )

        industry.click_delete_for_industry(
            existing_industry
        )

        assert industry.is_delete_modal_displayed()

        industry.cancel_delete()

        assert industry.wait_until_industry_present(
            existing_industry,
            timeout=10
        )

        print(
            "D01 DELETE CANCEL PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()


# ============================================================
# 25 - DELETE EXISTING INDUSTRY
# ============================================================

def test_delete_existing_industry():

    driver, industry, wait = open_industry()

    try:

        print(
            "\n========== "
            "D02 DELETE EXISTING INDUSTRY "
            "=========="
        )

        existing_industry = (
            industry.get_first_existing_industry()
        )

        assert industry.is_industry_present(
            existing_industry
        )

        industry.click_delete_for_industry(
            existing_industry
        )

        assert industry.is_delete_modal_displayed()

        industry.confirm_delete()

        industry.wait_until_industry_deleted(
            existing_industry,
            timeout=15
        )

        assert not industry.is_industry_present(
            existing_industry
        )

        print(
            "Deleted Industry:",
            existing_industry
        )

        print(
            "D02 DELETE EXISTING INDUSTRY PASSED"
        )

    finally:

        time.sleep(2)
        driver.quit()