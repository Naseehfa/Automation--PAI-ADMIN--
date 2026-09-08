import os
import time

from random import choices
from string import ascii_letters

from utils.driver_setup import get_driver

from config.config import (
    URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage
from pages.main_services_page import MainServicesPage

from selenium.webdriver.support.ui import WebDriverWait


# ============================================================
# URL
# ============================================================

MAIN_SERVICES_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/main-services"
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
# SAMPLE JPEG PATH
# ============================================================

SAMPLE_JPEG_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "sample_640×426.jpeg"
    )
)


# ============================================================
# GENERATE RANDOM SERVICE DATA
# ============================================================

def generate_service_data():

    random_text = ''.join(
        choices(
            ascii_letters,
            k=6
        )
    )

    service_name = (
        f"Software Testing {random_text}"
    )

    description = (
        f"Professional software testing "
        f"and quality assurance service "
        f"created for automation testing "
        f"{random_text}."
    )

    return service_name, description


# ============================================================
# GENERATE RANDOM LETTERS
# ============================================================

def generate_random_letters(
    length=6
):

    return ''.join(
        choices(
            ascii_letters,
            k=length
        )
    )


# ============================================================
# HELPER - LOGIN
# ============================================================

def open_admin_page():

    driver = get_driver()

    driver.get(URL)

    # Slightly zoom out browser
    driver.execute_script(
        "document.body.style.zoom='75%'"
    )

    time.sleep(4)

    print(
        "\n========== LOGIN =========="
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
        "login" not in d.current_url
    )

    time.sleep(4)

    print(
        "Current URL:",
        driver.current_url
    )

    return driver, wait


# ============================================================
# HELPER - OPEN MAIN SERVICES
# ============================================================

def open_main_services():

    driver, wait = open_admin_page()

    main_services = MainServicesPage(
        driver
    )

    main_services.open_main_services()

    wait.until(
        lambda d:
        "main-services" in d.current_url
    )

    assert (
        "main-services"
        in driver.current_url
    )

    return (
        driver,
        main_services,
        wait
    )


# ============================================================
# P01 - VALID SERVICE
# ============================================================

def test_add_service_valid_data():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== P01 VALID SERVICE =========="
        )

        service_name, description = (
            generate_service_data()
        )

        print(
            "Generated Service Name:",
            service_name
        )

        main_services.add_service(
            service_name=service_name,
            description=description,
            service_image=IMAGE_PATH
        )

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "Created Service:",
            service_name
        )

        print(
            "P01 VALID SERVICE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# P02 - SECOND VALID SERVICE
# ============================================================

def test_add_second_valid_service():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== P02 SECOND VALID SERVICE =========="
        )

        service_name, description = (
            generate_service_data()
        )

        main_services.add_service(
            service_name=service_name,
            description=description,
            service_image=IMAGE_PATH
        )

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "Created Service:",
            service_name
        )

        print(
            "P02 SECOND VALID SERVICE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# P03 - MULTIPLE WORD SERVICE
# ============================================================

def test_add_service_multiple_words():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== P03 MULTIPLE WORD SERVICE =========="
        )

        random_text = (
            generate_random_letters()
        )

        service_name = (
            f"Mobile Application Development "
            f"{random_text}"
        )

        description = (
            f"Development of Android and "
            f"iOS mobile applications "
            f"{random_text}."
        )

        main_services.add_service(
            service_name=service_name,
            description=description,
            service_image=IMAGE_PATH
        )

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "Created Service:",
            service_name
        )

        print(
            "P03 MULTIPLE WORD SERVICE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# P04 - MIXED CASE
# ============================================================

def test_add_service_mixed_case():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== P04 MIXED CASE SERVICE =========="
        )

        random_text = (
            generate_random_letters()
        )

        service_name = (
            f"Cloud Computing {random_text}"
        )

        description = (
            f"Cloud infrastructure and "
            f"deployment services "
            f"{random_text}."
        )

        main_services.add_service(
            service_name=service_name,
            description=description,
            service_image=IMAGE_PATH
        )

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "Created Service:",
            service_name
        )

        print(
            "P04 MIXED CASE SERVICE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N01 - ALL FIELDS EMPTY
# ============================================================

def test_add_service_all_fields_empty():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N01 ALL FIELDS EMPTY =========="
        )

        main_services.fill_service_form(
            service_name="",
            description="",
            service_image=""
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N01 ALL FIELDS EMPTY PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N02 - EMPTY SERVICE NAME
# ============================================================

def test_add_service_empty_name():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N02 EMPTY SERVICE NAME =========="
        )

        main_services.fill_service_form(
            service_name="",
            description="Valid description",
            service_image=IMAGE_PATH
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N02 EMPTY SERVICE NAME PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N03 - EMPTY DESCRIPTION
# ============================================================

def test_add_service_empty_description():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N03 EMPTY DESCRIPTION =========="
        )

        service_name, _ = (
            generate_service_data()
        )

        main_services.fill_service_form(
            service_name=service_name,
            description="",
            service_image=IMAGE_PATH
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N03 EMPTY DESCRIPTION PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N04 - EMPTY IMAGE
# ============================================================

def test_add_service_empty_image():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N04 EMPTY IMAGE =========="
        )

        service_name, description = (
            generate_service_data()
        )

        main_services.fill_service_form(
            service_name=service_name,
            description=description,
            service_image=""
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N04 EMPTY IMAGE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N05 - SPACES IN SERVICE NAME
# ============================================================

def test_add_service_spaces_name():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N05 SPACES IN SERVICE NAME =========="
        )

        main_services.fill_service_form(
            service_name="     ",
            description="Valid description",
            service_image=IMAGE_PATH
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N05 SPACES NAME PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N06 - SPACES IN DESCRIPTION
# ============================================================

def test_add_service_spaces_description():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N06 SPACES IN DESCRIPTION =========="
        )

        service_name, _ = (
            generate_service_data()
        )

        main_services.fill_service_form(
            service_name=service_name,
            description="     ",
            service_image=IMAGE_PATH
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N06 SPACES DESCRIPTION PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N07 - NUMERIC SERVICE NAME
# ============================================================

def test_add_service_numeric_name():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N07 NUMERIC SERVICE NAME =========="
        )

        main_services.fill_service_form(
            service_name="123456789",
            description="Valid description",
            service_image=IMAGE_PATH
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N07 NUMERIC SERVICE NAME PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N08 - SPECIAL CHARACTERS
# ============================================================

def test_add_service_special_characters():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N08 SPECIAL CHARACTERS =========="
        )

        main_services.fill_service_form(
            service_name="@#$%^&*",
            description="Valid description",
            service_image=IMAGE_PATH
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N08 SPECIAL CHARACTERS PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N09 - HTML / SCRIPT INPUT
# ============================================================

def test_add_service_html_input():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N09 HTML INPUT =========="
        )

        main_services.fill_service_form(
            service_name="<script>alert('XSS')</script>",
            description="Valid description",
            service_image=IMAGE_PATH
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N09 HTML INPUT PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N10 - VERY LONG SERVICE NAME
# ============================================================

def test_add_service_long_name():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N10 LONG SERVICE NAME =========="
        )

        long_name = "A" * 50

        main_services.fill_service_form(
            service_name=long_name,
            description="Valid description",
            service_image=IMAGE_PATH
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N10 LONG SERVICE NAME PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N11 - VERY LONG DESCRIPTION
# ============================================================

def test_add_service_long_description():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N11 LONG DESCRIPTION =========="
        )

        service_name, _ = (
            generate_service_data()
        )

        long_description = "A" * 150

        main_services.fill_service_form(
            service_name=service_name,
            description=long_description,
            service_image=IMAGE_PATH
        )

        main_services.click_submit()

        time.sleep(4)

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N11 LONG DESCRIPTION PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# N12 - INVALID IMAGE
# ============================================================

