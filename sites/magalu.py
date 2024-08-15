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

    #MAGAZINE LUIZA

    # magalu_search = magalu.get_magalu_search_url(input_search, page='1')
    # magalu_html = get_requests_code.get_response(magalu_search)

    # magalu_soup = scraper_code.Scraper(magalu_html)
    
    # magalu_product_name_tag, magalu_product_name_testid = magalu.get_magalu_product_testid_tag()

    # magalu_product_names_list = magalu_soup.get_text_all_data_testid(magalu_product_name_tag, magalu_product_name_testid)

    # magalu_old_price_tag, magalu_old_price_testid = magalu.get_magalu_old_price_testid_tag()
    # magalu_current_price_tag, magalu_current_price_testid = magalu.get_magalu_current_price_testid_tag()
    # magalu_all_prices_tag, magalu_all_prices_testid = magalu.get_magalu_all_prices_testid_tag()

    # magalu_all_prices_list = magalu_soup.get_soup_all_data_testid(magalu_all_prices_tag, magalu_all_prices_testid)
    # magalu_current_price_list = []
    # magalu_old_price_list = []

    # for i in magalu_all_prices_list:
    #     old_price_item = i.find(magalu_old_price_tag, attrs={"data-testid":magalu_old_price_testid})
    #     current_price_item = i.find(magalu_current_price_tag, attrs={"data-testid":magalu_current_price_testid})
    #     if old_price_item:
    #         magalu_old_price_list.append(old_price_item.get_text())
    #         magalu_current_price_list.append(current_price_item.get_text())
    #     else:
    #         magalu_old_price_list.append('')
    #         magalu_current_price_list.append(current_price_item.get_text())            

    # magalu_product_link_tag, magalu_product_link_testid = magalu.get_magalu_product_link_testid_tag()
    # magalu_product_link_list = magalu_soup.get_href_all_data_testid(magalu_product_link_tag, magalu_product_link_testid)

    # for i in range (36):
    #     print(magalu_product_names_list[i])
    #     print(magalu_old_price_list[i])
    #     print(magalu_current_price_list[i])
    #     print(magalu_product_link_list[i])