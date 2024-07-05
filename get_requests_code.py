from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

def get_response(url) -> str:

    driver.get(url)

    html = driver.page_source
    driver.quit()

    return html