import os
import time
import random
import string

from utils.driver_setup import get_driver

from config.config import (
    URL,
    VALID_USERNAME,
    VALID_PASSWORD
)

from pages.login_page import LoginPage
from pages.company_projects_page import CompanyProjectsPage

from selenium.webdriver.support.ui import WebDriverWait


# ============================================================
# URL
# ============================================================

COMPANY_PROJECTS_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/company-projects"
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
# GENERATE RANDOM TEXT
# ============================================================

def generate_random_text(length=8):

    letters = string.ascii_letters

    return "".join(
        random.choice(letters)
        for _ in range(length)
    )


# ============================================================
# GENERATE RANDOM PROJECT DATA
# ============================================================

def generate_project_data():

    random_text = generate_random_text()

    project_name = (
        f"Automation Project {random_text}"
    )

    caption = (
        f"Project Caption {random_text}"
    )

    description = (
        f"Professional company project created "
        f"for software testing and automation "
        f"purposes {random_text}."
    )

    return (
        project_name,
        caption,
        description
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
        "login" not in d.current_url
    )

    time.sleep(3)

    print(
        "Login completed."
    )

    print(
        "Current URL:",
        driver.current_url
    )

    return driver, wait


# ============================================================
# HELPER - OPEN COMPANY PROJECTS
# ============================================================

def open_company_projects():

    driver, wait = open_admin_page()

    company_projects = CompanyProjectsPage(
        driver
    )

    company_projects.navigate_to_company_projects()

    wait.until(
        lambda d:
        "company-projects"
        in d.current_url
    )

    assert (
        "company-projects"
        in driver.current_url
    )

    time.sleep(3)

    return (
        driver,
        company_projects,
        wait
    )


# ============================================================
# 1. NAVIGATION
# ============================================================

def test_company_projects_navigation():

    driver, wait = open_admin_page()

    try:

        print(
            "\n========== COMPANY PROJECTS NAVIGATION =========="
        )

        company_projects = CompanyProjectsPage(
            driver
        )

        company_projects.navigate_to_company_projects()

        wait.until(
            lambda d:
            "company-projects"
            in d.current_url
        )

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "COMPANY PROJECTS NAVIGATION PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 2. POSITIVE - VALID REQUIRED DATA
# ============================================================

def test_add_company_project_valid_data():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== P01 VALID PROJECT =========="
        )

        (
            project_name,
            caption,
            description
        ) = generate_project_data()

        print(
            "Project Name:",
            project_name
        )

        print(
            "Caption:",
            caption
        )

        company_projects.add_project(
            project_name=project_name,
            caption=caption,
            image_path=IMAGE_PATH,
            description=description
        )

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "P01 VALID PROJECT PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 3. POSITIVE - VALID URLS
# ============================================================

def test_add_company_project_valid_urls():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== P02 VALID URLS =========="
        )

        (
            project_name,
            caption,
            description
        ) = generate_project_data()

        valid_url_1 = (
            "https://www.google.com"
        )

        valid_url_2 = (
            "https://www.linkedin.com"
        )

        print(
            "Project Name:",
            project_name
        )

        print(
            "Valid URL 1:",
            valid_url_1
        )

        print(
            "Valid URL 2:",
            valid_url_2
        )

        company_projects.add_project_with_urls(
            project_name=project_name,
            caption=caption,
            image_path=IMAGE_PATH,
            url_1=valid_url_1,
            url_2=valid_url_2,
            description=description
        )

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "P02 VALID URLS PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 4. POSITIVE - MULTI WORD PROJECT NAME
# ============================================================

def test_add_company_project_multiple_words():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== P03 MULTI WORD PROJECT =========="
        )

        random_text = generate_random_text()

        project_name = (
            f"Mobile Application Development {random_text}"
        )

        caption = (
            f"Mobile Application Project {random_text}"
        )

        description = (
            f"Android and iOS mobile application "
            f"development project {random_text}."
        )

        company_projects.add_project(
            project_name=project_name,
            caption=caption,
            image_path=IMAGE_PATH,
            description=description
        )

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "P03 MULTI WORD PROJECT PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 5. POSITIVE - MIXED CASE
# ============================================================

