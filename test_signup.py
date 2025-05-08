from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random

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
        print("➡️ Nom saisi")

        # Générer un email aléatoire
        random_email = f"test{random.randint(1000, 9999)}@faouaz.com"

        email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
        email_input.send_keys(random_email)
        print(f"➡️ Email saisi : {random_email}")

        driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
        time.sleep(2)

        assert "Enter Account Information" in driver.page_source
        pswd_input = driver.find_element(By.ID, "password")
        pswd_input.send_keys("pswd123")
        day_select = Select(driver.find_element(By.CSS_SELECTOR, "#days"))
        day_select.select_by_value("7")
        month_select = Select(driver.find_element(By.CSS_SELECTOR, "#months"))
        month_select.select_by_value("4")
        year_select = Select(driver.find_element(By.CSS_SELECTOR, "#years"))
        year_select.select_by_value("1996")
        first_name_input = driver.find_element(By.ID, "first_name").send_keys("Testeur")
        last_name_input = driver.find_element(By.ID, "last_name").send_keys("AUTOMATION")
        company_input = driver.find_element(By.ID, "company").send_keys("4TEST")
        address_input = driver.find_element(By.ID, "address1").send_keys("MARS")
        adress2_input = driver.find_element(By.ID, "address2").send_keys("45")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "country")))
        country_dropdown = Select(driver.find_element(By.ID, "country"))
        country_dropdown.select_by_visible_text("Canada")
        state_input = driver.find_element(By.ID, "state").send_keys("Quebec")
        city_input = driver.find_element(By.ID, "city").send_keys("La lune")
        zip_input = driver.find_element(By.ID, "zipcode").send_keys("007")
        mobile_input = driver.find_element(By.ID, "mobile_number").send_keys("0102030405060")
        create_account_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
        create_account_button.click()
        print("➡️ Clic sur 'Create Account'")
        time.sleep(2)
        assert "Account Created!" in driver.page_source
        print("➡️ Vérification du message 'Account Created'")


        try:
            continue_button = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary")))
            driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
            continue_button.click()
        except Exception as e:
            print("❌ Bouton Continue non cliquable :", e)
            driver.save_screenshot("error_continue_click.png")


        # attendre que le bouton Delete Account apparaisse
        try:
            delete_account_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Delete Account']"))
            )
            driver.execute_script("arguments[0].scrollIntoView();", delete_account_button)
            delete_account_button.click()
            time.sleep(2)

            assert "Account Deleted!" in driver.page_source
            print("✅compte supprimé avec succès.")

            #clicker sur le bouton continue
            continue_button = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary")))
            driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
            continue_button.click()
            print("✅ Clic sur 'Continue'")
        except:
            print("❌  Échec de la suppression du compte :")


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

def signup_existing_email(driver):
    try:
        driver.get("https://www.automationexercise.com/login")
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
        name_input.send_keys("Faouaz")
        email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
        email_input.send_keys("test123@faouaz.com")
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Email Address already exist!']")))
        print("✅ Signup avec email déjà existant ne fonctionne pas (comme prévu).")
    except:
            print("❌ Le test pour email déjà existant a échoué ou le comportement est incorrect.")



def main():
    driver = setup_driver()
    try:
        maximize_window = driver.maximize_window()
        test_signup_valid_email(driver)
        test_signup_invalid_email(driver)
        test_signup_empty_fields(driver)
        signup_existing_email(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
