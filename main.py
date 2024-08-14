import base_code.scraper_code as scraper_code
import base_code.get_requests_code as get_requests_code
import sites.kabum as kabum
import sites.pichau as pichau
import sites.terabyte as terabyte
import sites.magalu as magalu
import sites.americanas as americanas
import sites.mercado_livre as mercadolivre

if __name__ == "__main__":
    input_search = input('Digite o que deseja procurar: ')
    
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

    # MERCADO LIVRE
    
    mercadolivre_search = mercadolivre.get_mercadolivre_search_url(input_search, page='1')
    mercadolivre_html = get_requests_code.get_response(mercadolivre_search)

    mercadolivre_soup = scraper_code.Scraper(mercadolivre_html)
    
    mercadolivre_product_name_tag, mercadolivre_product_name_class = mercadolivre.get_mercadolivre_product_class_tag()

    mercadolivre_product_names_list = mercadolivre_soup.get_text_all(mercadolivre_product_name_tag, mercadolivre_product_name_class)

    mercadolivre_old_price_tag, mercadolivre_old_price_class = mercadolivre.get_mercadolivre_old_price_class_tag()
    mercadolivre_current_price_tag, mercadolivre_current_price_class = mercadolivre.get_mercadolivre_current_price_class_tag()
    mercadolivre_all_prices_tag, mercadolivre_all_prices_class = mercadolivre.get_mercadolivre_all_prices_class_tag()

    mercadolivre_all_prices_list = mercadolivre_soup.get_soup_all(mercadolivre_all_prices_tag, mercadolivre_all_prices_class)
    mercadolivre_current_price_list = []
    mercadolivre_old_price_list = []

    for i in mercadolivre_all_prices_list:
        old_price_item = i.find(mercadolivre_old_price_tag, attrs={"class":mercadolivre_old_price_class})
        current_price_item = i.find(mercadolivre_current_price_tag, attrs={"class":mercadolivre_current_price_class})
        if old_price_item:
            mercadolivre_old_price_list.append(old_price_item.get_text())
            mercadolivre_current_price_list.append(current_price_item.get_text())
        else:
            mercadolivre_old_price_list.append('')
            mercadolivre_current_price_list.append(current_price_item.get_text())            

    mercadolivre_product_link_tag, mercadolivre_product_link_class = mercadolivre.get_mercadolivre_product_link_class_tag()
    mercadolivre_product_link_list = mercadolivre_soup.get_href_all(mercadolivre_product_link_tag, mercadolivre_product_link_class)

    for i in range (15):
        print(mercadolivre_product_names_list[i])
        print(mercadolivre_old_price_list[i])
        print(mercadolivre_current_price_list[i])
        print(mercadolivre_product_link_list[i])