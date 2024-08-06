pichau = {
    'initial_url': 'https://www.pichau.com.br/',
    'search': 'search?q=',
    'page_number': '&page=',
    'sort': '&sort='
}

pichau_html_specified = {
    'product_name' : ('h2','MuiTypography-h6'),
    'old_price' : ('span', 'jss303'),
    'current_price' : ('div', 'jss277'),
    'all_prices' : ('div', 'jss289'),
    'product_link' : ('a', 'jss188')
}

def get_pichau_search_url(product, page) -> str:
    search_url = pichau['initial_url'] + pichau['search'] + product
    return search_url

def get_pichau_product_class_tag() -> tuple:
    return pichau_html_specified['product_name']