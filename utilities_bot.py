# automation_bot.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutomationExerciseBot:
    def __init__(self, chrome_path, driver_path, url):
        self.chrome_path = chrome_path
        self.driver_path = driver_path
        self.url = url
        self.driver = None

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.binary_location = self.chrome_path
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        return self.driver

    def navigate_to_web_page(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Home']"))
        )
        print("✅ Web page loaded successfully")

    def close_cookie_popup(self):
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]/p'))
            )
            cookie_button.click()
        except:
            print("Cookie button not found or already dismissed.")

    def click_on_login_signup_button(self):
        login_button = self.driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']")
        login_button.click()
        print("✅ Login/Signup button clicked successfully")

    def login_with_valid_credentials(self, email="test123@faouaz.com", password="pswd123"):
        try:
            email_input = self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
            email_input.send_keys(email)
            password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
            password_input.send_keys(password)
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
            login_button.click()
            print("✅ Logged in successfully with valid credentials")
        except Exception as e:
            print(f"❌ Failed to login: {e}")

    def quit(self):
        self.driver.quit()
