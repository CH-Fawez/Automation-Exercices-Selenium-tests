from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


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
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]/p')))
        cookie_button.click()
    except:
        print("Cookie button not found or already dismissed.")


def navigate_to_web_page(driver, url):
    driver.get(url)
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Home']")))
    print("✅Web page loaded successfully")
    return driver

def test_products_page(driver):
    try:
        wait = WebDriverWait(driver, 10)
        products_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/products']")))
        products_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title.text-center")))
        print("✅Test passed")
    except:
        print("❌Test failed")

def add_to_cart(driver):
    try:
        #add first item to cart
        first_item_add = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-product-id='1']")))
        first_item_add.click()
        assert "Your product has been added to cart." in driver.page_source, "Failed to add item to cart"
        print("✅Test add to card passed")
    except:
        print("❌Test add to cart failed")

def continue_shopping(driver):
    try:
        continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")))
        continue_button.click()
        assert "All Products" in driver.page_source, "Failed to navigate to continue shopping page"
        print("✅Test continue shopping passed")
    except:
        print("❌Test continue shopping failed")

def add_to_cart2(driver):
    try:
        #add first item to cart
        second_item_add = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-product-id='2']")))
        second_item_add.click()
        assert "Your product has been added to cart." in driver.page_source, "Failed to add item to cart"
        view_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()
        assert "Shopping Cart" in driver.page_source, "Failed to navigate to cart page"
        print("✅Test add to card  seconced item passed")
    except:
        print("❌Test add to cart failed seconde item")

# Verify both products are added to Cart
def verify_cart(driver):
    try:
        cart_items = driver.find_elements(By.XPATH, "//tr[contains(@id, 'product')]")
        assert len(cart_items) == 2, "Failed to verify cart items"
        print("✅Test cart passed, products in cart = ",len(cart_items))
    except:
        print("❌Test cart failed, products not in cart")

def main():
    driver = setup_driver()

    try:

        # Navigate to the web page
        driver = navigate_to_web_page(driver, url)
        close_cookie_popup(driver)

        # Test the products page
        test_products_page(driver)

        # Add an item to the cart
        add_to_cart(driver)
        # Continue shopping page
        continue_shopping(driver)
        # Add another item to the cart
        add_to_cart2(driver)

        # Verify the items are added to the cart
        verify_cart(driver)
        print("✅All tests passed!✅")
    finally:
        # Close the driver
        driver.quit()


if __name__ == "__main__":
    main()









