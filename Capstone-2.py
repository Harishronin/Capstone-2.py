"""
TestcaseID:TC_PIM_01

Test objective:
  Forgot password link validation on login page
URL= https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Precondition:
1.Launch URL
2.OrangeHRM 3.0 site launched on a compatible browser
3.Click on “Forgot password” link
Steps
1.Username textbox is visible
2.Provide username
3.Click on Reset Password

Expected Result:
The user should be able to see the username box and get a successful message saying “Reset password link sent successfully”.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # To handle TimeoutException

class LoginPage:
    """Page Object Model for the Login Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.forgot_password_link = (By.LINK_TEXT, "Forgot your password?")
        self.username_reset_field = (By.NAME, "username")  # Username field on the reset page
        self.reset_password_button = (By.XPATH, "//button[contains(text(),'Reset Password')]")
        self.success_message = (By.XPATH, "//div[contains(text(),'Reset password link sent successfully')]")

    def open(self, url):
        """Open the login page."""
        self.driver.get(url)

    def click_forgot_password(self):
        """Click on the 'Forgot your password?' link."""
        self.wait.until(EC.element_to_be_clickable(self.forgot_password_link)).click()

    def provide_username_for_reset(self, username):
        """Provide username to reset password."""
        # Wait for the reset password page to load and ensure the username field is present
        self.wait.until(EC.presence_of_element_located(self.username_reset_field))

        # Interact with the username field
        username_field = self.driver.find_element(*self.username_reset_field)
        username_field.clear()
        username_field.send_keys(username)

        # Click the Reset Password button
        self.wait.until(EC.element_to_be_clickable(self.reset_password_button)).click()

    def is_success_message_displayed(self):
        """Check if the success message is displayed."""
        try:
            # Wait for the success message to appear and check if it's visible
            success_element = self.wait.until(EC.presence_of_element_located(self.success_message))
            return success_element.is_displayed()
        except TimeoutException:
            print("Error: Timeout - Success message not found")
            return False


# Test case for forgot password functionality
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    """Initializes the WebDriver."""
    driver = webdriver.Chrome()  # You can replace this with Firefox, Edge, etc.
    driver.maximize_window()
    yield driver
    driver.quit()

def test_forgot_password(driver):
    """
    Test Case: TC_PIM_01 - Forgot password link validation on the login page.
    """

    from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object Model for the Login Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.forgot_password_link = (By.LINK_TEXT, "Forgot your password?")
        self.username_reset_field = (By.NAME, "username")  # Username field on the reset page
        self.reset_password_button = (By.XPATH, "//button[contains(text(),'Reset Password')]")
        self.success_message = (By.XPATH, "//div[contains(text(),'Reset password link sent successfully')]")

    def open(self, url):
        """Open the login page."""
        self.driver.get(url)

    def click_forgot_password(self):
        """Click on the 'Forgot your password?' link."""
        self.wait.until(EC.element_to_be_clickable(self.forgot_password_link)).click()

    def is_username_textbox_visible(self):
        """Check if the username textbox is visible on the reset password page."""
        return self.wait.until(EC.visibility_of_element_located(self.username_reset_field))

    def enter_username(self, username):
        """Enter the username to reset the password."""
        username_field = self.wait.until(EC.presence_of_element_located(self.username_reset_field))
        username_field.clear()
        username_field.send_keys(username)

    def click_reset_password(self):
        """Click the 'Reset Password' button."""
        self.wait.until(EC.element_to_be_clickable(self.reset_password_button)).click()

    def is_success_message_displayed(self):
        """Check if the success message is displayed."""
        try:
            success_element = self.wait.until(EC.presence_of_element_located(self.success_message))
            return success_element.is_displayed()
        except Exception:
            return False

import pytest
from selenium import webdriver
from pages.login_page import LoginPage  # Ensure this import is correct

@pytest.fixture(scope="function")
def driver():
    """Initializes the WebDriver."""
    driver = webdriver.Chrome()  # You can replace this with Firefox, Edge, etc.
    driver.maximize_window()
    yield driver
    driver.quit()

