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

def subscribe_to_newsletter_home_page(driver):
    try:
        wait = WebDriverWait(driver, 10)
        #find the subcscription panel
        subscribe_panel= driver.find_element(By.ID, "susbscribe_email").send_keys("your_email@example.com")
        submit_button = driver.find_element(By.ID, "subscribe").click()
        assert "You have been successfully subscribed!" in driver.page_source, "Failed to subscribe to newsletter"
        print("✅Newsletter subscription successful from home page")
    except Exception as e:
        print("❌Failed to subscribe to newsletter from home page")

def subscribe_to_newsletter_cart_page(driver):
    try:
        wait = WebDriverWait(driver, 10)
        cart_button = driver.find_element(By.CSS_SELECTOR, "header[id='header'] li:nth-child(3) a:nth-child(1)")
        cart_button.click()
        subscribe_panel= driver.find_element(By.ID, "susbscribe_email").send_keys("your_email@example.com")
        submit_button = driver.find_element(By.ID, "subscribe").click()

        assert "You have been successfully subscribed!" in driver.page_source, "Failed to subscribe to newsletter"
        print("✅Newsletter subscription successful from cart page")
    except Exception as e:
        print("❌ Failed to subscribe to newsletter from cart page")

def main():
    driver = setup_driver()

    try:
        navigate_to_web_page(driver, url)
        driver.maximize_window()
        close_cookie_popup(driver)
        # Subscribe to the newsletter from the home page
        subscribe_to_newsletter_home_page(driver)

        # Subscribe to the newsletter from the cart page
        subscribe_to_newsletter_cart_page(driver)

    finally:
        # Close the Chrome driver
        driver.quit()

if __name__ == "__main__":
    main()
