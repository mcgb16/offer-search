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

    #TERABYTE

    # terabyte_search = terabyte.get_terabyte_search_url(input_search, page='1')
    # terabyte_html = get_requests_code.get_response(terabyte_search)

    # terabyte_soup = scraper_code.Scraper(terabyte_html)
    
    # terabyte_product_name_tag, terabyte_product_name_class = terabyte.get_terabyte_product_class_tag()

    # terabyte_product_names_list = terabyte_soup.get_text_all(terabyte_product_name_tag, terabyte_product_name_class)

    # terabyte_old_price_tag, terabyte_old_price_class = terabyte.get_terabyte_old_price_class_tag()
    # terabyte_current_price_tag, terabyte_current_price_class = terabyte.get_terabyte_current_price_class_tag()
    # terabyte_all_prices_tag, terabyte_all_prices_class = terabyte.get_terabyte_all_prices_class_tag()

    # terabyte_all_prices_list = terabyte_soup.get_soup_all(terabyte_all_prices_tag, terabyte_all_prices_class)
    # terabyte_current_price_list = []
    # terabyte_old_price_list = []

    # for i in terabyte_all_prices_list:
    #     old_price_item = i.find(terabyte_old_price_tag, terabyte_old_price_class)
    #     current_price_item = i.find(terabyte_current_price_tag, terabyte_current_price_class)
    #     if old_price_item:
    #         terabyte_old_price_list.append(old_price_item.get_text())
    #         terabyte_current_price_list.append(current_price_item.get_text())
    #     else:
    #         terabyte_old_price_list.append('')
    #         terabyte_current_price_list.append(current_price_item.get_text())            

    # terabyte_product_link_tag, terabyte_product_link_class = terabyte.get_terabyte_product_link_class_tag()
    # terabyte_product_link_list = terabyte_soup.get_href_all(terabyte_product_link_tag, terabyte_product_link_class)

    # for i in range (36):
    #     print(terabyte_product_names_list[i])
    #     print(terabyte_old_price_list[i])
    #     print(terabyte_current_price_list[i])
    #     print(terabyte_product_link_list[i])