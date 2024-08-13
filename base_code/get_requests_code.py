from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# No site da americanas não é possível utilizar o headless
chrome_options.add_argument('--headless')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

def get_response(url) -> str:

    driver.get(url)

    html = driver.page_source
    driver.quit()

    return html