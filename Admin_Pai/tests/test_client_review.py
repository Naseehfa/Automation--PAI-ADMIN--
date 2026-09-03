
import os
import time
import pytest

from utils.driver_setup import get_driver

from config.config import (
    URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage
from pages.client_review_page import ClientReviewPage


# ============================================================
# TEST DATA
# ============================================================

IMAGE_PATH = os.path.abspath("image.jpg")


# ============================================================
# FIXTURE
# ============================================================

@pytest.fixture
def driver():

    driver = get_driver()

    yield driver

    driver.quit()


# ============================================================
# LOGIN + CLIENT REVIEW FIXTURE
# ============================================================

@pytest.fixture
def client_review_page(driver):

    # --------------------------------------------------------
    # Open Login Page
    # --------------------------------------------------------

    driver.get(URL)

    time.sleep(2)

    # --------------------------------------------------------
    # Login
    # --------------------------------------------------------

    login = LoginPage(driver)

    login.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    # --------------------------------------------------------
    # Wait until login is completed
    # --------------------------------------------------------

    from selenium.webdriver.support.ui import WebDriverWait

    wait = WebDriverWait(driver, 20)

    wait.until(
        lambda d: "login" not in d.current_url.lower()
    )

    time.sleep(2)

    print(
        "After login URL:",
        driver.current_url
    )

    # --------------------------------------------------------
    # Open Client Review
    # --------------------------------------------------------

    client_review = ClientReviewPage(driver)

    client_review.navigate_to_client_review()

    time.sleep(2)

    return client_review


# ============================================================
# PAGE NAVIGATION
# ============================================================

def test_client_review_page_navigation(
    client_review_page
):

    assert (
        "/admin/client-review"
        in client_review_page.driver.current_url
    )


# ============================================================
# POSITIVE TEST CASES
# ============================================================

def test_add_client_review_valid_data(
    client_review_page
):

    client_review_page.fill_client_review_form(
        "John Smith",
        "CEO",
        IMAGE_PATH,
        "Excellent service. I am very happy with the experience."
    )

    client_review_page.click_add_client_review()

    time.sleep(2)


# ------------------------------------------------------------

def test_client_review_role_with_multiple_words(
    client_review_page
):

    role = "Senior Software Engineer"

    client_review_page.enter_client_role(
        role
    )

    assert (
        client_review_page.get_client_role_value()
        == role
    )


# ------------------------------------------------------------

def test_client_review_long_review(
    client_review_page
):

    review = (
        "I had a wonderful experience using this service. "
        "The system was easy to use and the service was very "
        "professional. I would definitely recommend this service "
        "to other customers."
    )

    client_review_page.enter_review_text(
        review
    )

    assert (
        client_review_page.get_review_text_value()
        == review
    )


# ------------------------------------------------------------

def test_client_review_upload_valid_image(
    client_review_page
):

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    time.sleep(1)


# ============================================================
# NEGATIVE TEST CASES - CLIENT NAME
# ============================================================

def test_client_review_empty_client_name(
    client_review_page
):

    client_review_page.enter_client_name("")

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)

    assert (
        client_review_page.is_client_name_error()
    )


# ------------------------------------------------------------

def test_client_review_client_name_numbers_only(
    client_review_page
):

    client_review_page.enter_client_name(
        "123456789"
    )

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ------------------------------------------------------------

def test_client_review_client_name_special_characters(
    client_review_page
):

    client_review_page.enter_client_name(
        "@#$%^&*"
    )

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ------------------------------------------------------------

def test_client_review_client_name_mixed_special_characters(
    client_review_page
):

    client_review_page.enter_client_name(
        "John@123#"
    )

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ------------------------------------------------------------

def test_client_review_client_name_only_spaces(
    client_review_page
):

    client_review_page.enter_client_name(
        "     "
    )

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ============================================================
# NEGATIVE TEST CASES - CLIENT ROLE
# ============================================================

def test_client_review_empty_client_role(
    client_review_page
):

    client_review_page.enter_client_name(
        "John Smith"
    )

    client_review_page.enter_client_role("")

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)

    assert (
        client_review_page.is_client_role_error()
    )


# ------------------------------------------------------------

