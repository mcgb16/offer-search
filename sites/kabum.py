kabum = {
    'initial_url': 'https://www.kabum.com.br/',
    'search': 'busca/',
    'initial_filter': '?facet_filters=',
    'page_size': '&page_size=100',
    'page_number': '&page_number=',
    'sort': '&sort=',
    'most_searched_sort': 'most_searched'
}

kabum_html_specified = {
    'product_name' : ('span','nameCard'),
    'old_price' : ('span', 'oldPriceCard'),
    'current_price' : ('span', 'priceCard'),
    'discount' : ('div', 'discountTagCard'),
    'product_link' : ('a', 'productLink')
}

def get_kabum_search_url(product, page) -> str:
    search_url = kabum['initial_url'] + kabum['search'] + product + kabum['initial_filter'] + kabum['page_size'] + kabum['page_number'] + page + kabum['sort'] + kabum['most_searched_sort']
    
    return search_url

def get_kabum_product_class_tag() -> tuple:
    return kabum_html_specified['product_name']

def get_kabum_old_price_class_tag() -> tuple:
    return kabum_html_specified['old_price']

def get_kabum_current_price_class_tag() -> tuple:
    return kabum_html_specified['current_price']

def get_kabum_dicount_class_tag() -> tuple:
    return kabum_html_specified['discount']

def get_kabum_product_link_class_tag() -> tuple:
    return kabum_html_specified['product_link']

    #KABUM

    # kabum_search = kabum.get_kabum_search_url(input_search, page='1')

    # kabum_html = get_requests_code.get_response(kabum_search)

    # kabum_soup = scraper_code.Scraper(kabum_html)

    # # Pegar a tag e a classe do componente que contém os nomes dos produtos.
    # kabum_product_name_tag, kabum_product_name_class = kabum.get_kabum_product_class_tag()

    # kabum_product_names_list = kabum_soup.get_text_all(kabum_product_name_tag, kabum_product_name_class)

    # # Pegar a tag e a classe do componente que contém os preços.
    # kabum_old_price_tag, kabum_old_price_class = kabum.get_kabum_old_price_class_tag()
    # kabum_current_price_tag, kabum_current_price_class = kabum.get_kabum_current_price_class_tag()

    # kabum_old_price_list = kabum_soup.get_text_all(kabum_old_price_tag, kabum_old_price_class)

    # kabum_current_price_list = kabum_soup.get_text_all(kabum_current_price_tag, kabum_current_price_class)

    # # Pegar a tag e a classe do componente que contém os descontos.

    # kabum_discount_tag, kabum_discount_class = kabum.get_kabum_dicount_class_tag()

    # kabum_discount_list = kabum_soup.get_text_all(kabum_discount_tag, kabum_discount_class)

    # # Pegar a tag e a classe do componente que contém os links dos produtos.

    # kabum_product_link_tag, kabum_product_link_class = kabum.get_kabum_product_link_class_tag()

    # kabum_product_link_list = kabum_soup.get_href_all(kabum_product_link_tag, kabum_product_link_class)
    # # Mesmo em situações que não tenha "old_price", ou seja, produtos que não estejam na promoção, este componente possui um valor, porém é um valor "vazio", por isso é possível sempre ter noção de quais são os valores e seus respectivos descontos sem um tratamento de dados mais detalhado.
    # for i in range(10):
    #     print(kabum_product_names_list[i])
    #     if kabum_old_price_list[i] != '':
    #         print(kabum_discount_list[i])
    #         print(kabum_old_price_list[i])
    #     print(kabum_current_price_list[i])
    #     print(kabum_product_link_list[i])