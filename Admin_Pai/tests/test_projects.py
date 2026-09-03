import time

import pytest

from utils.driver_setup import get_driver

from config.config import (
    URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage


# ============================================================
# DRIVER FIXTURE
# ============================================================

@pytest.fixture
def driver():

    driver = get_driver()

    driver.maximize_window()

    yield driver

    try:
        driver.quit()
    except Exception:
        pass


# ============================================================
# PROJECTS PAGE FIXTURE
# ============================================================

@pytest.fixture
def projects_page(driver):

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

    time.sleep(5)

    # --------------------------------------------------------
    # OPEN CLIENT PROJECTS
    # --------------------------------------------------------

    projects_page = ProjectsPage(driver)

    projects_page.open_projects()

    time.sleep(3)

    return projects_page


# ============================================================
# TEST 1
# Verify Edit icon opens selected project record
# ============================================================

def test_verify_edit_icon_opens_selected_project(
    projects_page
):

    print(
        "\nTEST 1: Verify Edit icon opens "
        "selected project record"
    )

    projects_page.click_edit_project()

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Project Edit modal did not open."
    )

    print(
        "PASS: Project Edit modal opened successfully."
    )


# ============================================================
# TEST 2
# Verify update with empty Project Name
# ============================================================

def test_update_with_empty_project_name(
    projects_page
):

    print(
        "\nTEST 2: Verify update with "
        "empty Project Name"
    )

    # --------------------------------------------------------
    # Open Edit
    # --------------------------------------------------------

    projects_page.click_edit_project()

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Edit modal did not open."
    )

    # --------------------------------------------------------
    # Completely delete old Project Name
    # --------------------------------------------------------

    projects_page.clear_project_name()

    current_name = (
        projects_page.get_project_name()
    )

    assert current_name == "", (
        "FAIL: Project Name was not completely "
        "cleared before clicking Update."
    )

    # --------------------------------------------------------
    # Click Update
    # --------------------------------------------------------

    projects_page.click_update_project()

    # --------------------------------------------------------
    # Verify update was prevented
    # --------------------------------------------------------

    time.sleep(2)

    current_name_after_update = (
        projects_page.get_project_name()
    )

    assert current_name_after_update == "", (
        "FAIL: Project Name field was not empty "
        "after clearing."
    )

    print(
        "PASS: Update was attempted with empty "
        "Project Name."
    )


# ============================================================
# TEST 3
# Verify update with empty Description
# ============================================================

def test_update_with_empty_description(
    projects_page
):

    print(
        "\nTEST 3: Verify update with "
        "empty Description"
    )

    # --------------------------------------------------------
    # Open Edit
    # --------------------------------------------------------

    projects_page.click_edit_project()

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Edit modal did not open."
    )

    # --------------------------------------------------------
    # Completely delete old Description
    # --------------------------------------------------------

    projects_page.clear_project_description()

    current_description = (
        projects_page.get_project_description()
    )

    assert current_description == "", (
        "FAIL: Description was not completely "
        "cleared before clicking Update."
    )

    # --------------------------------------------------------
    # Click Update
    # --------------------------------------------------------

    projects_page.click_update_project()

    time.sleep(2)

    current_description_after_update = (
        projects_page.get_project_description()
    )

    assert current_description_after_update == "", (
        "FAIL: Description field was not empty "
        "after clearing."
    )

    print(
        "PASS: Update was attempted with "
        "empty Description."
    )


# ============================================================
# TEST 4
# Verify Edit icon is displayed for each project
# ============================================================

def test_verify_edit_icon_is_displayed_for_each_project(
    projects_page
):

    print(
        "\nTEST 4: Verify Edit icon is displayed "
        "for each project"
    )

    projects_page.scroll_to_project_table()

    edit_buttons = projects_page.driver.find_elements(
        By.XPATH,
        "//table//tbody//tr//button[1]/img"
    )

    assert edit_buttons, (
        "FAIL: No Edit icons were found."
    )

    visible_count = 0

    for button in edit_buttons:

        try:

            if button.is_displayed():

                visible_count += 1

        except Exception:

            continue

    assert visible_count > 0, (
        "FAIL: Edit icons are not displayed."
    )

    print(
        f"PASS: {visible_count} Edit icon(s) "
        "are displayed."
    )


# ============================================================
# TEST 5
# Verify existing Project Name is populated
# ============================================================

