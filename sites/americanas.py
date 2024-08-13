americanas = {
    'initial_url': 'https://www.americanas.com.br/',
    'search': 'busca/',
    'page_number': '?page='
}

americanas_html_specified = {
    'product_name' : ('h3','product-name'),
    'old_price' : ('span', 'sales-price'),
    'current_price' : ('span', 'list-price'),
    'all_prices' : ('div', 'price-info'),
    'product_link' : ('a', 'inStockCard__Link-sc-1ngt5zo-1')
}

def get_americanas_search_url(product, page) -> str:
    search_url = americanas['initial_url'] + americanas['search'] + product + americanas['page_number'] + page
    return search_url

def get_americanas_product_class_tag() -> tuple:
    return americanas_html_specified['product_name']

def get_americanas_old_price_class_tag() -> tuple:
    return americanas_html_specified['old_price']

def get_americanas_current_price_class_tag() -> tuple:
    return americanas_html_specified['current_price']

def get_americanas_all_prices_class_tag() -> tuple:
    return americanas_html_specified['all_prices']

def get_americanas_product_link_class_tag() -> tuple:
    return americanas_html_specified['product_link']