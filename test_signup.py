from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

def test_signup_valid_email(driver):
    try:
        driver.get("https://www.automationexercise.com/")
        close_cookie_popup(driver)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))).click()
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
        name_input.send_keys("Faouaz")

        email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
        email_input.send_keys("test123@faouaz.com")

        driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
        time.sleep(2)

        assert "Enter Account Information" in driver.page_source
        print("✅ Signup avec email valide fonctionne.")
    except Exception as e:
        print("❌ Échec du signup avec email valide :", e)

def test_signup_invalid_email(driver):
    try:
        driver.get("https://www.automationexercise.com/login")
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
        name_input.send_keys("Faouaz")

        email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
        email_input.send_keys("invalid_email")

        driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
        time.sleep(2)

        assert "New User Signup!" in driver.page_source
        print("✅ Signup avec email invalide ne fonctionne pas (comme prévu).")
    except:
        print("❌ Le test pour email invalide a échoué ou le comportement est incorrect.")

def test_signup_empty_fields(driver):
    try:
        driver.get("https://www.automationexercise.com/login")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).clear()
        driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").clear()

        driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
        time.sleep(2)

        assert "New User Signup!" in driver.page_source
        print("✅ Signup avec champs vides ne fonctionne pas (comme prévu).")
    except:
        print("❌ Le test avec champs vides a échoué ou le comportement est incorrect.")

def main():
    driver = setup_driver()
    try:
        maximize_window = driver.maximize_window()
        test_signup_valid_email(driver)
        test_signup_invalid_email(driver)
        test_signup_empty_fields(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
