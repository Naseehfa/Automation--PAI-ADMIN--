import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CompanyProjectsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ============================================================
    # URL
    # ============================================================

    COMPANY_PROJECTS_URL = (
        "https://paiwebsiteqa.pineappleai.cloud/admin/company-projects"
    )

    # ============================================================
    # LEFT MENU
    # ============================================================

    COMPANY_PROJECTS_MENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[4]/button/span'
    )

    COMPANY_PROJECTS_MENU_ALT = (
        By.XPATH,
        '/html/body/div/div/aside/nav/div[4]/button/span'
    )

    COMPANY_PROJECTS_SUBMENU = (
        By.XPATH,
        '//*[@id="root"]/div/aside/nav/div[4]/div/button[1]'
    )

    # ============================================================
    # ADD PROJECT FORM
    # ============================================================

    PROJECT_NAME = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[1]/input'
    )

    CAPTION = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/input'
    )

    PROJECT_PHOTO = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[3]/div/span'
    )

    URL_FIELD_1 = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[4]/input'
    )

    URL_FIELD_2 = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[5]/input'
    )

    OPTIONAL_FIELD_3 = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[6]/div'
    )

    DESCRIPTION = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/textarea'
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[1]/div[3]/button'
    )

    # ============================================================
    # EDIT PROJECT
    # ============================================================

    # NEW SPECIFIC EDIT-ROW XPATH
    EDIT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[7]/button[1]/img'
    )

    # Edit modal
    EDIT_MODAL = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[3]/div/div[3]/div'
    )

    # Confirmed edit project name XPath
    EDIT_PROJECT_NAME = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[3]/div/div[4]/div/input'
    )

    # Edit photo
    EDIT_PROJECT_PHOTO = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[3]/div/div[6]/div/div/span'
    )

    # Confirmed edit/save button XPath
    EDIT_SAVE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[3]/div/div[8]/button'
    )

    # ============================================================
    # DELETE PROJECT
    # ============================================================

    DELETE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[7]/button[2]/img'
    )

    DELETE_CANCEL_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[3]/div/div[2]/button[1]'
    )

    DELETE_CONFIRM_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div/div/div[2]/div[3]/div/div[2]/button[2]'
    )

    # ============================================================
    # NAVIGATION
    # ============================================================

    def open_company_projects(self):

        self.driver.get(
            self.COMPANY_PROJECTS_URL
        )

        self.wait.until(
            EC.url_contains(
                "/admin/company-projects"
            )
        )

        time.sleep(3)

    def click_company_projects_menu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.COMPANY_PROJECTS_MENU
            )
        )

        element.click()

        time.sleep(1)

    def click_company_projects_submenu(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.COMPANY_PROJECTS_SUBMENU
            )
        )

        element.click()

        self.wait.until(
            EC.url_contains(
                "/admin/company-projects"
            )
        )

        time.sleep(3)

    def navigate_to_company_projects(self):

        self.click_company_projects_menu()

        self.click_company_projects_submenu()

    # ============================================================
    # PROJECT NAME
    # ============================================================

    def enter_project_name(self, project_name):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.PROJECT_NAME
            )
        )

        element.clear()

        element.send_keys(
            project_name
        )

        time.sleep(1)

    # ============================================================
    # CAPTION
    # ============================================================

    def enter_caption(self, caption):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.CAPTION
            )
        )

        element.clear()

        element.send_keys(
            caption
        )

        time.sleep(1)

    # ============================================================
    # PROJECT PHOTO
    # ============================================================

    def upload_project_photo(self, image_path):

        file_input = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//input[@type="file"]'
                )
            )
        )

        file_input.send_keys(
            image_path
        )

        time.sleep(2)

        print(
            "Project photo uploaded:",
            image_path
        )

    # ============================================================
    # URL FIELD 1
    # ============================================================

    def enter_url_1(self, url):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.URL_FIELD_1
            )
        )

        element.clear()

        element.send_keys(
            url
        )

        time.sleep(1)

    # ============================================================
    # URL FIELD 2
    # ============================================================

    def enter_url_2(self, url):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.URL_FIELD_2
            )
        )

        element.clear()

        element.send_keys(
            url
        )

        time.sleep(1)

    # ============================================================
    # OPTIONAL FIELD 3
    # ============================================================

    def click_optional_field_3(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.OPTIONAL_FIELD_3
            )
        )

        element.click()

        time.sleep(1)

    # ============================================================
    # DESCRIPTION
    # ============================================================

    def enter_description(self, description):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.DESCRIPTION
            )
        )

        element.clear()

        element.send_keys(
            description
        )

        time.sleep(1)

    # ============================================================
    # SUBMIT
    # ============================================================

    def click_submit(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON
            )
        )

        element.click()

        time.sleep(4)

    # ============================================================
    # FILL REQUIRED FIELDS
    # ============================================================

    def fill_required_fields(
        self,
        project_name,
        caption,
        image_path,
        description
    ):

        self.enter_project_name(
            project_name
        )

        self.enter_caption(
            caption
        )

        self.upload_project_photo(
            image_path
        )

        self.enter_description(
            description
        )

        time.sleep(2)

    # ============================================================
    # ADD PROJECT
    # ============================================================

    def add_project(
        self,
        project_name,
        caption,
        image_path,
        description
    ):

        self.fill_required_fields(
            project_name=project_name,
            caption=caption,
            image_path=image_path,
            description=description
        )

        self.click_submit()

        time.sleep(4)

    # ============================================================
    # ADD PROJECT WITH URLS
    # ============================================================

    def add_project_with_urls(
        self,
        project_name,
        caption,
        image_path,
        url_1,
        url_2,
        description
    ):

        self.enter_project_name(
            project_name
        )

        self.enter_caption(
            caption
        )

        self.upload_project_photo(
            image_path
        )

        self.enter_url_1(
            url_1
        )

        self.enter_url_2(
            url_2
        )

        self.enter_description(
            description
        )

        time.sleep(2)

        self.click_submit()

        time.sleep(4)

    # ============================================================
    # EDIT PROJECT
    # ============================================================

    def click_edit_project(self):

        print(
            "Clicking Edit Project button..."
        )

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        time.sleep(1)

        element.click()

        time.sleep(2)

        print(
            "Edit button clicked."
        )

    # ============================================================
    # WAIT FOR EDIT MODAL
    # ============================================================

    def wait_for_edit_modal(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_MODAL
            )
        )

        time.sleep(2)

        print(
            "Edit modal opened."
        )

    # ============================================================
    # ENTER EDIT PROJECT NAME
    # ============================================================

    def enter_edit_project_name(
        self,
        project_name
    ):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.EDIT_PROJECT_NAME
            )
        )

        element.clear()

        element.send_keys(
            project_name
        )

        time.sleep(1)

        print(
            "Updated Project Name:",
            project_name
        )

    # ============================================================
    # UPLOAD EDIT PROJECT PHOTO
    # ============================================================

    def upload_edit_project_photo(
        self,
        image_path
    ):

        file_inputs = self.driver.find_elements(
            By.XPATH,
            '//input[@type="file"]'
        )

        if not file_inputs:

            raise Exception(
                "No file input found for edit project."
            )

        file_input = file_inputs[-1]

        file_input.send_keys(
            image_path
        )

        time.sleep(2)

        print(
            "Edit project photo uploaded:",
            image_path
        )

    # ============================================================
    # SAVE EDIT
    # ============================================================

    def click_edit_save(self):

        print(
            "Clicking Edit Save button..."
        )

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_SAVE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        time.sleep(1)

        element.click()

        time.sleep(4)

        print(
            "Project edit saved."
        )

    # ============================================================
    # COMPLETE EDIT
    # ============================================================

    def edit_project(
        self,
        project_name,
        image_path=None
    ):

        # --------------------------------------------------------
        # 1. Click Edit
        # --------------------------------------------------------

        self.click_edit_project()

        # --------------------------------------------------------
        # 2. Wait for Edit Modal
        # --------------------------------------------------------

        self.wait_for_edit_modal()

        # --------------------------------------------------------
        # 3. Update Project Name
        # --------------------------------------------------------

        self.enter_edit_project_name(
            project_name
        )

        # --------------------------------------------------------
        # 4. Update Image if provided
        # --------------------------------------------------------

        if image_path is not None:

            self.upload_edit_project_photo(
                image_path
            )

        # --------------------------------------------------------
        # 5. Save
        # --------------------------------------------------------

        self.click_edit_save()

        time.sleep(4)

    # ============================================================
    # DELETE PROJECT
    # ============================================================

    def click_delete_project(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_BUTTON
            )
        )

        element.click()

        time.sleep(3)

    # ============================================================
    # CANCEL DELETE
    # ============================================================

    def cancel_delete(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_CANCEL_BUTTON
            )
        )

        element.click()

        time.sleep(3)

    # ============================================================
    # CONFIRM DELETE
    # ============================================================

    def confirm_delete(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_CONFIRM_BUTTON
            )
        )

        element.click()

        time.sleep(4)

    # ============================================================
    # COMPLETE DELETE
    # ============================================================

    def delete_project(self):

        self.click_delete_project()

        time.sleep(2)

        self.confirm_delete()

        time.sleep(4)