import base_code.scraper_code as scraper_code
import base_code.get_requests_code as get_requests_code

americanas = {
    'initial_url': 'https://www.americanas.com.br/',
    'search': 'busca/',
    'page_number': '?page='
}

americanas_html_specified = {
    'product_name' : ('h3','product-name', 'class'),
    'old_price' : ('span', 'sales-price', 'class'),
    'current_price' : ('span', 'list-price', 'class'),
    'all_prices' : ('div', 'price-info', 'class'),
    'product_link' : ('a', 'inStockCard__Link-sc-1ngt5zo-1', 'class')
}

def get_americanas_soup(product, page) -> scraper_code.Scraper:
    search_url = americanas['initial_url'] + americanas['search'] + product + americanas['page_number'] + page
    americanas_html = get_requests_code.get_response(search_url)

    americanas_soup = scraper_code.Scraper(americanas_html)
    
    return americanas_soup

def get_americanas_product_names(soup) -> list:
    tag_name, class_name, search_type = americanas_html_specified['product_name']

    product_names = soup.get_text_all(tag_name, class_name, search_type)
    
    return product_names

# É preciso fazer uma busca dentro do próprio "all prices" para ser possível distinguir de qual produto que é o preço original, visto que este componente não existe nos produtos sem promoção.
def get_americanas_prices(all_prices) -> list:
    old_price_tag_name, old_price_class_name, old_price_search_type = americanas_html_specified['old_price']
    current_price_tag_name, current_price_class_name, current_price_search_type = americanas_html_specified['current_price']

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

def get_americanas_all_prices(soup) -> scraper_code.BeautifulSoup:
    tag_name, class_name, search_type = americanas_html_specified['all_prices']

    all_prices = soup.get_soup_all(tag_name, class_name, search_type)
    
    return all_prices

def get_americanas_product_links(soup) -> list:
    tag_name, class_name, search_type = americanas_html_specified['product_link']

    product_links = soup.get_href_all(tag_name, class_name, search_type)
    
    return product_links