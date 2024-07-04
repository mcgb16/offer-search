import scraper_code
import get_requests_code

def get_html(search) -> str:
    html_response = get_requests_code.get_response(search)
    return html_response

def create_scraper(html) -> scraper_code.BeautifulSoup:
    soup = scraper_code.Scraper(html)
    return soup

def get_products_name(soup, tag, class_name) -> list:
    products_name = soup.get_text_all(tag, class_name)

    return products_name