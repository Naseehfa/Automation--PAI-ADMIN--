import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ============================================================
    # LOCATORS
    # ============================================================

    about_menu = (
        By.XPATH,
        "//span[text()='About']"
    )

    add_employee_btn = (
        By.XPATH,
        "//button[contains(text(),'Add Employee')]"
    )

    # ============================================================
    # ADD EMPLOYEE FORM
    # ============================================================

    name_input = (
        By.XPATH,
        "//input[@placeholder='Add employee name']"
    )

    job_dropdown = (
        By.XPATH,
        "//select"
    )

    linkedin_input = (
        By.XPATH,
        "//input[@placeholder='Add Linked URL']"
    )

    bio_textarea = (
        By.XPATH,
        "(//textarea[@placeholder='Write a short bio about employee'])[1]"
    )

    image_input = (
        By.XPATH,
        "//input[@type='file']"
    )

    # ============================================================
    # EDIT EMPLOYEE
    # ============================================================

    # First employee - Edit button
    edit_employee_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div/button[1]/img"
    )

    # Edit modal - Name
    edit_name_input = (
        By.ID,
        "modal-name"
    )

    # Edit modal - LinkedIn
    edit_linkedin_input = (
        By.ID,
        "modal-linkedin"
    )

    # Update button
    update_btn = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/form/div[3]/button"
    )

    # ============================================================
    # DELETE EMPLOYEE
    # ============================================================

    # ------------------------------------------------------------
    # DELETE 1
    # ------------------------------------------------------------

    delete_employee_btn_1 = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div/button[2]/img"
    )

    delete_confirm_btn_1 = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/button[1]"
    )

    # ------------------------------------------------------------
    # DELETE 2
    # ------------------------------------------------------------

    delete_employee_btn_2 = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div/button[2]/img"
    )

    delete_confirm_btn_2 = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/button"
    )

    # ------------------------------------------------------------
    # DELETE 3
    # ------------------------------------------------------------

    delete_employee_btn_3 = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div/button[2]/img"
    )

    delete_confirm_btn_3 = (
        By.XPATH,
        "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/button[2]"
    )

    # ============================================================
    # NAVIGATION
    # ============================================================

    def click_about(self):

        time.sleep(2)

        about = self.wait.until(
            EC.element_to_be_clickable(
                self.about_menu
            )
        )

        about.click()

        time.sleep(3)

    # ============================================================
    # ADD EMPLOYEE
    # ============================================================

    def fill_employee_form(
        self,
        name="",
        position="",
        linkedin_url="",
        description="",
        image_path=""
    ):

        # ========================================================
        # NAME
        # ========================================================

        name_field = self.wait.until(
            EC.visibility_of_element_located(
                self.name_input
            )
        )

        time.sleep(2)

        name_field.clear()

        if name:
            name_field.send_keys(name)

        time.sleep(3)

        # ========================================================
        # POSITION
        # ========================================================

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                self.job_dropdown
            )
        )

        time.sleep(2)

        dropdown.click()

        time.sleep(2)

        if position:
            dropdown.send_keys(position)

        time.sleep(3)

        # ========================================================
        # LINKEDIN
        # ========================================================

        linkedin_field = self.wait.until(
            EC.visibility_of_element_located(
                self.linkedin_input
            )
        )

        time.sleep(2)

        linkedin_field.clear()

        if linkedin_url:
            linkedin_field.send_keys(linkedin_url)

        time.sleep(3)

        # ========================================================
        # DESCRIPTION
        # ========================================================

        bio_field = self.wait.until(
            EC.visibility_of_element_located(
                self.bio_textarea
            )
        )

        time.sleep(2)

        bio_field.clear()

        if description:
            bio_field.send_keys(description)

        time.sleep(3)

        # ========================================================
        # IMAGE
        # ========================================================

        if image_path:

            time.sleep(2)

            image_field = self.wait.until(
                EC.presence_of_element_located(
                    self.image_input
                )
            )

            time.sleep(2)

            image_field.send_keys(image_path)

            time.sleep(4)

        time.sleep(3)

    # ============================================================
    # CLICK ADD EMPLOYEE
    # ============================================================

    def click_add_employee(self):

        time.sleep(3)

        add_btn = self.wait.until(
            EC.presence_of_element_located(
                self.add_employee_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            add_btn
        )

        time.sleep(3)

        self.wait.until(
            EC.element_to_be_clickable(
                self.add_employee_btn
            )
        )

        time.sleep(2)

        try:

            add_btn.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                add_btn
            )

        time.sleep(5)

    # ============================================================
    # EDIT EMPLOYEE
    # ============================================================

    def edit_first_employee(
        self,
        new_name="Soya",
        new_linkedin="https://www.linkedin.com/in/Soya"
    ):

        # ========================================================
        # CLICK EDIT
        # ========================================================

        time.sleep(3)

        edit_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.edit_employee_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            edit_btn
        )

        time.sleep(3)

        edit_btn.click()

        time.sleep(3)

        # ========================================================
        # CHANGE NAME
        # ========================================================

        name_field = self.wait.until(
            EC.visibility_of_element_located(
                self.edit_name_input
            )
        )

        time.sleep(2)

        name_field.clear()

        time.sleep(1)

        name_field.send_keys(new_name)

        time.sleep(3)

        # ========================================================
        # CHANGE LINKEDIN
        # ========================================================

        linkedin_field = self.wait.until(
            EC.visibility_of_element_located(
                self.edit_linkedin_input
            )
        )

        time.sleep(2)

        linkedin_field.clear()

        time.sleep(1)

        linkedin_field.send_keys(new_linkedin)

        time.sleep(3)

        # ========================================================
        # CLICK UPDATE
        # ========================================================

        update_button = self.wait.until(
            EC.element_to_be_clickable(
                self.update_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            update_button
        )

        time.sleep(3)

        update_button.click()

        time.sleep(5)

    # ============================================================
    # DELETE EMPLOYEE - METHOD 1
    # ============================================================

    def delete_first_employee_1(self):

        # Click Delete button
        time.sleep(3)

        delete_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_employee_btn_1
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            delete_btn
        )

        time.sleep(3)

        delete_btn.click()

        time.sleep(3)

        # Click first confirmation button
        confirm_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_confirm_btn_1
            )
        )

        time.sleep(2)

        confirm_btn.click()

        time.sleep(5)

    # ============================================================
    # DELETE EMPLOYEE - METHOD 2
    # ============================================================

    def delete_first_employee_2(self):

        # Click Delete button
        time.sleep(3)

        delete_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_employee_btn_2
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            delete_btn
        )

        time.sleep(3)

        delete_btn.click()

        time.sleep(3)

        # Click confirmation button
        confirm_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_confirm_btn_2
            )
        )

        time.sleep(2)

        confirm_btn.click()

        time.sleep(5)

    # ============================================================
    # DELETE EMPLOYEE - METHOD 3
    # ============================================================

    def delete_first_employee_3(self):

        # Click Delete button
        time.sleep(3)

        delete_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_employee_btn_3
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            delete_btn
        )

        time.sleep(3)

        delete_btn.click()

        time.sleep(3)

        # Click second confirmation button
        confirm_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_confirm_btn_3
            )
        )

        time.sleep(2)

        confirm_btn.click()

        time.sleep(5)