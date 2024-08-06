pichau = {
    'initial_url': 'https://www.pichau.com.br/',
    'search': 'search?q=',
    'page_number': '&page=',
    'sort': '&sort='
}

pichau_html_specified = {
    'product_name' : ('h2','MuiTypography-h6'),
    'old_price' : ('span', 'jss129'),
    'current_price' : ('div', 'jss103'),
    'all_prices' : ('div', 'jss115'),
    'product_link' : ('a', 'jss16')
}

def get_pichau_search_url(product, page) -> str:
    search_url = pichau['initial_url'] + pichau['search'] + product
    return search_url

def get_pichau_product_class_tag() -> tuple:
    return pichau_html_specified['product_name']

def get_pichau_old_price_class_tag() -> tuple:
    return pichau_html_specified['old_price']

def get_pichau_current_price_class_tag() -> tuple:
    return pichau_html_specified['current_price']

def get_pichau_all_prices_class_tag() -> tuple:
    return pichau_html_specified['all_prices']

def get_pichau_product_link_class_tag() -> tuple:
    return pichau_html_specified['product_link']