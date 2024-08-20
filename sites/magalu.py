import base_code.scraper_code as scraper_code
import base_code.get_requests_code as get_requests_code

magalu = {
    'initial_url': 'https://www.magazineluiza.com.br/',
    'search': 'busca/',
    'page_number': '/?page='
}

magalu_html_specified = {
    'product_name' : ('h2','product-title', 'data-testid'),
    'old_price' : ('p', 'price-original', 'data-testid'),
    'current_price' : ('p', 'price-value', 'data-testid'),
    'all_prices' : ('div', 'price-default', 'data-testid'),
    'product_link' : ('a', 'product-card-container', 'data-testid')
}

def get_magalu_soup(product, page) -> scraper_code.Scraper:
    search_url = magalu['initial_url'] + magalu['search'] + product + magalu['page_number'] + page
    
    magalu_html = get_requests_code.get_response(search_url)

    magalu_soup = scraper_code.Scraper(magalu_html)
    
    return magalu_soup

def get_magalu_product_names(soup) -> list:
    tag_name, class_name, search_type = magalu_html_specified['product_name']

    product_names = soup.get_text_all(tag_name, class_name, search_type)
    
    return product_names

# É preciso fazer uma busca dentro do próprio "all prices" para ser possível distinguir de qual produto que é o preço original, visto que este componente não existe nos produtos sem promoção.
def get_magalu_prices(all_prices) -> list:
    old_price_tag_name, old_price_class_name, old_price_search_type = magalu_html_specified['old_price']
    current_price_tag_name, current_price_class_name, current_price_search_type = magalu_html_specified['current_price']

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

def get_magalu_all_prices(soup) -> scraper_code.BeautifulSoup:
    tag_name, class_name, search_type = magalu_html_specified['all_prices']

    all_prices = soup.get_soup_all(tag_name, class_name, search_type)
    
    return all_prices

def get_magalu_product_links(soup) -> list:
    tag_name, class_name, search_type = magalu_html_specified['product_link']

    product_links = soup.get_href_all(tag_name, class_name, search_type)
    
    return product_links            