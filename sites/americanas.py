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

    # AMERICANAS
    
    # americanas_search = americanas.get_americanas_search_url(input_search, page='1')
    # americanas_html = get_requests_code.get_response(americanas_search)

    # americanas_soup = scraper_code.Scraper(americanas_html)
    
    # americanas_product_name_tag, americanas_product_name_class = americanas.get_americanas_product_class_tag()

    # americanas_product_names_list = americanas_soup.get_text_all(americanas_product_name_tag, americanas_product_name_class)

    # americanas_old_price_tag, americanas_old_price_class = americanas.get_americanas_old_price_class_tag()
    # americanas_current_price_tag, americanas_current_price_class = americanas.get_americanas_current_price_class_tag()
    # americanas_all_prices_tag, americanas_all_prices_class = americanas.get_americanas_all_prices_class_tag()

    # americanas_all_prices_list = americanas_soup.get_soup_all(americanas_all_prices_tag, americanas_all_prices_class)
    # americanas_current_price_list = []
    # americanas_old_price_list = []

    # for i in americanas_all_prices_list:
    #     old_price_item = i.find(americanas_old_price_tag, attrs={"class":americanas_old_price_class})
    #     current_price_item = i.find(americanas_current_price_tag, attrs={"class":americanas_current_price_class})
    #     if old_price_item:
    #         americanas_old_price_list.append(old_price_item.get_text())
    #         americanas_current_price_list.append(current_price_item.get_text())
    #     else:
    #         americanas_old_price_list.append('')
    #         americanas_current_price_list.append(current_price_item.get_text())            

    # americanas_product_link_tag, americanas_product_link_class = americanas.get_americanas_product_link_class_tag()
    # americanas_product_link_list = americanas_soup.get_href_all(americanas_product_link_tag, americanas_product_link_class)

    # for i in range (15):
    #     print(americanas_product_names_list[i])
    #     print(americanas_old_price_list[i])
    #     print(americanas_current_price_list[i])
    #     print(americanas_product_link_list[i])