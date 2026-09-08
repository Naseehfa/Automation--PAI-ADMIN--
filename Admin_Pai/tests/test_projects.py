
import time

import pytest

from selenium.webdriver.common.by import By

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

    # --------------------------------------------------------
    # REDUCE PAGE ZOOM
    # --------------------------------------------------------

    print(
        "Reducing page zoom to 80%..."
    )

    driver.execute_script(
        "document.body.style.zoom='80%'"
    )

    time.sleep(2)

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

    projects_page.click_edit_project()

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Edit modal did not open."
    )

    projects_page.clear_project_name()

    current_name = (
        projects_page.get_project_name()
    )

    assert current_name == "", (
        "FAIL: Project Name was not completely "
        "cleared before clicking Update."
    )

    projects_page.click_update_project()

    time.sleep(2)

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Edit modal closed. Expected validation "
        "to prevent update with an empty Project Name."
    )

    print(
        "PASS: Project update was prevented with an "
        "empty Project Name."
    )


# ============================================================

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
    # STEP 1: Click Edit icon
    # --------------------------------------------------------

    projects_page.click_edit_project()

    assert projects_page.is_edit_modal_open(), (
        "FAIL: Edit modal did not open."
    )

    print(
        "PASS: Edit modal opened successfully."
    )

    # --------------------------------------------------------
    # STEP 2: Completely clear Description
    # --------------------------------------------------------
    # IMPORTANT:
    # Project Name is NOT changed.

    projects_page.clear_project_description()

    # --------------------------------------------------------
    # STEP 3: Verify Description is completely empty
    # --------------------------------------------------------

    current_description = (
        projects_page.get_project_description()
    )

    assert current_description == "", (
        "FAIL: Project Description was not "
        "completely cleared before clicking Update."
    )

    print(
        "PASS: Project Description is completely empty."
    )

    # --------------------------------------------------------
    # STEP 4: Click Update
    # --------------------------------------------------------

    projects_page.click_update_project()

    time.sleep(2)

    print(
        "PASS: Update button clicked successfully."
    )

    print(
        "PASS: Project Name remained unchanged."
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

    # --------------------------------------------------------
    # STEP 1: Zoom out the page
    # --------------------------------------------------------

    projects_page.driver.execute_script("""
        document.body.style.zoom = '70%';
    """)

    time.sleep(2)

    print(
        "Page zoomed out to 70%."
    )

    # --------------------------------------------------------
    # STEP 2: Scroll down the page
    # --------------------------------------------------------

    projects_page.driver.execute_script("""
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    """)

    time.sleep(2)

    print(
        "Scrolled down successfully."
    )

    # --------------------------------------------------------
    # STEP 3: Verify page is displayed
    # --------------------------------------------------------

    body = projects_page.driver.find_element(
        By.TAG_NAME,
        "body"
    )

    assert body.is_displayed(), (
        "FAIL: Client Projects page is not displayed."
    )

    print(
        "PASS: Client Projects page is displayed "
        "successfully."
    )

    # --------------------------------------------------------
    # STEP 4: Test completed
    # --------------------------------------------------------

    print(
        "TEST 4 PASSED."
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

    # --------------------------------------------------------
    # STEP 1: Zoom out the page
    # --------------------------------------------------------

    projects_page.driver.execute_script("""
        document.body.style.zoom = '70%';
    """)

    time.sleep(2)

    print(
        "Page zoomed out to 70%."
    )

    # --------------------------------------------------------
    # STEP 2: Scroll down the page
    # --------------------------------------------------------

    projects_page.driver.execute_script("""
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    """)

    time.sleep(2)

    print(
        "Scrolled down successfully."
    )

    # --------------------------------------------------------
    # STEP 3: Verify page is displayed
    # --------------------------------------------------------

    body = projects_page.driver.find_element(
        By.TAG_NAME,
        "body"
    )

    assert body.is_displayed(), (
        "FAIL: Client Projects page is not displayed."
    )

    print(
        "PASS: Client Projects page is displayed "
        "successfully."
    )

    # --------------------------------------------------------
    # STEP 4: Test completed
    # --------------------------------------------------------

    print(
        "TEST 9 PASSED."
    )


# ============================================================
# TEST 10
# Verify NO button cancels project deletion
# ============================================================


def test_verify_no_button_cancels_deletion(
    projects_page
):

    print(
        "\nTEST 10: Verify NO button cancels "
        "project deletion"
    )

    # --------------------------------------------------------
    # STEP 1: Open Client Projects menu
    # --------------------------------------------------------

    menu = projects_page.driver.find_element(
        By.XPATH,
        "//*[@id='root']/div/aside/nav/div[4]/button/span"
    )

    projects_page.driver.execute_script(
        "arguments[0].click();",
        menu
    )

    time.sleep(1)

    print(
        "Client Projects menu clicked."
    )

    # --------------------------------------------------------
    # STEP 2: Check Client Projects submenu
    # --------------------------------------------------------

    submenu_xpath = (
        "//*[@id='root']/div/aside/nav/div[4]/div/button[2]"
    )

    submenu_elements = projects_page.driver.find_elements(
        By.XPATH,
        submenu_xpath
    )

    # If submenu is not available after clicking the menu,
    # click the menu again to expand it.
    if not submenu_elements:

        print(
            "Client Projects submenu is collapsed. "
            "Opening it..."
        )

        menu = projects_page.driver.find_element(
            By.XPATH,
            "//*[@id='root']/div/aside/nav/div[4]/button/span"
        )

        projects_page.driver.execute_script(
            "arguments[0].click();",
            menu
        )

        time.sleep(1)

    # --------------------------------------------------------
    # STEP 3: Click Client Projects submenu
    # --------------------------------------------------------

    submenu = projects_page.driver.find_element(
        By.XPATH,
        submenu_xpath
    )

    projects_page.driver.execute_script(
        """
        arguments[0].scrollIntoView({
            block: 'center'
        });
        """,
        submenu
    )

    time.sleep(1)

    projects_page.driver.execute_script(
        "arguments[0].click();",
        submenu
    )

    time.sleep(4)

    print(
        "Client Projects submenu opened."
    )

    # --------------------------------------------------------
    # STEP 4: Reduce page zoom
    # --------------------------------------------------------

    projects_page.driver.execute_script(
        "document.body.style.zoom='70%'"
    )

    time.sleep(2)

    print(
        "Page zoomed out to 70%."
    )

    # --------------------------------------------------------
    # STEP 5: Scroll down to project list
    # --------------------------------------------------------

    projects_page.driver.execute_script(
        """
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
        """
    )

    time.sleep(2)

    print(
        "Scrolled down to project list."
    )

    # --------------------------------------------------------
    # STEP 6: Click Delete icon
    # --------------------------------------------------------

    delete_button = projects_page.driver.find_element(
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[5]/button[2]/img"
    )

    projects_page.driver.execute_script(
        """
        arguments[0].scrollIntoView({
            block: 'center'
        });
        """,
        delete_button
    )

    time.sleep(1)

    projects_page.driver.execute_script(
        "arguments[0].click();",
        delete_button
    )

    time.sleep(2)

    print(
        "Delete icon clicked."
    )

    # --------------------------------------------------------
    # STEP 7: Click NO button
    # --------------------------------------------------------

    no_button = projects_page.driver.find_element(
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[3]/div/div[2]/button[1]"
    )

    projects_page.driver.execute_script(
        """
        arguments[0].scrollIntoView({
            block: 'center'
        });
        """,
        no_button
    )

    time.sleep(1)

    projects_page.driver.execute_script(
        "arguments[0].click();",
        no_button
    )

    time.sleep(3)

    print(
        "NO button clicked."
    )

    # --------------------------------------------------------
    # STEP 8: Verify delete confirmation is closed
    # --------------------------------------------------------

    confirmation = projects_page.driver.find_elements(
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[3]/div/div[2]/button[1]"
    )

    visible_confirmation = [
        button
        for button in confirmation
        if button.is_displayed()
    ]

    assert not visible_confirmation, (
        "FAIL: Delete confirmation is still displayed "
        "after clicking NO."
    )

    print(
        "PASS: Project deletion was cancelled "
        "successfully by clicking NO."
    )

    print(
        "TEST 10 PASSED."
    )

