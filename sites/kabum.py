import base_code.scraper_code as scraper_code
import base_code.get_requests_code as get_requests_code

kabum = {
    'initial_url': 'https://www.kabum.com.br/',
    'search': 'busca/',
    'initial_filter': '?facet_filters=',
    'page_size': '&page_size=100',
    'page_number': '&page_number=',
    'sort': '&sort=',
    'most_searched_sort': 'most_searched'
}

kabum_html_specified = {
    'product_name' : ('span','nameCard','class'),
    'old_price' : ('span', 'oldPriceCard','class'),
    'current_price' : ('span', 'priceCard','class'),
    'discount' : ('div', 'discountTagCard','class'),
    'product_link' : ('a', 'productLink','class')
}

def get_kabum_soup(product, page) -> scraper_code.Scraper:
    search_url = kabum['initial_url'] + kabum['search'] + product + kabum['initial_filter'] + kabum['page_size'] + kabum['page_number'] + page + kabum['sort'] + kabum['most_searched_sort']
    
    kbm_html = get_requests_code.get_response(search_url)

    kbm_soup = scraper_code.Scraper(kbm_html)

    return kbm_soup

def get_kabum_product_names(soup) -> tuple:
    tag_name, class_name, search_type = kabum_html_specified['product_name']

    product_names = soup.get_text_all(tag_name, class_name, search_type)
    
    return product_names

def get_kabum_old_prices(soup) -> tuple:
    tag_name, class_name, search_type = kabum_html_specified['old_price']

    kabum_old_prices = soup.get_text_all(tag_name, class_name, search_type)
    
    return kabum_old_prices

def get_kabum_current_prices(soup) -> tuple:
    tag_name, class_name, search_type = kabum_html_specified['current_price']

    kabum_current_prices = soup.get_text_all(tag_name, class_name, search_type)
    
    return kabum_current_prices

def get_kabum_discounts(soup) -> tuple:
    tag_name, class_name, search_type = kabum_html_specified['discount']

    kabum_discounts = soup.get_text_all(tag_name, class_name, search_type)
    
    return kabum_discounts

def get_kabum_product_links(soup) -> tuple:
    tag_name, class_name, search_type = kabum_html_specified['product_link']

    kabum_product_links = soup.get_href_all(tag_name, class_name, search_type)
    
    return kabum_product_links

# Mesmo em situações que não tenha "old_price", ou seja, produtos que não estejam na promoção, este componente possui um valor, porém é um valor "vazio", por isso é possível sempre ter noção de quais são os valores e seus respectivos descontos sem um tratamento de dados mais detalhado.