
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


LOGIN_URL = (
    "https://paiwebsiteqa.pineappleai.cloud/admin/login"
)


@pytest.fixture
def driver():

    # ============================================================
    # CHROME OPTIONS
    # ============================================================

    options = Options()
    options.add_argument("--start-maximized")

    # ============================================================
    # START CHROME
    # ============================================================

    driver = webdriver.Chrome(options=options)

    # ============================================================
    # OPEN LOGIN PAGE
    # ============================================================

    driver.get(LOGIN_URL)

    # ============================================================
    # WAIT FOR PAGE TO LOAD
    # ============================================================

    driver.implicitly_wait(5)

    # ============================================================
    # SEND DRIVER TO TEST
    # ============================================================

    yield driver

    # ============================================================
    # CLOSE BROWSER
    # ============================================================

    driver.quit()

