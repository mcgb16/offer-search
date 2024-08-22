from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from playwright.sync_api import sync_playwright
import time

# chrome_options = Options()
# # No site da americanas não é possível utilizar o headless
# chrome_options.add_argument('--headless')
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# driver = webdriver.Chrome(options=chrome_options)

# def get_response(url) -> str:

#     driver.get(url)

#     html = driver.page_source
#     driver.quit()

#     return html

def get_response(url) -> str:
    with sync_playwright() as p:
        if 'https://www.americanas.com.br/' in url:
            browser = p.firefox.launch(headless=True)
        else:
            browser = p.chromium.launch(headless=True)
        
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        page = context.new_page()

        page.goto(url)
        time.sleep(2)
        
        html = page.content()

        browser.close()

    return html
