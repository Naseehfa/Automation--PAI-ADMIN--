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
from pages.clients_projects_page import ClientsProjectsPage

from selenium.webdriver.support.ui import WebDriverWait


# ============================================================
# URL
# ============================================================

CLIENTS_PROJECTS_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/clients-projects"
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
# VALID PROJECT CATEGORIES
# ============================================================

WEB_CATEGORY = "Web Solution"

MOBILE_CATEGORY = "Mobile Solution"

UIUX_CATEGORY = "UI/UX Design"


# ============================================================
# DEFAULT VALID CATEGORY
# ============================================================

VALID_CATEGORY = WEB_CATEGORY


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
# GENERATE PROJECT DATA
# ============================================================

def generate_project_data():

    random_text = generate_random_text()

    project_name = (
        f"Automation Client Project {random_text}"
    )

    description = (
        f"Professional client project created "
        f"for software testing and automation "
        f"purposes {random_text}"
    )

    return (
        project_name,
        description
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
# OPEN CLIENT PROJECTS
# ============================================================

def open_clients_projects():

    driver, wait = (
        open_admin_page()
    )

    clients_projects = (
        ClientsProjectsPage(
            driver
        )
    )

    clients_projects.navigate_to_clients_projects()

    wait.until(
        lambda d:
        "/admin/clients-projects"
        in d.current_url
    )

    assert (
        "/admin/clients-projects"
        in driver.current_url
    )

    time.sleep(2)

    return (
        driver,
        clients_projects,
        wait
    )


# ============================================================
# 01 - NAVIGATION
# ============================================================

def test_clients_projects_navigation():

    driver, wait = (
        open_admin_page()
    )

    try:

        print(
            "\n========== "
            "CLIENT PROJECT NAVIGATION "
            "=========="
        )

        clients_projects = (
            ClientsProjectsPage(
                driver
            )
        )

        clients_projects.navigate_to_clients_projects()

        wait.until(
            lambda d:
            "/admin/clients-projects"
            in d.current_url
        )

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        )

        print(
            "NAVIGATION PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 02 - POSITIVE VALID PROJECT
# ============================================================

def test_add_clients_project_valid_data():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "P01 VALID PROJECT "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.add_project(
            project_name=project_name,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH,
            url="https://www.google.com",
            description=description
        )

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        )

        print(
            "Project Name:",
            project_name
        )

        print(
            "Category:",
            VALID_CATEGORY
        )

        print(
            "P01 VALID PROJECT PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 03 - POSITIVE MOBILE CATEGORY
# ============================================================

def test_add_clients_project_mobile_solution():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "P02 MOBILE SOLUTION "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.add_project(
            project_name=project_name,
            category=MOBILE_CATEGORY,
            image_path=IMAGE_PATH,
            url="https://www.google.com",
            description=description
        )

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        )

        print(
            "P02 MOBILE SOLUTION PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 04 - POSITIVE UI/UX CATEGORY
# ============================================================

def test_add_clients_project_uiux():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "P03 UI/UX DESIGN "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.add_project(
            project_name=project_name,
            category=UIUX_CATEGORY,
            image_path=IMAGE_PATH,
            url="https://www.google.com",
            description=description
        )

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        )

        print(
            "P03 UI/UX DESIGN PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 05 - POSITIVE MULTI WORD PROJECT
# ============================================================

def test_add_clients_project_multiple_words():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "P04 MULTI WORD PROJECT "
            "=========="
        )

        random_text = (
            generate_random_text()
        )

        project_name = (
            f"E Commerce Website "
            f"Development {random_text}"
        )

        description = (
            f"E commerce client project "
            f"for automation testing "
            f"{random_text}"
        )

        clients_projects.add_project(
            project_name=project_name,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH,
            url="https://www.google.com",
            description=description
        )

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        )

        print(
            "P04 MULTI WORD PROJECT PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 06 - POSITIVE VALID URL
# ============================================================

def test_add_clients_project_valid_url():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "P05 VALID URL "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.add_project(
            project_name=project_name,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH,
            url=(
                "https://www.linkedin.com/"
                "company/example"
            ),
            description=description
        )

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        )

        print(
            "P05 VALID URL PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 07 - POSITIVE LONG DESCRIPTION
# ============================================================

def test_add_clients_project_long_valid_description():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "P06 LONG VALID DESCRIPTION "
            "=========="
        )

        project_name = (
            f"Long Description Project "
            f"{generate_random_text()}"
        )

        description = (
            "This is a valid client project "
            "description for automation testing "
            * 20
        )

        clients_projects.add_project(
            project_name=project_name,
            category=VALID_CATEGORY,
            image_path=IMAGE_PATH,
            url="https://www.google.com",
            description=description
        )

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        )

        print(
            "P06 LONG DESCRIPTION PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 08 - NEGATIVE ALL EMPTY
# ============================================================

def test_add_clients_project_all_empty():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N01 ALL EMPTY "
            "=========="
        )

        clients_projects.enter_project_name(
            ""
        )

        clients_projects.enter_project_url(
            ""
        )

        clients_projects.enter_description(
            ""
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N01 ALL EMPTY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 09 - NEGATIVE EMPTY NAME
# ============================================================

def test_add_clients_project_empty_name():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N02 EMPTY NAME "
            "=========="
        )

        clients_projects.enter_project_name(
            ""
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            "Valid project description"
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N02 EMPTY NAME PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 10 - NEGATIVE EMPTY CATEGORY
# ============================================================

def test_add_clients_project_empty_category():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N03 EMPTY CATEGORY "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            description
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N03 EMPTY CATEGORY PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 11 - NEGATIVE EMPTY IMAGE
# ============================================================

def test_add_clients_project_empty_image():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N04 EMPTY IMAGE "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            description
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N04 EMPTY IMAGE PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 12 - NEGATIVE EMPTY URL
# ============================================================

def test_add_clients_project_empty_url():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N05 EMPTY URL "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            ""
        )

        clients_projects.enter_description(
            description
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N05 EMPTY URL PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 13 - NEGATIVE EMPTY DESCRIPTION
# ============================================================

def test_add_clients_project_empty_description():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N06 EMPTY DESCRIPTION "
            "=========="
        )

        project_name, _ = (
            generate_project_data()
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            ""
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N06 EMPTY DESCRIPTION PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 14 - NEGATIVE SPACES NAME
# ============================================================

def test_add_clients_project_spaces_name():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N07 SPACES NAME "
            "=========="
        )

        clients_projects.enter_project_name(
            "     "
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            "Valid description"
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N07 SPACES NAME PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 15 - NEGATIVE SPACES DESCRIPTION
# ============================================================

def test_add_clients_project_spaces_description():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N08 SPACES DESCRIPTION "
            "=========="
        )

        project_name, _ = (
            generate_project_data()
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            "     "
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N08 SPACES DESCRIPTION PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 16 - NEGATIVE NUMERIC NAME
# ============================================================

def test_add_clients_project_numeric_name():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N09 NUMERIC NAME "
            "=========="
        )

        clients_projects.enter_project_name(
            "123456789"
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            "Valid description"
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N09 NUMERIC NAME PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 17 - NEGATIVE SPECIAL CHARACTERS
# ============================================================

def test_add_clients_project_special_characters():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N10 SPECIAL CHARACTERS "
            "=========="
        )

        clients_projects.enter_project_name(
            "@#$%^&*"
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            "Valid description"
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N10 SPECIAL CHARACTERS PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 18 - NEGATIVE INVALID URL
# ============================================================

def test_add_clients_project_invalid_url():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N11 INVALID URL "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "invalid-url"
        )

        clients_projects.enter_description(
            description
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N11 INVALID URL PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 19 - NEGATIVE URL WITHOUT PROTOCOL
# ============================================================

def test_add_clients_project_url_without_protocol():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N12 URL WITHOUT PROTOCOL "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "www.google.com"
        )

        clients_projects.enter_description(
            description
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N12 URL WITHOUT PROTOCOL PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 20 - NEGATIVE HTML / XSS INPUT
# ============================================================

def test_add_clients_project_html_input():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N13 HTML INPUT "
            "=========="
        )

        clients_projects.enter_project_name(
            "<script>alert('XSS')</script>"
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            "Valid description"
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N13 HTML INPUT PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 21 - NEGATIVE LONG NAME
# ============================================================

def test_add_clients_project_long_name():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N14 LONG NAME "
            "=========="
        )

        long_name = (
            "Client Project "
            + "A" * 300
        )

        clients_projects.enter_project_name(
            long_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            "Valid description"
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N14 LONG NAME PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 22 - NEGATIVE LONG DESCRIPTION
# ============================================================

def test_add_clients_project_long_description():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N15 LONG DESCRIPTION "
            "=========="
        )

        project_name, _ = (
            generate_project_data()
        )

        long_description = (
            "A" * 2000
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google.com"
        )

        clients_projects.enter_description(
            long_description
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N15 LONG DESCRIPTION PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 23 - NEGATIVE URL WITH SPACES
# ============================================================

def test_add_clients_project_url_with_spaces():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N16 URL WITH SPACES "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://www.google .com"
        )

        clients_projects.enter_description(
            description
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N16 URL WITH SPACES PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 24 - NEGATIVE SPECIAL URL
# ============================================================

def test_add_clients_project_special_url():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "N17 SPECIAL URL "
            "=========="
        )

        project_name, description = (
            generate_project_data()
        )

        clients_projects.enter_project_name(
            project_name
        )

        clients_projects.select_project_category(
            VALID_CATEGORY
        )

        clients_projects.upload_project_image(
            IMAGE_PATH
        )

        clients_projects.enter_project_url(
            "https://@@@@"
        )

        clients_projects.enter_description(
            description
        )

        clients_projects.click_submit()

        time.sleep(2)

        assert (
            clients_projects.is_form_displayed()
        )

        print(
            "N17 SPECIAL URL PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 25 - EDIT PROJECT
# ============================================================

def test_edit_clients_project():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "P25 EDIT CLIENT PROJECT "
            "=========="
        )

        random_text = (
            generate_random_text()
        )

        updated_project_name = (
            f"Updated Client Project "
            f"{random_text}"
        )

        print(
            "New Project Name:",
            updated_project_name
        )

        clients_projects.edit_project(
            updated_project_name
        )

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        )

        print(
            "Updated Project Name:",
            updated_project_name
        )

        print(
            "P25 EDIT CLIENT PROJECT PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()


# ============================================================
# 26 - DELETE PROJECT
# ============================================================

def test_delete_clients_project():

    driver, clients_projects, wait = (
        open_clients_projects()
    )

    try:

        print(
            "\n========== "
            "P26 DELETE CLIENT PROJECT "
            "=========="
        )

        # --------------------------------------------------------
        # STEP 1 - Verify we are on Clients Projects page
        # --------------------------------------------------------

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        ), (
            "User is not on Clients Projects page "
            "before deleting."
        )

        print(
            "Clients Projects page opened successfully."
        )

        # --------------------------------------------------------
        # STEP 2 - Click Delete button
        # --------------------------------------------------------

        clients_projects.click_delete_project()

        print(
            "Delete button clicked successfully."
        )

        # --------------------------------------------------------
        # STEP 3 - Verify confirmation modal
        # --------------------------------------------------------

        assert (
            clients_projects.is_delete_confirmation_displayed()
        ), (
            "Delete confirmation modal "
            "was not displayed."
        )

        print(
            "Delete confirmation modal displayed."
        )

        # --------------------------------------------------------
        # STEP 4 - Confirm deletion
        # --------------------------------------------------------

        clients_projects.confirm_delete_project()

        print(
            "Delete confirmation completed."
        )

        # --------------------------------------------------------
        # STEP 5 - Verify URL
        # --------------------------------------------------------

        wait.until(
            lambda d:
            "/admin/clients-projects"
            in d.current_url
        )

        assert (
            driver.current_url
            == CLIENTS_PROJECTS_URL
        ), (
            "User is not on Clients Projects page "
            "after deleting the project."
        )

        # --------------------------------------------------------
        # STEP 6 - Final result
        # --------------------------------------------------------

        print(
            "P26 DELETE CLIENT PROJECT PASSED"
        )

    finally:

        time.sleep(2)

        driver.quit()