
import time

import pytest

from utils.driver_setup import get_driver

from config.config import (
    URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage
from pages.employee_page import EmployeePage


# ============================================================
# DRIVER FIXTURE
# ============================================================

@pytest.fixture
def driver():

    driver = get_driver()

    driver.maximize_window()

    yield driver

    driver.quit()


# ============================================================
# EMPLOYEE PAGE FIXTURE
# ============================================================

@pytest.fixture
def employee_page(driver):

    # --------------------------------------------------------
    # LOGIN
    # --------------------------------------------------------

    login_page = LoginPage(driver)

    driver.get(URL)

    time.sleep(2)

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    time.sleep(4)

    # --------------------------------------------------------
    # OPEN EMPLOYEE / TEAM PAGE
    # --------------------------------------------------------

    employee_page = EmployeePage(driver)

    employee_page.open_employee_page()

    return employee_page


# ============================================================
# TEST 1
# Verify Edit icon opens selected employee record
# ============================================================

def test_verify_edit_icon_opens_selected_employee_record(
    employee_page
):

    print(
        "\nTEST 1: Verify Edit icon opens "
        "selected employee record"
    )

    # Click first employee Edit icon
    employee_page.click_edit_first_employee()

    # Verify edit form
    assert employee_page.is_edit_form_open(), (
        "FAIL: Employee Edit form did not open "
        "after clicking Edit icon."
    )

    print(
        "PASS: Edit icon opened the selected "
        "employee record."
    )


# ============================================================
# TEST 2
# Verify Edit form populates existing employee details
# correctly
# ============================================================

def test_verify_edit_form_populates_existing_employee_details(
    employee_page
):

    print(
        "\nTEST 2: Verify Edit form populates "
        "existing employee details correctly"
    )

    # Open edit form
    employee_page.click_edit_first_employee()

    assert employee_page.is_edit_form_open(), (
        "Employee Edit form did not open."
    )

    # Read existing values
    employee_name = (
        employee_page.get_employee_name()
    )

    position = (
        employee_page.get_position()
    )

    linkedin = (
        employee_page.get_linkedin()
    )

    description = (
        employee_page.get_description()
    )

    print(
        "\nExisting Employee Details:"
    )

    print(
        "Name:",
        employee_name
    )

    print(
        "Position:",
        position
    )

    print(
        "LinkedIn:",
        linkedin
    )

    print(
        "Description:",
        description
    )

    # Name should be populated
    assert employee_name, (
        "FAIL: Employee Name field is empty."
    )

    # Position should be populated
    assert position, (
        "FAIL: Employee Position field is empty."
    )

    print(
        "PASS: Existing employee details "
        "are populated correctly."
    )


# ============================================================
# TEST 3
# Verify employee Position can be changed
# during editing
# ============================================================

def test_verify_employee_position_can_be_changed(
    employee_page
):

    print(
        "\nTEST 3: Verify employee Position "
        "can be changed during editing"
    )

    # Open edit form
    employee_page.click_edit_first_employee()

    assert employee_page.is_edit_form_open(), (
        "Employee Edit form did not open."
    )

    # Get original position
    original_position = (
        employee_page.get_position()
    )

    # Change position
    changed_position = (
        employee_page.change_position()
    )

    print(
        "Original Position:",
        original_position
    )

    print(
        "Changed Position:",
        changed_position
    )

    # Verify selection changed
    assert changed_position != original_position, (
        "FAIL: Employee Position was not changed."
    )

    # Keep other required fields valid
    assert employee_page.get_employee_name(), (
        "Employee Name is empty before update."
    )

    # Click Update
    employee_page.click_update()

    # Success message
    success_message = (
        employee_page.get_success_message()
    )

    print(
        "Success Message:",
        success_message
    )

    assert success_message, (
        "FAIL: Success message was not displayed "
        "after changing employee Position."
    )

    print(
        "PASS: Employee Position was changed "
        "and update completed."
    )


# ============================================================
# TEST 4
# Verify employee update is prevented
# when Name is cleared
# ============================================================

def test_verify_employee_update_prevented_when_name_cleared(
    employee_page
):

    print(
        "\nTEST 4: Verify employee update is prevented "
        "when Name is cleared"
    )

    # Open edit form
    employee_page.click_edit_first_employee()

    assert employee_page.is_edit_form_open(), (
        "Employee Edit form did not open."
    )

    # Clear Name
    employee_page.clear_employee_name()

    # Make sure Position remains selected
    position = employee_page.get_position()

    assert position, (
        "Position is unexpectedly empty. "
        "Test requires Position to remain valid."
    )

    # Click Update
    employee_page.click_update()

    # Give frontend validation time
    time.sleep(2)

    # Get validation
    validation_messages = (
        employee_page.get_validation_messages()
    )

    print(
        "Validation Messages:",
        validation_messages
    )

    # Update should be prevented
    assert validation_messages, (
        "FAIL: Employee update was not prevented "
        "when Name field was cleared."
    )

    print(
        "PASS: Employee update was prevented "
        "when Name was cleared."
    )


# ============================================================
# TEST 5
# Verify employee update is prevented
# without Position selection
# ============================================================

def test_verify_employee_update_prevented_without_position(
    employee_page
):

    print(
        "\nTEST 5: Verify employee update is prevented "
        "without Position selection"
    )

    # Open edit form
    employee_page.click_edit_first_employee()

    assert employee_page.is_edit_form_open(), (
        "Employee Edit form did not open."
    )

    # Name must remain valid
    employee_name = (
        employee_page.get_employee_name()
    )

    assert employee_name, (
        "Employee Name is already empty. "
        "Test requires valid Name."
    )

    # Clear Position
    employee_page.clear_position()

    # Click Update
    employee_page.click_update()

    time.sleep(2)

    # Get validation
    validation_messages = (
        employee_page.get_validation_messages()
    )

    print(
        "Validation Messages:",
        validation_messages
    )

    # Position should be required
    assert validation_messages, (
        "FAIL: Employee update was not prevented "
        "without Position selection."
    )

    print(
        "PASS: Employee update was prevented "
        "without Position selection."
    )


# ============================================================
# TEST 6
# Verify invalid LinkedIn URL cannot be saved
# during update
# ============================================================

def test_verify_invalid_linkedin_url_cannot_be_saved(
    employee_page
):

    print(
        "\nTEST 6: Verify invalid LinkedIn URL "
        "cannot be saved during update"
    )

    # Open edit form
    employee_page.click_edit_first_employee()

    assert employee_page.is_edit_form_open(), (
        "Employee Edit form did not open."
    )

    # Keep Name valid
    assert employee_page.get_employee_name(), (
        "Employee Name is empty."
    )

    # Keep Position valid
    assert employee_page.get_position(), (
        "Position is empty."
    )

    # Invalid LinkedIn URL
    invalid_linkedin = "invalid-linkedin-url"

    employee_page.enter_linkedin(
        invalid_linkedin
    )

    # Click Update
    employee_page.click_update()

    time.sleep(2)

    # Check validation
    validation_messages = (
        employee_page.get_validation_messages()
    )

    print(
        "Validation Messages:",
        validation_messages
    )

    # Also inspect native validation
    linkedin_field = employee_page.driver.find_element(
        *employee_page.linkedin_field
    )

    native_validation = (
        linkedin_field.get_attribute(
            "validationMessage"
        )
        or ""
    ).strip()

    print(
        "LinkedIn Native Validation:",
        native_validation
    )

    # Either application validation or HTML5 validation
    assert (
        validation_messages
        or native_validation
    ), (
        "FAIL: Invalid LinkedIn URL was accepted "
        "without validation."
    )

    print(
        "PASS: Invalid LinkedIn URL was prevented "
        "from being saved."
    )


# ============================================================
# TEST 7
# Verify only modified employee field is updated
# ============================================================

def test_verify_only_modified_employee_field_is_updated(
    employee_page
):

    print(
        "\nTEST 7: Verify only modified employee "
        "field is updated"
    )

    # Open edit form
    employee_page.click_edit_first_employee()

    assert employee_page.is_edit_form_open(), (
        "Employee Edit form did not open."
    )

    # --------------------------------------------------------
    # Capture original values
    # --------------------------------------------------------

    original_name = (
        employee_page.get_employee_name()
    )

    original_position = (
        employee_page.get_position()
    )

    original_linkedin = (
        employee_page.get_linkedin()
    )

    original_description = (
        employee_page.get_description()
    )

    print(
        "\nOriginal values:"
    )

    print(
        "Name:",
        original_name
    )

    print(
        "Position:",
        original_position
    )

    print(
        "LinkedIn:",
        original_linkedin
    )

    print(
        "Description:",
        original_description
    )

    # --------------------------------------------------------
    # Modify ONLY Description
    # --------------------------------------------------------

    updated_description = (
        f"{original_description} - Automation Updated"
    )

    employee_page.enter_description(
        updated_description
    )

    # Do NOT modify:
    # Name
    # Position
    # LinkedIn

    # --------------------------------------------------------
    # Click Update
    # --------------------------------------------------------

    employee_page.click_update()

    success_message = (
        employee_page.get_success_message()
    )

    print(
        "Success Message:",
        success_message
    )

    assert success_message, (
        "FAIL: Success message was not displayed "
        "after updating Description."
    )

    # --------------------------------------------------------
    # Verify form/table refresh
    # --------------------------------------------------------

    time.sleep(2)

    employee_page.refresh_page()

    # Search for updated description
    page_text = employee_page.get_page_text()

    assert updated_description in page_text, (
        "FAIL: Modified Description was not "
        "found after update."
    )

    # Original Name should remain
    assert original_name in page_text, (
        "FAIL: Employee Name was unexpectedly "
        "changed."
    )

    print(
        "PASS: Only the modified employee field "
        "was updated while existing fields remained."
    )