def test_add_service_invalid_image():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== N12 INVALID IMAGE =========="
        )

        # --------------------------------------------------------
        # JPEG PATH FROM PROJECT ROOT
        # --------------------------------------------------------

        invalid_image = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "sample_640×426.jpeg"
            )
        )

        # --------------------------------------------------------
        # VERIFY FILE EXISTS
        # --------------------------------------------------------

        assert os.path.exists(
            invalid_image
        ), (
            f"sample_640×426.jpeg was not found: "
            f"{invalid_image}"
        )

        # --------------------------------------------------------
        # VERIFY JPEG EXTENSION
        # --------------------------------------------------------

        assert invalid_image.lower().endswith(
            ".jpeg"
        ), (
            "The selected file is not a JPEG file."
        )

        service_name, description = (
            generate_service_data()
        )

        print(
            "Service Name:",
            service_name
        )

        print(
            "Invalid Image Path:",
            invalid_image
        )

        print(
            "Testing JPEG as invalid image format..."
        )

        # --------------------------------------------------------
        # UPLOAD JPEG
        # --------------------------------------------------------

        main_services.fill_service_form(
            service_name=service_name,
            description=description,
            service_image=invalid_image
        )

        # --------------------------------------------------------
        # SUBMIT
        # --------------------------------------------------------

        main_services.click_submit()

        time.sleep(4)

        # --------------------------------------------------------
        # VERIFY PAGE
        # --------------------------------------------------------

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "N12 INVALID IMAGE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# P14 - EDIT SERVICE
# ============================================================

def test_edit_service_name():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== P14 EDIT SERVICE =========="
        )

        new_service_name = "Manual"

        print(
            "New Service Name:",
            new_service_name
        )

        main_services.edit_service(
            new_service_name
        )

        wait.until(
            lambda d:
            "main-services"
            in d.current_url
        )

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "Service updated to:",
            new_service_name
        )

        print(
            "P14 EDIT SERVICE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# P15 - DELETE CANCEL
# ============================================================

def test_delete_service_cancel():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== P15 DELETE CANCEL =========="
        )

        # Open delete confirmation modal
        main_services.click_delete_service()

        # Click Cancel
        main_services.cancel_delete()

        # Verify we remain on Main Services
        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "Delete cancelled successfully."
        )

        print(
            "P15 DELETE CANCEL PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# P16 - DELETE CLOSE BUTTON
# ============================================================

def test_delete_service_close():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== P16 DELETE CLOSE =========="
        )

        # Open delete confirmation modal
        main_services.click_delete_service()

        # Click X / Close button
        main_services.close_delete_modal()

        # Verify we remain on Main Services
        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "Delete modal closed successfully."
        )

        print(
            "P16 DELETE CLOSE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# P17 - DELETE SERVICE
# ============================================================

def test_delete_service():

    driver, main_services, wait = (
        open_main_services()
    )

    try:

        print(
            "\n========== P17 DELETE SERVICE =========="
        )

        # --------------------------------------------------------
        # Open delete confirmation
        # --------------------------------------------------------

        main_services.click_delete_service()

        print(
            "Delete confirmation modal opened."
        )

        # --------------------------------------------------------
        # Confirm deletion
        # --------------------------------------------------------

        main_services.confirm_delete()

        time.sleep(4)

        # --------------------------------------------------------
        # Verify page
        # --------------------------------------------------------

        assert (
            "main-services"
            in driver.current_url
        )

        print(
            "Service deleted successfully."
        )

        print(
            "P17 DELETE SERVICE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()