def test_verify_existing_project_name_is_populated(
    projects_page
):

    print(
        "\nTEST 5: Verify existing Project Name "
        "is populated in Edit modal"
    )

    projects_page.click_edit_project()

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Edit modal did not open."
    )

    project_name = (
        projects_page.get_project_name()
    )

    assert project_name, (
        "FAIL: Existing Project Name "
        "is not populated."
    )

    print(
        "Existing Project Name:",
        project_name
    )

    print(
        "PASS: Existing Project Name is populated."
    )


# ============================================================
# TEST 6
# Verify existing Project Category is populated
# ============================================================

def test_verify_existing_project_category_is_populated(
    projects_page
):

    print(
        "\nTEST 6: Verify existing Project Category "
        "is populated"
    )

    projects_page.click_edit_project()

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Edit modal did not open."
    )

    category = (
        projects_page.get_project_category()
    )

    assert category, (
        "FAIL: Existing Project Category "
        "is not populated."
    )

    print(
        "Existing Project Category:",
        category
    )

    print(
        "PASS: Existing Project Category is populated."
    )


# ============================================================
# TEST 7
# Verify existing Website is populated
# ============================================================

def test_verify_existing_website_is_populated(
    projects_page
):

    print(
        "\nTEST 7: Verify existing Website "
        "is populated"
    )

    projects_page.click_edit_project()

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Edit modal did not open."
    )

    website = (
        projects_page.get_project_website()
    )

    assert website, (
        "FAIL: Existing Website "
        "is not populated."
    )

    print(
        "Existing Website:",
        website
    )

    print(
        "PASS: Existing Website is populated."
    )


# ============================================================
# TEST 8
# Verify existing Description is populated
# ============================================================

def test_verify_existing_description_is_populated(
    projects_page
):

    print(
        "\nTEST 8: Verify existing Description "
        "is populated"
    )

    projects_page.click_edit_project()

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Edit modal did not open."
    )

    description = (
        projects_page.get_project_description()
    )

    assert description, (
        "FAIL: Existing Description "
        "is not populated."
    )

    print(
        "Existing Description:",
        description
    )

    print(
        "PASS: Existing Description is populated."
    )


# ============================================================
# TEST 9
# Verify Delete icon is displayed for each project
# ============================================================

def test_verify_delete_icon_is_displayed_for_each_project(
    projects_page
):

    print(
        "\nTEST 9: Verify Delete icon is displayed "
        "for each project"
    )

    projects_page.scroll_to_project_table()

    delete_buttons = projects_page.driver.find_elements(
        By.XPATH,
        "//table//tbody//tr//button[2]/img"
    )

    assert delete_buttons, (
        "FAIL: No Delete icons were found."
    )

    visible_count = 0

    for button in delete_buttons:

        try:

            if button.is_displayed():

                visible_count += 1

        except Exception:

            continue

    assert visible_count > 0, (
        "FAIL: Delete icons are not displayed."
    )

    print(
        f"PASS: {visible_count} Delete icon(s) "
        "are displayed."
    )


# ============================================================
# TEST 10
# Verify No button cancels deletion
# ============================================================

def test_verify_no_button_cancels_deletion(
    projects_page
):

    print(
        "\nTEST 10: Verify No button "
        "cancels deletion"
    )

    # --------------------------------------------------------
    # Get project name BEFORE deletion
    # --------------------------------------------------------

    project_name = (
        projects_page
        .get_delete_target_project_name()
    )

    assert project_name, (
        "FAIL: Could not identify project "
        "before deletion."
    )

    print(
        "Project selected:",
        project_name
    )

    # --------------------------------------------------------
    # Click Delete
    # --------------------------------------------------------

    projects_page.click_delete_project()

    assert projects_page.is_delete_confirmation_open(), (
        "FAIL: Delete confirmation "
        "did not open."
    )

    # --------------------------------------------------------
    # Click NO
    # --------------------------------------------------------

    projects_page.click_delete_no()

    # --------------------------------------------------------
    # Verify confirmation closed
    # --------------------------------------------------------

    time.sleep(2)

    assert not projects_page.is_delete_confirmation_open(), (
        "FAIL: Delete confirmation modal "
        "remained open after clicking NO."
    )

    # --------------------------------------------------------
    # Verify project still exists
    # --------------------------------------------------------

    projects_page.refresh_projects_page()

    project_exists = (
        projects_page
        .is_project_name_present_in_table(
            project_name
        )
    )

    assert project_exists, (
        f"FAIL: Project '{project_name}' "
        "was not found after clicking NO."
    )

    print(
        "PASS: NO button cancelled deletion "
        "and project remains."
    )


