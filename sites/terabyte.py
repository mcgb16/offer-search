import base_code.scraper_code as scraper_code
import base_code.get_requests_code as get_requests_code

terabyte = {
    'initial_url': 'https://www.terabyteshop.com.br/',
    'search': 'busca?str=',
}

terabyte_html_specified = {
    'product_name' : ('a','prod-name', 'class'),
    'old_price' : ('div', 'prod-old-price', 'class'),
    'current_price' : ('div', 'prod-new-price', 'class'),
    'all_prices' : ('div', 'commerce_columns_item_info', 'class'),
    'product_link' : ('a', 'prod-name', 'class')
}

def get_terabyte_soup(product, page) -> scraper_code.Scraper:
    search_url = terabyte['initial_url'] + terabyte['search'] + product
    
    terabyte_html = get_requests_code.get_response(search_url)

    terabyte_soup = scraper_code.Scraper(terabyte_html)
    
    return terabyte_soup

def get_terabyte_product_names(soup) -> list:
    tag_name, class_name, search_type = terabyte_html_specified['product_name']

    product_names = soup.get_text_all(tag_name, class_name, search_type)
    
    return product_names

# É preciso fazer uma busca dentro do próprio "all prices" para ser possível distinguir de qual produto que é o preço original, visto que este componente não existe nos produtos sem promoção.
def get_terabyte_prices(all_prices) -> list:
    old_price_tag_name, old_price_class_name, old_price_search_type = terabyte_html_specified['old_price']
    current_price_tag_name, current_price_class_name, current_price_search_type = terabyte_html_specified['current_price']

    old_prices = []
    current_prices = []

    for i in all_prices:

        old_price_item = i.find(old_price_tag_name, {old_price_search_type: old_price_class_name})
        current_price_item = i.find(current_price_tag_name, {current_price_search_type: current_price_class_name})
        if old_price_item:
            old_prices.append(old_price_item.get_text())
            current_prices.append(current_price_item.get_text())
        else:
            old_prices.append('')
            current_prices.append(current_price_item.get_text())
    
    return old_prices, current_prices

def get_terabyte_all_prices(soup) -> scraper_code.BeautifulSoup:
    tag_name, class_name, search_type = terabyte_html_specified['all_prices']

    all_prices = soup.get_soup_all(tag_name, class_name, search_type)
    
    return all_prices

def get_terabyte_product_links(soup) -> list:
    tag_name, class_name, search_type = terabyte_html_specified['product_link']

    product_links = soup.get_href_all(tag_name, class_name, search_type)
    
    return product_links

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