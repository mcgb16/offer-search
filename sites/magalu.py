magalu = {
    'initial_url': 'https://www.magazineluiza.com.br/',
    'search': 'busca/',
    'page_number': '/?page='
}

magalu_html_specified = {
    'product_name' : ('h2','product-title'),
    'old_price' : ('p', 'price-original'),
    'current_price' : ('p', 'price-value'),
    'all_prices' : ('div', 'price-default'),
    'product_link' : ('a', 'product-card-container')
}

def get_magalu_search_url(product, page) -> str:
    search_url = magalu['initial_url'] + magalu['search'] + product + magalu['page_number'] + page
    return search_url

def get_magalu_product_testid_tag() -> tuple:
    return magalu_html_specified['product_name']

def get_magalu_old_price_testid_tag() -> tuple:
    return magalu_html_specified['old_price']

def get_magalu_current_price_testid_tag() -> tuple:
    return magalu_html_specified['current_price']

def get_magalu_all_prices_testid_tag() -> tuple:
    return magalu_html_specified['all_prices']

def get_magalu_product_link_testid_tag() -> tuple:
    return magalu_html_specified['product_link']