def test_forgot_password(driver):
    """
    Test Case: Validate the forgot password functionality on the login page.
    """
    # Test data
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"  # Assuming 'Admin' is the username for reset purpose

    # Initialize Page Object
    login_page = LoginPage(driver)

    # Step 1: Open the login page
    login_page.open(url)

    # Step 2: Click on the "Forgot your password?" link
    login_page.click_forgot_password()

    # Step 3: Validate that the username textbox is visible
    assert login_page.is_username_textbox_visible(), "Username textbox is not visible."

    # Step 4: Provide username
    login_page.enter_username(username)

    # Step 5: Click on Reset Password button
    login_page.click_reset_password()

    # Step 6: Validate the success message
    assert login_page.is_success_message_displayed(), "Success message is not displayed."
    print("Test Passed: Forgot password functionality works as expected.")

"""
TestcaseID:TC_PIM_02
Test objective:
  Header validation on Admin page 
Precondition:
1.Launch URL and login as “Admin”
2.OrangeHRM 3.0 site launched on a compatible browser
Steps:
1.Go to Admin page and validate “Title of the page as OrangeHRM”
2.Validate below options are displaying on admin page
                 1.User management
                 2.Job
                3.Organizations
               4.Qualifications
               5.Nationalities
              6.Corporate banking
              7.Configuration

Expected Result:
The user should be able to see above mentioned Admin page headers on Admin page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    """Page Object Model for the OrangeHRM Admin Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.admin_link = (By.XPATH, "//span[text()='Admin']")

    def navigate_to_admin_page(self):
        """Navigates to the Admin page."""
        self.wait.until(EC.element_to_be_clickable(self.admin_link)).click()

    def validate_page_title(self, expected_title):
        """Validates the title of the page."""
        self.wait.until(lambda d: d.title == expected_title)
        assert self.driver.title == expected_title, f"Expected: {expected_title}, Found: {self.driver.title}"

    def are_headers_present(self, headers):
        """Validates the presence of specified headers on the Admin page."""
        for header in headers:
            header_xpath = (By.XPATH, f"//span[text()='{header}']")
            try:
                self.wait.until(EC.visibility_of_element_located(header_xpath))
                print(f"Header '{header}' is visible on the Admin page.")
            except Exception:
                print(f"Header '{header}' is NOT visible on the Admin page.")
                return False
        return True
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

@pytest.fixture(scope="function")
def driver():
    """Initializes the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_admin_page_headers(driver):
    """
    Test Case: Validate the headers on the Admin page.
    """

    # Test data
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    expected_title = "OrangeHRM"

    headers = ["User Management", "Job", "Organization", "Qualification", "Reports"]  # Example headers to validate

    # Initialize Page Objects
    login_page = LoginPage(driver)
    admin_page = AdminPage(driver)

    # Step 1: Open the login page
    login_page.open(url)

    # Step 2: Log in to the application (Assuming LoginPage has a method to handle login)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    # Step 3: Navigate to the Admin page
    admin_page.navigate_to_admin_page()

    # Step 4: Validate the page title
    admin_page.validate_page_title(expected_title)

    # Step 5: Validate the headers on the Admin page
    headers_present = admin_page.are_headers_present(headers)
    assert headers_present, "One or more headers are missing on the Admin page."

    print("Test Passed: All specified headers are visible on the Admin page.")
  
 """
    Test Case: Validate headers on the Admin page.
    """
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object Model for the Login Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self, url):
        """Open the login page."""
        self.driver.get(url)

    def enter_username(self, username):
        """Enter the username."""
        self.wait.until(EC.presence_of_element_located(self.username_field))
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        """Enter the password."""
        self.wait.until(EC.presence_of_element_located(self.password_field))
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        """Click on the login button."""
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username, password):
        """Login using the provided username and password."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    """Page Object Model for the OrangeHRM Admin Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.admin_link = (By.XPATH, "//span[text()='Admin']")

    def navigate_to_admin_page(self):
        """Navigates to the Admin page."""
        self.wait.until(EC.element_to_be_clickable(self.admin_link)).click()

    def validate_page_title(self, expected_title):
        """Validates the title of the page."""
        self.wait.until(lambda d: d.title == expected_title)
        assert self.driver.title == expected_title, f"Expected: {expected_title}, Found: {self.driver.title}"

    def are_headers_present(self, headers):
        """Validates the presence of specified headers on the Admin page."""
        all_headers_present = True
        for header in headers:
            header_xpath = (By.XPATH, f"//span[text()='{header}']")
            try:
                self.wait.until(EC.visibility_of_element_located(header_xpath))
                print(f"Header '{header}' is visible on the Admin page.")
            except Exception:
                print(f"Header '{header}' is NOT visible on the Admin page.")
                all_headers_present = False
        return all_headers_present
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

