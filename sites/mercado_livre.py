mercadolivre = {
    'initial_url': 'https://mercadolivre.com.br/',
    'search_url': 'https://lista.mercadolivre.com.br/'
}

mercadolivre_html_specified = {
    'product_name' : ('h2','ui-search-item__title'),
    'old_price' : ('s', 'ui-search-price__original-value'),
    'current_price' : ('span', 'ui-search-price__part--medium'),
    'all_prices' : ('div', 'ui-search-price__part-without-link'),
    'product_link' : ('a', 'ui-search-link__title-card')
}

def get_mercadolivre_search_url(product, page) -> str:
    search_url = mercadolivre['search_url'] + product
    return search_url

def get_mercadolivre_product_class_tag() -> tuple:
    return mercadolivre_html_specified['product_name']

def get_mercadolivre_old_price_class_tag() -> tuple:
    return mercadolivre_html_specified['old_price']

def get_mercadolivre_current_price_class_tag() -> tuple:
    return mercadolivre_html_specified['current_price']

def get_mercadolivre_all_prices_class_tag() -> tuple:
    return mercadolivre_html_specified['all_prices']

def get_mercadolivre_product_link_class_tag() -> tuple:
    return mercadolivre_html_specified['product_link']