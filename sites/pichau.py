import base_code.scraper_code as scraper_code
import base_code.get_requests_code as get_requests_code

pichau = {
    'initial_url': 'https://www.pichau.com.br/',
    'search': 'search?q=',
    'page_number': '&page=',
    'sort': '&sort='
}

pichau_html_specified = {
    'product_name' : ('h2','MuiTypography-h6','class'),
    'old_price' : ('span', 'jss129','class'),
    'current_price' : ('div', 'jss103','class'),
    'all_prices' : ('div', 'jss115','class'),
    'product_link' : ('a', 'jss16','class')
}

def get_pichau_soup(product, page) -> scraper_code.Scraper:
    search_url = pichau['initial_url'] + pichau['search'] + product
    
    pichau_html = get_requests_code.get_response(search_url)

    pichau_soup = scraper_code.Scraper(pichau_html)
    
    return pichau_soup

def get_pichau_product_names(soup) -> list:
    tag_name, class_name, search_type = pichau_html_specified['product_name']

    product_names = soup.get_text_all(tag_name, class_name, search_type)
    
    return product_names

# É preciso fazer uma busca dentro do próprio "all prices" para ser possível distinguir de qual produto que é o preço original, visto que este componente não existe nos produtos sem promoção.
def get_pichau_prices(all_prices) -> list:
    old_price_tag_name, old_price_class_name, old_price_search_type = pichau_html_specified['old_price']
    current_price_tag_name, current_price_class_name, current_price_search_type = pichau_html_specified['current_price']

    old_prices = []
    current_prices = []

    for i in all_prices:

        old_price_item = i.find(old_price_tag_name, {old_price_search_type: old_price_class_name})
        current_price_item = i.find(current_price_tag_name, {current_price_search_type: current_price_class_name})
        if old_price_item:
            old_prices.append(old_price_item.get_text())
            current_prices.append(current_price_item.get_text())
        else:
            old_prices.append('')
            current_prices.append(current_price_item.get_text())
    
    return old_prices, current_prices

def get_pichau_all_prices(soup) -> scraper_code.BeautifulSoup:
    tag_name, class_name, search_type = pichau_html_specified['all_prices']

    all_prices = soup.get_soup_all(tag_name, class_name, search_type)
    
    return all_prices

def get_pichau_product_links(soup) -> list:
    tag_name, class_name, search_type = pichau_html_specified['product_link']

    product_links = soup.get_href_all(tag_name, class_name, search_type)
    
    return product_links