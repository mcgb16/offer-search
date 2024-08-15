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

    #PICHAU

    # pichau_search = pichau.get_pichau_search_url(input_search, page='1')
    # pichau_html = get_requests_code.get_response(pichau_search)

    # pichau_soup = scraper_code.Scraper(pichau_html)
    
    # pichau_product_name_tag, pichau_product_name_class = pichau.get_pichau_product_class_tag()

    # pichau_product_names_list = pichau_soup.get_text_all(pichau_product_name_tag, pichau_product_name_class)

    # pichau_old_price_tag, pichau_old_price_class = pichau.get_pichau_old_price_class_tag()
    # pichau_current_price_tag, pichau_current_price_class = pichau.get_pichau_current_price_class_tag()
    # pichau_all_prices_tag, pichau_all_prices_class = pichau.get_pichau_all_prices_class_tag()

    # pichau_all_prices_list = pichau_soup.get_soup_all(pichau_all_prices_tag, pichau_all_prices_class)
    # pichau_current_price_list = []
    # pichau_old_price_list = []

    # for i in pichau_all_prices_list:
    #     old_price_item = i.find(pichau_old_price_tag, pichau_old_price_class)
    #     current_price_item = i.find(pichau_current_price_tag, pichau_current_price_class)
    #     if old_price_item:
    #         pichau_old_price_list.append(old_price_item.get_text())
    #         pichau_current_price_list.append(current_price_item.get_text())
    #     else:
    #         pichau_old_price_list.append('')
    #         pichau_current_price_list.append(current_price_item.get_text())            

    # pichau_product_link_tag, pichau_product_link_class = pichau.get_pichau_product_link_class_tag()
    # pichau_product_link_list = pichau_soup.get_href_all(pichau_product_link_tag, pichau_product_link_class)

    # for i in range (36):
    #     print(pichau_product_names_list[i])
    #     print(pichau_old_price_list[i])
    #     print(pichau_current_price_list[i])
    #     print(pichau_product_link_list[i+8])