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

    # MERCADO LIVRE
    
    # mercadolivre_search = mercadolivre.get_mercadolivre_search_url(input_search, page='1')
    # mercadolivre_html = get_requests_code.get_response(mercadolivre_search)

    # mercadolivre_soup = scraper_code.Scraper(mercadolivre_html)
    
    # mercadolivre_product_name_tag, mercadolivre_product_name_class = mercadolivre.get_mercadolivre_product_class_tag()

    # mercadolivre_product_names_list = mercadolivre_soup.get_text_all(mercadolivre_product_name_tag, mercadolivre_product_name_class)

    # mercadolivre_old_price_tag, mercadolivre_old_price_class = mercadolivre.get_mercadolivre_old_price_class_tag()
    # mercadolivre_current_price_tag, mercadolivre_current_price_class = mercadolivre.get_mercadolivre_current_price_class_tag()
    # mercadolivre_all_prices_tag, mercadolivre_all_prices_class = mercadolivre.get_mercadolivre_all_prices_class_tag()

    # mercadolivre_all_prices_list = mercadolivre_soup.get_soup_all(mercadolivre_all_prices_tag, mercadolivre_all_prices_class)
    # mercadolivre_current_price_list = []
    # mercadolivre_old_price_list = []

    # for i in mercadolivre_all_prices_list:
    #     old_price_item = i.find(mercadolivre_old_price_tag, attrs={"class":mercadolivre_old_price_class})
    #     current_price_item = i.find(mercadolivre_current_price_tag, attrs={"class":mercadolivre_current_price_class})
    #     if old_price_item:
    #         mercadolivre_old_price_list.append(old_price_item.get_text())
    #         mercadolivre_current_price_list.append(current_price_item.get_text())
    #     else:
    #         mercadolivre_old_price_list.append('')
    #         mercadolivre_current_price_list.append(current_price_item.get_text())            

    # mercadolivre_product_link_tag, mercadolivre_product_link_class = mercadolivre.get_mercadolivre_product_link_class_tag()
    # mercadolivre_product_link_list = mercadolivre_soup.get_href_all(mercadolivre_product_link_tag, mercadolivre_product_link_class)

    # for i in range (15):
    #     print(mercadolivre_product_names_list[i])
    #     print(mercadolivre_old_price_list[i])
    #     print(mercadolivre_current_price_list[i])
    #     print(mercadolivre_product_link_list[i])