def test_client_review_role_numbers_only(
    client_review_page
):

    client_review_page.enter_client_name(
        "John Smith"
    )

    client_review_page.enter_client_role(
        "123456"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ------------------------------------------------------------

def test_client_review_role_special_characters(
    client_review_page
):

    client_review_page.enter_client_name(
        "John Smith"
    )

    client_review_page.enter_client_role(
        "@#$%^&*"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ------------------------------------------------------------

def test_client_review_role_only_spaces(
    client_review_page
):

    client_review_page.enter_client_name(
        "John Smith"
    )

    client_review_page.enter_client_role(
        "     "
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ============================================================
# NEGATIVE TEST CASES - REVIEW TEXT
# ============================================================

def test_client_review_empty_review(
    client_review_page
):

    client_review_page.enter_client_name(
        "John Smith"
    )

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text("")

    client_review_page.click_add_client_review()

    time.sleep(1)

    assert (
        client_review_page.is_review_text_error()
    )


# ------------------------------------------------------------

def test_client_review_only_spaces(
    client_review_page
):

    client_review_page.enter_client_name(
        "John Smith"
    )

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "     "
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ------------------------------------------------------------

def test_client_review_special_characters(
    client_review_page
):

    client_review_page.enter_client_name(
        "John Smith"
    )

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "@#$%^&*()"
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ============================================================
# NEGATIVE TEST CASES - PHOTO
# ============================================================

def test_client_review_without_photo(
    client_review_page
):

    client_review_page.enter_client_name(
        "John Smith"
    )

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ============================================================
# NEGATIVE TEST CASES - ALL EMPTY
# ============================================================

def test_client_review_all_fields_empty(
    client_review_page
):

    client_review_page.click_add_client_review()

    time.sleep(1)


# ============================================================
# NEGATIVE TEST CASES - COMBINATIONS
# ============================================================

def test_client_review_empty_name_and_role(
    client_review_page
):

    client_review_page.enter_client_name("")

    client_review_page.enter_client_role("")

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text(
        "Excellent service."
    )

    client_review_page.click_add_client_review()

    time.sleep(1)


# ------------------------------------------------------------

def test_client_review_empty_name_and_review(
    client_review_page
):

    client_review_page.enter_client_name("")

    client_review_page.enter_client_role(
        "Manager"
    )

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text("")

    client_review_page.click_add_client_review()

    time.sleep(1)


# ------------------------------------------------------------

def test_client_review_empty_role_and_review(
    client_review_page
):

    client_review_page.enter_client_name(
        "John Smith"
    )

    client_review_page.enter_client_role("")

    client_review_page.upload_client_photo(
        IMAGE_PATH
    )

    client_review_page.enter_review_text("")

    client_review_page.click_add_client_review()

    time.sleep(1)


# ============================================================
# EDIT CLIENT REVIEW - UPDATE ONLY ROLE
# ============================================================

def test_edit_client_role_valid_data(
    client_review_page
):

    client_review_page.update_client_role(
        "Senior Manager"
    )

    time.sleep(2)


# ============================================================
# EDIT CLIENT REVIEW - UPDATE ONLY NAME
# ============================================================

def test_edit_client_name_valid_data(
    client_review_page
):

    client_review_page.update_client_name(
        "David Smith"
    )

    time.sleep(2)


# ============================================================
# EDIT CLIENT REVIEW - UPDATE ONLY REVIEW
# ============================================================

def test_edit_client_review_text(
    client_review_page
):

    client_review_page.update_client_review_text(
        "This is the updated client review."
    )

    time.sleep(2)


# ============================================================
# EDIT CLIENT REVIEW - UPDATE ONLY PHOTO
# ============================================================

def test_edit_client_photo(
    client_review_page
):

    client_review_page.update_client_photo(
        IMAGE_PATH
    )

    time.sleep(2)


# ============================================================
# EDIT CLIENT REVIEW - UPDATE ALL FIELDS
# ============================================================

def test_edit_client_review_all_fields(
    client_review_page
):

    client_review_page.update_client_review(
        name="Michael Johnson",
        role="Chief Executive Officer",
        photo=IMAGE_PATH,
        review="The service was excellent and I am very satisfied."
    )

    time.sleep(2)


# ============================================================
# EDIT CLIENT REVIEW - MULTIPLE WORD ROLE
# ============================================================

def test_edit_client_role_multiple_words(
    client_review_page
):

    client_review_page.update_client_role(
        "Chief Executive Officer"
    )

    time.sleep(2)


# ============================================================
# EDIT CLIENT REVIEW - EMPTY ROLE
# ============================================================

def test_edit_client_role_empty(
    client_review_page
):

    client_review_page.click_edit_client()

    client_review_page.enter_edit_client_role(
        ""
    )

    client_review_page.click_update_client()

    time.sleep(1)


# ============================================================
# EDIT CLIENT REVIEW - NUMBERS ONLY
# ============================================================

def test_edit_client_role_numbers_only(
    client_review_page
):

    client_review_page.click_edit_client()

    client_review_page.enter_edit_client_role(
        "123456"
    )

    client_review_page.click_update_client()

    time.sleep(1)


# ============================================================
# EDIT CLIENT REVIEW - SPECIAL CHARACTERS
# ============================================================

def test_edit_client_role_special_characters(
    client_review_page
):

    client_review_page.click_edit_client()

    client_review_page.enter_edit_client_role(
        "@#$%^&*"
    )

    client_review_page.click_update_client()

    time.sleep(1)


# ============================================================
# EDIT CLIENT REVIEW - ONLY SPACES
# ============================================================

def test_edit_client_role_only_spaces(
    client_review_page
):

    client_review_page.click_edit_client()

    client_review_page.enter_edit_client_role(
        "     "
    )

    client_review_page.click_update_client()

    time.sleep(1)


# ============================================================
# DELETE CLIENT REVIEW - WITHOUT CONFIRMATION
# ============================================================

def test_delete_client_review_without_confirmation(
    client_review_page
):

    # --------------------------------------------------------
    # Click delete icon
    # --------------------------------------------------------

    client_review_page.click_delete_client()

    # --------------------------------------------------------
    # Verify confirmation popup is displayed
    # --------------------------------------------------------

    assert (
        client_review_page.is_delete_confirmation_displayed()
    ), "Delete confirmation popup was not displayed"

    # --------------------------------------------------------
    # Do NOT click confirmation Delete
    # --------------------------------------------------------

    time.sleep(2)


# ============================================================
# DELETE CLIENT REVIEW - WITH CONFIRMATION
# ============================================================

def test_delete_client_review_with_confirmation(
    client_review_page
):

    # --------------------------------------------------------
    # Click delete icon
    # --------------------------------------------------------

    client_review_page.click_delete_client()

    # --------------------------------------------------------
    # Verify confirmation popup is displayed
    # --------------------------------------------------------

    assert (
        client_review_page.is_delete_confirmation_displayed()
    ), "Delete confirmation popup was not displayed"

    # --------------------------------------------------------
    # Confirm deletion
    # --------------------------------------------------------

    client_review_page.confirm_delete_client()

    # --------------------------------------------------------
    # Verify deletion completed
    # --------------------------------------------------------

    assert (
        client_review_page.is_delete_completed()
    ), "Client review deletion was not completed"

    time.sleep(2)

