import base_code.scraper_code as scraper_code
import base_code.get_requests_code as get_requests_code
import sites.kabum as kabum
import sites.pichau as pichau

if __name__ == "__main__":
    input_search = input('Digite o que deseja procurar: ')

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

    pichau_search = pichau.get_pichau_search_url(input_search, page='1')
    pichau_html = get_requests_code.get_response(pichau_search)

    pichau_soup = scraper_code.Scraper(pichau_html)
    
    pichau_product_name_tag, pichau_product_name_class = pichau.get_pichau_product_class_tag()

    pichau_product_names_list = pichau_soup.get_text_all(pichau_product_name_tag, pichau_product_name_class)

    pichau_old_price_tag, pichau_old_price_class = pichau.get_pichau_old_price_class_tag()
    pichau_current_price_tag, pichau_current_price_class = pichau.get_pichau_current_price_class_tag()
    pichau_all_prices_tag, pichau_all_prices_class = pichau.get_pichau_all_prices_class_tag()

    pichau_all_prices_list = pichau_soup.get_soup_all(pichau_all_prices_tag, pichau_all_prices_class)
    pichau_current_price_list = []
    pichau_old_price_list = []

    for i in pichau_all_prices_list:
        old_price_item = i.find(pichau_old_price_tag, pichau_old_price_class)
        current_price_item = i.find(pichau_current_price_tag, pichau_current_price_class)
        if old_price_item:
            pichau_old_price_list.append(old_price_item.get_text())
            pichau_current_price_list.append(current_price_item.get_text())
        else:
            pichau_old_price_list.append('')
            pichau_current_price_list.append(current_price_item.get_text())            

    pichau_product_link_tag, pichau_product_link_class = pichau.get_pichau_product_link_class_tag()
    pichau_product_link_list = pichau_soup.get_href_all(pichau_product_link_tag, pichau_product_link_class)

    for i in range (36):
        print(pichau_product_names_list[i])
        print(pichau_old_price_list[i])
        print(pichau_current_price_list[i])
        print(pichau_product_link_list[i+8])