@pytest.fixture(scope="function")
def driver():
    """Initializes the WebDriver."""
    driver = webdriver.Chrome()  # You can replace this with Firefox, Edge, etc.
    driver.maximize_window()
    yield driver
    driver.quit()

def test_admin_page_headers(driver):
    """
    Test Case: Validate the headers on the Admin page.
    """

    # Test data
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    expected_title = "OrangeHRM"
    expected_headers = [
        "User Management",
        "Job",
        "Organization",
        "Qualifications",
        "Nationalities",
        "Corporate Banking",
        "Configuration"
    ]

    # Initialize Page Objects
    login_page = LoginPage(driver)
    admin_page = AdminPage(driver)

    # Step 1: Open the login page and log in as Admin
    login_page.open(url)
    login_page.login(username, password)

    # Step 2: Navigate to the Admin page
    admin_page.navigate_to_admin_page()

    # Step 3: Validate the title of the page
    admin_page.validate_page_title(expected_title)

    # Step 4: Validate the presence of expected headers
    assert admin_page.are_headers_present(expected_headers), "Not all headers are visible on the Admin page."

    print("Test Passed: All specified headers are visible on the Admin page.")
"""
TestcaseID:TC_PIM_03
Test objective:
  Main menu validation on Admin page 
Precondition:
1.Launch URL and login as “Admin”
2.OrangeHRM 3.0 site launched on a compatible browser
Steps:
             1.Go to admin Page
             2.Validate below “Menu options”(on side pane)displaying on Admin page

                 a.Admin
                 b.PIM
                 C.Time
                 d.Leave
                 e.Recruitment
                 f.My Info
                 g.Performance
                 h.Dashboard
                 i.Directory
                k.Maintainance
                l.Buzz

Ecpected Result: The user should able to see above mentioned Admin Page Menu items on Admin page.
"""

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.admin_page import AdminPage


@pytest.fixture(scope="function")
def driver():
    """
    Initializes the WebDriver.
    """
    driver = webdriver.Chrome()  # Ensure the correct browser driver is installed
    driver.maximize_window()
    yield driver
    driver.quit()


def test_admin_page_menu_options(driver):
    """
    TestcaseID: TC_PIM_03
    Test Objective: Validate the main menu options displayed on the Admin page.
    Precondition:
      1. Launch URL and login as "Admin".
      2. OrangeHRM 3.0 site launched on a compatible browser.
    """

    # Test data
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    expected_menu_options = [
        "Admin",
        "PIM",
        "Time",
        "Leave",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard",
        "Directory",
        "Maintenance",
        "Buzz",
    ]

    # Initialize Page Objects
    login_page = LoginPage(driver)
    admin_page = AdminPage(driver)

    # Step 1: Open the login page and log in as Admin
    login_page.open(url)
    login_page.login(username, password)

    # Step 2: Navigate to the Admin page
    admin_page.navigate_to_admin_page()

    # Step 3: Validate that the expected menu options are visible
    all_options_visible = admin_page.are_menu_options_present(expected_menu_options)

    # Step 4: Assert that all menu options are visible
    assert all_options_visible, "Not all menu options are visible on the Admin page."

    print("Test Passed: All specified menu options are visible on the Admin page.")
