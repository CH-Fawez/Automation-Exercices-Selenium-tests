from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the URL of the web page
url = "https://www.automationexercise.com/"

# Set up driver paths
chrome_portable_path = r'C:\ChromeDriver\chrome_133_win64\chrome-win64\chrome-win64\chrome.exe'
chromedriver_path = r'C:\ChromeDriver\ChromeDriver_133\chromedriver-win32\chromedriver-win32\chromedriver.exe'

def setup_driver():
    chrome_options = Options()
    chrome_options.binary_location = chrome_portable_path
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def close_cookie_popup(driver):
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]/p'))
        )
        cookie_button.click()
    except:
        print("Cookie button not found or already dismissed.")

def navigate_to_web_page(driver, url):
    driver.get(url)
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Home']")))
    print("✅Web page loaded successfully")
    return driver

def click_on_login_signup_button (driver):
    login_button = driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']")
    login_button.click()
    print("✅Login/Signup button clicked successfully")
    return driver

def login_with_valid_credentials(driver):
    try:
        # Login with valid credentials
        default_email = "test123@faouaz.com"
        default_password = "pswd123"
        email_input = driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
        email_input.send_keys(default_email)
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_input.send_keys(default_password)
        login_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
        login_button.click()
        print("✅Logged in successfully with valid credentials")

    except Exception as e:
        print(f"�� Failed to login with valid credentials: {e}")
        return driver

def logout(driver):
    try:
        logout_button = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
        logout_button.click()
        time.sleep(2)
        assert "Login to your account" in driver.page_source  # Check if the logout message is displayed
        print("✅Logged out successfully")
        return driver
    except:
        print("Failed to logout")
        return driver



def login_with_invalid_credentials(driver):
        try:
            # Login with invalid credentials
            default_email = "test123@faouaz.com"
            default_password = "invalid_password"
            email_input = driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
            email_input.send_keys(default_email)
            password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
            password_input.send_keys(default_password)
            login_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
            login_button.click()
            time.sleep(2)  # Wait for the error message to appear
            assert "Your email or password is incorrect!" in driver.page_source
            print("✅Failed to log in with invalid credentials")
        except Exception as e:
            print("log in with invalid credentials works: {e}")

def main():
    driver = setup_driver()
    try:
         navigate_to_web_page(driver, url)
         maximize_window = driver.maximize_window()
         close_cookie_popup(driver)
         click_on_login_signup_button(driver)
         login_with_valid_credentials(driver)
         logout(driver)
         login_with_invalid_credentials(driver)


    finally:
        driver.quit()

if __name__ == "__main__":
    main()









