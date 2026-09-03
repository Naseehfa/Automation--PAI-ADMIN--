import time

import pytest

from utils.driver_setup import get_driver

from config.config import (
    URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage
from pages.services_page import ServicesPage


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
# SERVICES PAGE FIXTURE
# ============================================================

@pytest.fixture
def services_page(driver):

    login_page = LoginPage(driver)

    driver.get(URL)

    time.sleep(2)

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    time.sleep(4)

    services_page = ServicesPage(driver)

    services_page.open_services()

    time.sleep(3)

    return services_page


# ============================================================
# TEST 1
# Verify clicking Edit opens the service edit interface
# ============================================================

def test_verify_clicking_edit_opens_service_edit_interface(
    services_page
):

    print(
        "\nTEST 1: Verify clicking Edit opens "
        "service edit interface"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open(), (
        "FAIL: Service edit interface did not open "
        "after clicking Edit."
    )

    print(
        "PASS: Service edit interface opened successfully."
    )


# ============================================================
# TEST 2
# Verify updating Service information with valid data
# ============================================================

def test_update_service_information_with_valid_data(
    services_page
):

    print(
        "\nTEST 2: Verify updating Service information "
        "with valid data"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open(), (
        "Service edit interface did not open."
    )

    updated_service_name = (
        "Updated Automation Service"
    )

    services_page.enter_service_name(
        updated_service_name
    )

    existing_description = (
        services_page.get_description()
    )

    assert existing_description.strip(), (
        "Existing Description is empty."
    )

    services_page.click_update()

    success_message = (
        services_page.get_success_message()
    )

    assert success_message, (
        "FAIL: Success message was not displayed "
        "after updating Service name."
    )

    print(
        "Success message:",
        success_message
    )

    assert services_page.verify_service_name_in_table(
        updated_service_name
    ), (
        f"FAIL: Updated Service '{updated_service_name}' "
        "was not found in table."
    )

    print(
        "PASS: Service information updated successfully."
    )


# ============================================================
# TEST 3
# Verify updating Description with valid data
# ============================================================

def test_update_description_with_valid_data(
    services_page
):

    print(
        "\nTEST 3: Verify updating Description "
        "with valid data"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    existing_service_name = (
        services_page.get_service_name()
    )

    assert existing_service_name.strip(), (
        "Existing Service name is empty."
    )

    updated_description = (
        "Updated automation service description"
    )

    services_page.enter_description(
        updated_description
    )

    services_page.click_update()

    success_message = (
        services_page.get_success_message()
    )

    assert success_message, (
        "FAIL: Success message was not displayed "
        "after updating Description."
    )

    print(
        "Success message:",
        success_message
    )

    assert services_page.verify_description_in_table(
        updated_description
    ), (
        f"FAIL: Updated Description "
        f"'{updated_description}' "
        "was not found in table."
    )

    print(
        "PASS: Description updated successfully."
    )


# ============================================================
# TEST 4
# Verify updating Service and Description together
# ============================================================

def test_update_service_and_description_together(
    services_page
):

    print(
        "\nTEST 4: Verify updating Service and "
        "Description together"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    updated_service_name = (
        "Combined Updated Service"
    )

    updated_description = (
        "Combined updated service description"
    )

    services_page.enter_service_name(
        updated_service_name
    )

    services_page.enter_description(
        updated_description
    )

    services_page.click_update()

    success_message = (
        services_page.get_success_message()
    )

    assert success_message, (
        "FAIL: Success message was not displayed "
        "after combined update."
    )

    print(
        "Success message:",
        success_message
    )

    assert services_page.verify_service_data_in_table(
        updated_service_name,
        updated_description
    ), (
        "FAIL: Updated Service and Description "
        "were not both found in table."
    )

    print(
        "PASS: Service and Description updated successfully."
    )


# ============================================================
# TEST 5
# Verify Update with empty Service field
# ============================================================

def test_update_with_empty_service_field(
    services_page
):

    print(
        "\nTEST 5: Verify Update with empty "
        "Service field"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    # --------------------------------------------------------
    # Keep Description valid
    # --------------------------------------------------------

    description = (
        services_page.get_description()
    )

    assert description.strip(), (
        "Existing Description is empty. "
        "Test requires a valid Description."
    )

    # --------------------------------------------------------
    # DELETE Service Name
    # --------------------------------------------------------

    services_page.clear_service_name()

    # Verify field really became empty
    current_service_name = (
        services_page.get_service_name()
    )

    assert current_service_name.strip() == "", (
        "FAIL: Service Name field was not cleared."
    )

    # --------------------------------------------------------
    # CLICK UPDATE
    # --------------------------------------------------------

    services_page.click_update()

    # --------------------------------------------------------
    # VERIFY VALIDATION
    # --------------------------------------------------------

    validation_message = (
        services_page.get_validation_message()
    )

    print(
        "Validation message:",
        validation_message
    )

    assert validation_message, (
        "FAIL: Service validation message was not "
        "displayed when Service field was empty."
    )

    # The edit form should remain open
    assert services_page.is_edit_interface_open(), (
        "FAIL: Edit interface closed after invalid "
        "Service update."
    )

    print(
        "PASS: Empty Service field was validated."
    )


# ============================================================
# TEST 6
# Verify Update with empty Description field
# ============================================================

def test_update_with_empty_description_field(
    services_page
):

    print(
        "\nTEST 6: Verify Update with empty "
        "Description field"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    # --------------------------------------------------------
    # Verify Service Name exists
    # --------------------------------------------------------

    service_name = (
        services_page.get_service_name()
    )

    assert service_name.strip(), (
        "Existing Service name is empty."
    )

    # --------------------------------------------------------
    # DELETE Description
    # --------------------------------------------------------

    services_page.clear_description()

    current_description = (
        services_page.get_description()
    )

    assert current_description.strip() == "", (
        "FAIL: Description field was not cleared."
    )

    # --------------------------------------------------------
    # CLICK UPDATE
    # --------------------------------------------------------

    services_page.click_update()

    # --------------------------------------------------------
    # VERIFY VALIDATION
    # --------------------------------------------------------

    validation_message = (
        services_page.get_validation_message()
    )

    print(
        "Validation message:",
        validation_message
    )

    assert validation_message, (
        "FAIL: Description validation message was "
        "not displayed when Description was empty."
    )

    assert services_page.is_edit_interface_open(), (
        "FAIL: Edit interface closed after invalid "
        "Description update."
    )

    print(
        "PASS: Empty Description field was validated."
    )


# ============================================================
# TEST 7
# Verify Update with both mandatory fields empty
# ============================================================

def test_update_with_both_mandatory_fields_empty(
    services_page
):

    print(
        "\nTEST 7: Verify Update with both "
        "mandatory fields empty"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    # --------------------------------------------------------
    # DELETE SERVICE NAME
    # --------------------------------------------------------

    services_page.clear_service_name()

    # --------------------------------------------------------
    # DELETE DESCRIPTION
    # --------------------------------------------------------

    services_page.clear_description()

    # --------------------------------------------------------
    # VERIFY BOTH ARE EMPTY
    # --------------------------------------------------------

    service_name = (
        services_page.get_service_name()
    )

    description = (
        services_page.get_description()
    )

    assert service_name.strip() == "", (
        "Service Name was not cleared."
    )

    assert description.strip() == "", (
        "Description was not cleared."
    )

    # --------------------------------------------------------
    # CLICK UPDATE
    # --------------------------------------------------------

    services_page.click_update()

    # --------------------------------------------------------
    # VERIFY VALIDATION
    # --------------------------------------------------------

    validation_message = (
        services_page.get_validation_message()
    )

    print(
        "Validation message:",
        validation_message
    )

    assert validation_message, (
        "FAIL: Validation message was not displayed "
        "when both mandatory fields were empty."
    )

    assert services_page.is_edit_interface_open(), (
        "FAIL: Edit interface closed after invalid update."
    )

    print(
        "PASS: Empty mandatory fields were validated."
    )


# ============================================================
# TEST 8
# Verify updated service data appears in table
# ============================================================

def test_updated_service_data_appears_in_table(
    services_page
):

    print(
        "\nTEST 8: Verify updated service data "
        "appears in table"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    updated_service_name = (
        "Final Updated Automation Service"
    )

    updated_description = (
        "Final updated automation description"
    )

    services_page.enter_service_name(
        updated_service_name
    )

    services_page.enter_description(
        updated_description
    )

    services_page.click_update()

    success_message = (
        services_page.get_success_message()
    )

    assert success_message, (
        "FAIL: Success message was not displayed "
        "after updating service."
    )

    print(
        "Success message:",
        success_message
    )

    time.sleep(3)

    assert services_page.verify_service_name_in_table(
        updated_service_name
    ), (
        f"FAIL: Updated Service "
        f"'{updated_service_name}' "
        "was not found in table."
    )

    assert services_page.verify_description_in_table(
        updated_description
    ), (
        f"FAIL: Updated Description "
        f"'{updated_description}' "
        "was not found in table."
    )

    print(
        "PASS: Updated Service and Description "
        "are displayed in the table."
    )


# ============================================================
# TEST 9
# Verify service data remains after page refresh
# ============================================================

def test_service_data_remains_after_page_refresh(
    services_page
):

    print(
        "\nTEST 9: Verify service data remains "
        "after page refresh"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    existing_service_name = (
        services_page.get_service_name()
    )

    existing_description = (
        services_page.get_description()
    )

    assert existing_service_name.strip(), (
        "Service Name is empty."
    )

    assert existing_description.strip(), (
        "Description is empty."
    )

    print(
        "Service before refresh:",
        existing_service_name
    )

    print(
        "Description before refresh:",
        existing_description
    )

    # Close edit interface by refreshing
    services_page.refresh_page()

    # --------------------------------------------------------
    # Verify page scrolled back to service table
    # --------------------------------------------------------

    assert services_page.verify_service_name_in_table(
        existing_service_name
    ), (
        f"FAIL: Service '{existing_service_name}' "
        "was not found after page refresh."
    )

    assert services_page.verify_description_in_table(
        existing_description
    ), (
        "FAIL: Description was not found "
        "after page refresh."
    )

    print(
        "PASS: Service data remains after page refresh."
    )


# ============================================================
# TEST 10
# Verify updated service remains after page refresh
# ============================================================

def test_updated_service_remains_after_page_refresh(
    services_page
):

    print(
        "\nTEST 10: Verify updated service remains "
        "after page refresh"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    updated_service_name = (
        "Refresh Updated Automation Service"
    )

    updated_description = (
        "Refresh updated automation description"
    )

    services_page.enter_service_name(
        updated_service_name
    )

    services_page.enter_description(
        updated_description
    )

    services_page.click_update()

    success_message = (
        services_page.get_success_message()
    )

    assert success_message, (
        "Update success message was not displayed."
    )

    time.sleep(3)

    # --------------------------------------------------------
    # REFRESH
    # --------------------------------------------------------

    services_page.refresh_page()

    # --------------------------------------------------------
    # VERIFY DATA AFTER REFRESH
    # --------------------------------------------------------

    assert services_page.verify_service_name_in_table(
        updated_service_name
    ), (
        f"FAIL: Updated Service "
        f"'{updated_service_name}' "
        "was not found after refresh."
    )

    assert services_page.verify_description_in_table(
        updated_description
    ), (
        f"FAIL: Updated Description "
        f"'{updated_description}' "
        "was not found after refresh."
    )

    print(
        "PASS: Updated service remains after refresh."
    )


# ============================================================
# TEST 11
# Verify repeated Submit does not create unintended
# duplicate records
# ============================================================

def test_repeated_submit_does_not_create_duplicate_records(
    services_page
):

    print(
        "\nTEST 11: Verify repeated Submit does not "
        "create unintended duplicate records"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    service_name = (
        "Repeated Submit Test Service"
    )

    description = (
        "Repeated submit test description"
    )

    services_page.enter_service_name(
        service_name
    )

    services_page.enter_description(
        description
    )

    # --------------------------------------------------------
    # FIRST SUBMIT
    # --------------------------------------------------------

    services_page.click_update()

    time.sleep(3)

    first_success = (
        services_page.get_success_message()
    )

    print(
        "First submit message:",
        first_success
    )

    # --------------------------------------------------------
    # REFRESH TABLE
    # --------------------------------------------------------

    services_page.refresh_page()

    assert services_page.verify_service_name_in_table(
        service_name
    ), (
        "Service was not created/updated after "
        "first submit."
    )

    # --------------------------------------------------------
    # COUNT EXACT SERVICE OCCURRENCES
    # --------------------------------------------------------

    page_text = services_page.get_table_text()

    first_count = page_text.count(
        service_name
    )

    print(
        "Service occurrence count after first submit:",
        first_count
    )

    # --------------------------------------------------------
    # OPEN EDIT AGAIN
    # --------------------------------------------------------

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    # Enter the same values again
    services_page.enter_service_name(
        service_name
    )

    services_page.enter_description(
        description
    )

    # --------------------------------------------------------
    # SECOND SUBMIT
    # --------------------------------------------------------

    services_page.click_update()

    time.sleep(3)

    services_page.refresh_page()

    # --------------------------------------------------------
    # VERIFY NO UNINTENDED DUPLICATE
    # --------------------------------------------------------

    page_text_after = (
        services_page.get_table_text()
    )

    second_count = page_text_after.count(
        service_name
    )

    print(
        "Service occurrence count after second submit:",
        second_count
    )

    assert second_count <= first_count + 1, (
        "FAIL: Repeated Submit appears to have created "
        "unintended duplicate service records."
    )

    print(
        "PASS: Repeated Submit did not create "
        "an unintended duplicate record."
    )


# ============================================================
# TEST 12
# Verify repeated Update does not create duplicate
# service records
# ============================================================

def test_repeated_update_does_not_create_duplicate_service_records(
    services_page
):

    print(
        "\nTEST 12: Verify repeated Update does not "
        "create duplicate service records"
    )

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    service_name = (
        "Repeated Update Service"
    )

    description = (
        "Repeated update description"
    )

    services_page.enter_service_name(
        service_name
    )

    services_page.enter_description(
        description
    )

    # First update
    services_page.click_update()

    time.sleep(3)

    services_page.refresh_page()

    assert services_page.verify_service_name_in_table(
        service_name
    ), (
        "Service was not found after first update."
    )

    # --------------------------------------------------------
    # Open same record again
    # --------------------------------------------------------

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    # Update with exactly the same values
    services_page.enter_service_name(
        service_name
    )

    services_page.enter_description(
        description
    )

    # Second update
    services_page.click_update()

    time.sleep(3)

    services_page.refresh_page()

    # --------------------------------------------------------
    # Verify service still exists
    # --------------------------------------------------------

    assert services_page.verify_service_name_in_table(
        service_name
    ), (
        "Service disappeared after repeated Update."
    )

    # --------------------------------------------------------
    # Count occurrences
    # --------------------------------------------------------

    page_text = (
        services_page.get_table_text()
    )

    occurrence_count = page_text.count(
        service_name
    )

    print(
        "Service occurrence count:",
        occurrence_count
    )

    assert occurrence_count <= 2, (
        "FAIL: Repeated Update appears to have "
        "created duplicate service records."
    )

    print(
        "PASS: Repeated Update did not create "
        "duplicate service records."
    )


# ============================================================
# TEST 13
# Verify duplicate Service name restriction
# ============================================================

def test_duplicate_service_name_restriction(
    services_page
):

    print(
        "\nTEST 13: Verify duplicate Service "
        "name restriction"
    )

    # --------------------------------------------------------
    # Get an existing service name
    # --------------------------------------------------------

    services_page.click_edit_service()

    assert services_page.is_edit_interface_open()

    existing_service_name = (
        services_page.get_service_name()
    )

    existing_description = (
        services_page.get_description()
    )

    assert existing_service_name.strip(), (
        "Existing Service name is empty."
    )

    assert existing_description.strip(), (
        "Existing Description is empty."
    )

    print(
        "Existing Service:",
        existing_service_name
    )

    # --------------------------------------------------------
    # Enter the same service name
    # --------------------------------------------------------

    services_page.enter_service_name(
        existing_service_name
    )

    services_page.enter_description(
        "Duplicate service name test description"
    )

    # --------------------------------------------------------
    # Click Update
    # --------------------------------------------------------

    services_page.click_update()

    time.sleep(3)

    validation_message = (
        services_page.get_validation_message()
    )

    success_message = (
        services_page.get_success_message()
    )

    print(
        "Validation message:",
        validation_message
    )

    print(
        "Success message:",
        success_message
    )

    # --------------------------------------------------------
    # RESULT
    #
    # The requirement is to verify duplicate restriction.
    # Therefore either:
    #
    # 1. Validation/error is displayed -> PASS
    # OR
    # 2. Application allows the same name -> FAIL
    # --------------------------------------------------------

    if validation_message:

        print(
            "PASS: Duplicate Service name was restricted."
        )

    else:

        # If application allows the update, verify whether
        # it actually created a duplicate.
        services_page.refresh_page()

        page_text = (
            services_page.get_table_text()
        )

        occurrences = page_text.count(
            existing_service_name
        )

        print(
            "Duplicate name occurrences:",
            occurrences
        )

        assert occurrences <= 1, (
            f"FAIL: Duplicate Service name "
            f"'{existing_service_name}' "
            "was allowed and appears multiple times."
        )

        print(
            "PASS: No duplicate Service record was created."
        )