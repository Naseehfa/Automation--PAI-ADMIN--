import os

from utils.driver_setup import get_driver
from config.config import URL, VALID_USERNAME, VALID_PASSWORD
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from selenium.webdriver.support.ui import WebDriverWait


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
# HELPER FUNCTION
# ============================================================

def open_employee_form():

    driver = get_driver()

    driver.get(URL)

    # ========================================================
    # REDUCE PAGE ZOOM
    # ========================================================

    driver.execute_script(
        "document.body.style.zoom='80%'"
    )

    # ========================================================
    # LOGIN
    # ========================================================

    login = LoginPage(driver)

    login.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    wait = WebDriverWait(driver, 20)

    wait.until(
        lambda d: "admin" in d.current_url
    )

    # ========================================================
    # NAVIGATION
    # ========================================================

    menu = MenuPage(driver)

    menu.click_about()

    wait.until(
        lambda d: "team" in d.current_url
    )

    return driver, menu, wait


# ============================================================
# 1. VALID DATA
# ============================================================

def test_add_employee_valid_data():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="John Doe",
        position="QA Engineer",
        linkedin_url="https://linkedin.com/in/johndoe",
        description="Experienced QA Engineer",
        image_path=IMAGE_PATH
    )

    menu.click_add_employee()

    wait.until(
        lambda d: "team" in d.current_url
    )

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 2. ALL FIELDS EMPTY
# ============================================================

def test_add_employee_all_fields_empty():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="",
        position="",
        linkedin_url="",
        description="",
        image_path=""
    )

    menu.click_add_employee()

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 3. EMPTY NAME
# ============================================================

def test_add_employee_empty_name():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="",
        position="QA Engineer",
        linkedin_url="https://linkedin.com/in/johndoe",
        description="Experienced QA Engineer",
        image_path=IMAGE_PATH
    )

    menu.click_add_employee()

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 4. EMPTY POSITION
# ============================================================

def test_add_employee_empty_position():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="John Doe",
        position="",
        linkedin_url="https://linkedin.com/in/johndoe",
        description="Experienced QA Engineer",
        image_path=IMAGE_PATH
    )

    menu.click_add_employee()

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 5. EMPTY LINKEDIN URL
# ============================================================

def test_add_employee_empty_linkedin():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="John Doe",
        position="QA Engineer",
        linkedin_url="",
        description="Experienced QA Engineer",
        image_path=IMAGE_PATH
    )

    menu.click_add_employee()

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 6. EMPTY DESCRIPTION
# ============================================================

def test_add_employee_empty_description():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="John Doe",
        position="QA Engineer",
        linkedin_url="https://linkedin.com/in/johndoe",
        description="",
        image_path=IMAGE_PATH
    )

    menu.click_add_employee()

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 7. INVALID NAME - NUMBERS
# ============================================================

def test_add_employee_invalid_name_numbers():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="123456",
        position="QA Engineer",
        linkedin_url="https://linkedin.com/in/johndoe",
        description="Experienced QA Engineer",
        image_path=IMAGE_PATH
    )

    menu.click_add_employee()

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 8. INVALID NAME - SPECIAL CHARACTERS
# ============================================================

def test_add_employee_invalid_name_special_characters():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="@#$%^&*",
        position="QA Engineer",
        linkedin_url="https://linkedin.com/in/johndoe",
        description="Experienced QA Engineer",
        image_path=IMAGE_PATH
    )

    menu.click_add_employee()

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 9. INVALID LINKEDIN URL
# ============================================================

def test_add_employee_invalid_linkedin():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="John Doe",
        position="QA Engineer",
        linkedin_url="invalid-url",
        description="Experienced QA Engineer",
        image_path=IMAGE_PATH
    )

    menu.click_add_employee()

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 10. INVALID DESCRIPTION
# ============================================================

def test_add_employee_invalid_description():

    driver, menu, wait = open_employee_form()

    menu.fill_employee_form(
        name="John Doe",
        position="QA Engineer",
        linkedin_url="https://linkedin.com/in/johndoe",
        description="@#$%^&*",
        image_path=IMAGE_PATH
    )

    menu.click_add_employee()

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 11. EDIT EMPLOYEE
# ============================================================

def test_edit_employee():

    driver, menu, wait = open_employee_form()

    menu.edit_first_employee(
        new_name="Soya",
        new_linkedin="https://www.linkedin.com/in/Soya"
    )

    wait.until(
        lambda d: "team" in d.current_url
    )

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 12. DELETE EMPLOYEE - CONFIRM BUTTON 1
# ============================================================

def test_delete_employee_1():

    driver, menu, wait = open_employee_form()

    menu.delete_first_employee_1()

    wait.until(
        lambda d: "team" in d.current_url
    )

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 13. DELETE EMPLOYEE - CONFIRM BUTTON
# ============================================================

def test_delete_employee_2():

    driver, menu, wait = open_employee_form()

    menu.delete_first_employee_2()

    wait.until(
        lambda d: "team" in d.current_url
    )

    assert "team" in driver.current_url

    driver.quit()


# ============================================================
# 14. DELETE EMPLOYEE - CONFIRM BUTTON 2
# ============================================================

def test_delete_employee_3():

    driver, menu, wait = open_employee_form()

    menu.delete_first_employee_3()

    wait.until(
        lambda d: "team" in d.current_url
    )

    assert "team" in driver.current_url

    driver.quit()

