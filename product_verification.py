# main.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utilities_bot import AutomationExerciseBot

# Chemins vers Chrome et ChromeDriver
chrome_path = r'C:\ChromeDriver\chrome_133_win64\chrome-win64\chrome-win64\chrome.exe'
driver_path = r'C:\ChromeDriver\ChromeDriver_133\chromedriver-win32\chromedriver-win32\chromedriver.exe'
url = "https://www.automationexercise.com/"

# Utilisation du bot
bot = AutomationExerciseBot(chrome_path, driver_path, url)
bot.setup_driver()
bot.navigate_to_web_page()
bot.close_cookie_popup()
def test_products_page():
    try:
        wait = WebDriverWait(bot.driver, 10)
        products_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/products']")))
        products_button.click()
        WebDriverWait(bot.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title.text-center")))
        print("✅Test passed")
    except:
        print("❌Test failed")

def test_number_of_products():
    try:
        product_list = bot.driver.find_elements(By.CLASS_NAME,"product-image-wrapper")
        WebDriverWait(bot.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-image-wrapper")))
        assert len(product_list) > 0
        print("✅Product list length:", len(product_list))
    except:
         print("❌product list not found")

def test_product_information():
    try:
        wait = WebDriverWait(bot.driver, 10)
        view_firstproduct = bot.driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']")
        view_firstproduct.click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-information")))
        print("✅Product details displayed")
    except:
        print("❌Product details not displayed")

def test_product_details_content():
    try:
        product_name = bot.driver.find_element(By.XPATH, "//h2[normalize-space()='Blue Top']")
        print("✅Product name available")
        product_category = bot.driver.find_element(By.XPATH, "//p[normalize-space()='Category: Women > Tops']")
        print("✅Product category available")
        product_price = bot.driver.find_element(By.XPATH, "//span[normalize-space()='Rs. 500']")
        print("✅Product price available")
        product_availability = bot.driver.find_element(By.XPATH, "//b[normalize-space()='Availability:']")
        print("✅Product availability available")
        product_condition = bot.driver.find_element(By.XPATH, "//b[normalize-space()='Condition:']")
        print("✅Product condition available")
        product_brand = bot.driver.find_element(By.XPATH, "//b[normalize-space()='Brand:']")
        print("✅Product brand available")
    except Exception as e:
        print("❌Test failed:", e)







def main():
    try:
        bot.driver.maximize_window()
        test_products_page()
        test_number_of_products()
        test_product_information()
        test_product_details_content()
    finally:
        bot.driver.quit()

if __name__ == "__main__":
    main()




