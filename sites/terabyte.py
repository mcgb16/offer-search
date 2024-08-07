terabyte = {
    'initial_url': 'https://www.terabyteshop.com.br/',
    'search': 'busca?str=',
}

terabyte_html_specified = {
    'product_name' : ('a','prod-name'),
    'old_price' : ('div', 'prod-old-price'),
    'current_price' : ('div', 'prod-new-price'),
    'all_prices' : ('div', 'commerce_columns_item_info'),
    'product_link' : ('a', 'prod-name')
}

def get_terabyte_search_url(product, page) -> str:
    search_url = terabyte['initial_url'] + terabyte['search'] + product
    return search_url

def get_terabyte_product_class_tag() -> tuple:
    return terabyte_html_specified['product_name']

def get_terabyte_old_price_class_tag() -> tuple:
    return terabyte_html_specified['old_price']

def get_terabyte_current_price_class_tag() -> tuple:
    return terabyte_html_specified['current_price']

def get_terabyte_all_prices_class_tag() -> tuple:
    return terabyte_html_specified['all_prices']

def get_terabyte_product_link_class_tag() -> tuple:
    return terabyte_html_specified['product_link']