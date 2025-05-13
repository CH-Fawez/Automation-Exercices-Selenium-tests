# main.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

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

def search_product():
    try:
        wait = WebDriverWait(bot.driver, 10)

        # Rechercher "tshirt"
        search_bar = bot.driver.find_element(By.ID, "search_product")
        search_bar.send_keys("tshirt")
        search_button = bot.driver.find_element(By.ID, "submit_search")
        search_button.click()

        # Attente du texte "Searched Products"
        wait.until(EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Searched Products']")))
        print("✅ Searched Products section is visible.")

        # Récupérer tous les produits affichés après la recherche
        product_titles = bot.driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']/p")

        if not product_titles:
            print("❌ No products found.")
            return

        tshirt_pattern = re.compile(r"t[\s-]?shirt", re.IGNORECASE)
        # Vérifier que chaque produit contient 'tshirt'
        for product in product_titles:
            text = product.text.lower()
            assert "shirt" in text, f"❌ Product does not contain 'tshirt': {text}"

        print(f"✅ All {len(product_titles)} products contain 'tshirt'.")
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")



def main():
    try:
        bot.driver.maximize_window()
        test_products_page()
        search_product()
        print("✅All tests passed.")

    finally:
        bot.driver.quit()

if __name__ == "__main__":
    main()


