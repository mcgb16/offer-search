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
    'product_name' : ('span','nameCard'),
    'old_price' : ('span', 'oldPriceCard'),
    'current_price' : ('span', 'priceCard'),
    'discount' : ('div', 'discountTagCard')
}

def get_kabum_search_url(product, page) -> str:
    search_url = kabum['initial_url'] + kabum['search'] + product + kabum['initial_filter'] + kabum['page_size'] + kabum['page_number'] + page + kabum['sort'] + kabum['most_searched_sort']
    
    return search_url

def get_kabum_product_class_tag() -> tuple:
    return kabum_html_specified['product_name']

def get_kabum_old_price_class_tag() -> tuple:
    return kabum_html_specified['old_price']

def get_kabum_current_price_class_tag() -> tuple:
    return kabum_html_specified['current_price']

def get_kabum_dicount_class_tag() -> tuple:
    return kabum_html_specified['discount']