def test_add_company_project_mixed_case():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== P04 MIXED CASE =========="
        )

        random_text = generate_random_text()

        project_name = (
            f"Cloud Computing {random_text}"
        )

        caption = (
            f"Cloud Infrastructure {random_text}"
        )

        description = (
            f"Cloud infrastructure project "
            f"for automation testing {random_text}."
        )

        company_projects.add_project(
            project_name=project_name,
            caption=caption,
            image_path=IMAGE_PATH,
            description=description
        )

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "P04 MIXED CASE PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 6. NEGATIVE - ALL REQUIRED FIELDS EMPTY
# ============================================================

def test_add_company_project_all_empty():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N01 ALL REQUIRED FIELDS EMPTY =========="
        )

        company_projects.enter_project_name(
            ""
        )

        company_projects.enter_caption(
            ""
        )

        company_projects.enter_description(
            ""
        )

        company_projects.click_submit()

        time.sleep(4)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N01 ALL EMPTY PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 7. NEGATIVE - EMPTY PROJECT NAME
# ============================================================

def test_add_company_project_empty_name():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N02 EMPTY PROJECT NAME =========="
        )

        company_projects.enter_project_name(
            ""
        )

        company_projects.enter_caption(
            "Valid Caption"
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            "Valid project description"
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N02 EMPTY PROJECT NAME PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 8. NEGATIVE - EMPTY CAPTION
# ============================================================

def test_add_company_project_empty_caption():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N03 EMPTY CAPTION =========="
        )

        project_name, _, description = (
            generate_project_data()
        )

        company_projects.enter_project_name(
            project_name
        )

        company_projects.enter_caption(
            ""
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            description
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N03 EMPTY CAPTION PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 9. NEGATIVE - EMPTY PHOTO
# ============================================================

def test_add_company_project_empty_photo():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N04 EMPTY PHOTO =========="
        )

        project_name, caption, description = (
            generate_project_data()
        )

        company_projects.enter_project_name(
            project_name
        )

        company_projects.enter_caption(
            caption
        )

        company_projects.enter_description(
            description
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N04 EMPTY PHOTO PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 10. NEGATIVE - EMPTY DESCRIPTION
# ============================================================

def test_add_company_project_empty_description():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N05 EMPTY DESCRIPTION =========="
        )

        project_name, caption, _ = (
            generate_project_data()
        )

        company_projects.enter_project_name(
            project_name
        )

        company_projects.enter_caption(
            caption
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            ""
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N05 EMPTY DESCRIPTION PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 11. NEGATIVE - PROJECT NAME ONLY SPACES
# ============================================================

def test_add_company_project_spaces_name():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N06 SPACES PROJECT NAME =========="
        )

        company_projects.enter_project_name(
            "     "
        )

        company_projects.enter_caption(
            "Valid Caption"
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            "Valid description"
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N06 SPACES PROJECT NAME PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 12. NEGATIVE - CAPTION ONLY SPACES
# ============================================================

def test_add_company_project_spaces_caption():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N07 SPACES CAPTION =========="
        )

        project_name, _, description = (
            generate_project_data()
        )

        company_projects.enter_project_name(
            project_name
        )

        company_projects.enter_caption(
            "     "
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            description
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N07 SPACES CAPTION PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 13. NEGATIVE - DESCRIPTION ONLY SPACES
# ============================================================

def test_add_company_project_spaces_description():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        project_name, caption, _ = (
            generate_project_data()
        )

        print(
            "\n========== N08 SPACES DESCRIPTION =========="
        )

        company_projects.enter_project_name(
            project_name
        )

        company_projects.enter_caption(
            caption
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            "     "
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N08 SPACES DESCRIPTION PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 14. NEGATIVE - NUMERIC PROJECT NAME
# ============================================================

def test_add_company_project_numeric_name():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N09 NUMERIC PROJECT NAME =========="
        )

        company_projects.enter_project_name(
            "123456789"
        )

        company_projects.enter_caption(
            "Valid Caption"
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            "Valid description"
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N09 NUMERIC PROJECT NAME PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 15. NEGATIVE - SPECIAL CHARACTERS
# ============================================================

def test_add_company_project_special_characters():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N10 SPECIAL CHARACTERS =========="
        )

        company_projects.enter_project_name(
            "@#$%^&*"
        )

        company_projects.enter_caption(
            "Valid Caption"
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            "Valid description"
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N10 SPECIAL CHARACTERS PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 16. NEGATIVE - HTML / XSS INPUT
# ============================================================

def test_add_company_project_html_input():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N11 HTML INPUT =========="
        )

        company_projects.enter_project_name(
            "<script>alert('XSS')</script>"
        )

        company_projects.enter_caption(
            "Valid Caption"
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            "Valid description"
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N11 HTML INPUT PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 17. NEGATIVE - LONG PROJECT NAME
# ============================================================

def test_add_company_project_long_name():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N12 LONG PROJECT NAME =========="
        )

        long_name = (
            "Project " + "A" * 300
        )

        company_projects.enter_project_name(
            long_name
        )

        company_projects.enter_caption(
            "Valid Caption"
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            "Valid description"
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N12 LONG PROJECT NAME PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 18. NEGATIVE - LONG DESCRIPTION
# ============================================================

def test_add_company_project_long_description():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N13 LONG DESCRIPTION =========="
        )

        project_name, caption, _ = (
            generate_project_data()
        )

        long_description = (
            "A" * 2000
        )

        company_projects.enter_project_name(
            project_name
        )

        company_projects.enter_caption(
            caption
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_description(
            long_description
        )

        company_projects.click_submit()

        time.sleep(3)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N13 LONG DESCRIPTION PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 19. POSITIVE - VALID URL FORMAT
# ============================================================

def test_company_project_valid_url_format():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== P05 VALID URL FORMAT =========="
        )

        project_name, caption, description = (
            generate_project_data()
        )

        valid_url_1 = (
            "https://www.google.com"
        )

        valid_url_2 = (
            "https://www.linkedin.com/company/example"
        )

        company_projects.enter_project_name(
            project_name
        )

        company_projects.enter_caption(
            caption
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_url_1(
            valid_url_1
        )

        company_projects.enter_url_2(
            valid_url_2
        )

        company_projects.enter_description(
            description
        )

        company_projects.click_submit()

        time.sleep(4)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "P05 VALID URL FORMAT PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 20. NEGATIVE - INVALID URL FORMAT
# ============================================================

def test_company_project_invalid_url_format():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== N14 INVALID URL FORMAT =========="
        )

        project_name, caption, description = (
            generate_project_data()
        )

        invalid_url_1 = (
            "invalid-url"
        )

        invalid_url_2 = (
            "www.invalid"
        )

        company_projects.enter_project_name(
            project_name
        )

        company_projects.enter_caption(
            caption
        )

        company_projects.upload_project_photo(
            IMAGE_PATH
        )

        company_projects.enter_url_1(
            invalid_url_1
        )

        company_projects.enter_url_2(
            invalid_url_2
        )

        company_projects.enter_description(
            description
        )

        company_projects.click_submit()

        time.sleep(4)

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "N14 INVALID URL FORMAT PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 21. EDIT PROJECT
# ============================================================

def test_edit_company_project():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== EDIT COMPANY PROJECT =========="
        )

        random_text = generate_random_text()

        updated_project_name = (
            f"Updated Project {random_text}"
        )

        print(
            "Updated Project Name:",
            updated_project_name
        )

        # --------------------------------------------------------
        # EDIT EXISTING PROJECT
        # ------------------------------------------------------
        company_projects.edit_project(
            project_name=updated_project_name,
            image_path=IMAGE_PATH
        )

        # --------------------------------------------------------
        # VERIFY URL
        # --------------------------------------------------------

        wait.until(
            lambda d:
            "company-projects"
            in d.current_url
        )

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "Updated Project Name:",
            updated_project_name
        )

        print(
            "EDIT COMPANY PROJECT PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 22. DELETE - CANCEL
# ============================================================

def test_delete_company_project_cancel():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== DELETE PROJECT - CANCEL =========="
        )

        company_projects.click_delete_project()

        time.sleep(2)

        company_projects.cancel_delete()

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "DELETE CANCEL PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()


# ============================================================
# 23. DELETE - CONFIRM
# ============================================================

def test_delete_company_project():

    driver, company_projects, wait = (
        open_company_projects()
    )

    try:

        print(
            "\n========== DELETE COMPANY PROJECT =========="
        )

        company_projects.click_delete_project()

        time.sleep(2)

        company_projects.confirm_delete()

        assert (
            "company-projects"
            in driver.current_url
        )

        print(
            "DELETE COMPANY PROJECT PASSED"
        )

    finally:

        time.sleep(3)

        driver.quit()