import base_code.scraper_code as scraper_code
import base_code.get_requests_code as get_requests_code
# O SCRAPING DO ML PRECISA SER EVOLUÍDO, POIS TEM PRODUTOS QUE SÃO MOSTRADOS QUE NÃO POSSUEM PREÇOS NO SITE.

mercadolivre = {
    'initial_url': 'https://mercadolivre.com.br/',
    'search_url': 'https://lista.mercadolivre.com.br/'
}

mercadolivre_html_specified = {
    'product_name' : ('h2','ui-search-item__title','class'),
    'old_price' : ('s', 'ui-search-price__original-value','class'),
    'current_price' : ('span', 'ui-search-price__part--medium','class'),
    'all_prices' : ('div', 'ui-search-price__part-without-link','class'),
    'product_link' : ('a', 'ui-search-link__title-card','class')
}

def get_mercadolivre_soup(product, page) -> scraper_code.Scraper:
    search_url = mercadolivre['search_url'] + product
    
    mercadolivre_html = get_requests_code.get_response(search_url)

    mercadolivre_soup = scraper_code.Scraper(mercadolivre_html)
    
    return mercadolivre_soup

def get_mercadolivre_product_names(soup) -> list:
    tag_name, class_name, search_type = mercadolivre_html_specified['product_name']

    product_names = soup.get_text_all(tag_name, class_name, search_type)
    
    return product_names

# É preciso fazer uma busca dentro do próprio "all prices" para ser possível distinguir de qual produto que é o preço original, visto que este componente não existe nos produtos sem promoção.
def get_mercadolivre_prices(all_prices) -> list:
    old_price_tag_name, old_price_class_name, old_price_search_type = mercadolivre_html_specified['old_price']
    current_price_tag_name, current_price_class_name, current_price_search_type = mercadolivre_html_specified['current_price']

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

def get_mercadolivre_all_prices(soup) -> scraper_code.BeautifulSoup:
    tag_name, class_name, search_type = mercadolivre_html_specified['all_prices']

    all_prices = soup.get_soup_all(tag_name, class_name, search_type)
    
    return all_prices

def get_mercadolivre_product_links(soup) -> list:
    tag_name, class_name, search_type = mercadolivre_html_specified['product_link']

    product_links = soup.get_href_all(tag_name, class_name, search_type)
    
    return product_links