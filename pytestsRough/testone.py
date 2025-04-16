from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()

# Set preferences to block all cookies
prefs = {
    "profile.default_content_setting_values.cookies": 2,  # 2 = Block all cookies
    "profile.block_third_party_cookies": True,
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the browser with options
driver = webdriver.Chrome(options=chrome_options)

# Open a website
driver.get("https://www.google.com")

# Verify cookies are blocked
cookies = driver.get_cookies()
print("Cookies:", cookies)  # Should be empty

# Close the browser
driver.quit()