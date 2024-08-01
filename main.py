import base_code.scraper_code as scraper_code
import base_code.get_requests_code as get_requests_code
import sites.kabum as kabum

if __name__ == "__main__":
    input_search = input('Digite o que deseja procurar: ')

    kabum_search = kabum.get_kabum_search_url(input_search, page='1')

    kabum_html = get_requests_code.get_response(kabum_search)

    kabum_soup = scraper_code.Scraper(kabum_html)

    # Pegar a tag e a classe do componente que contém os nomes dos produtos.
    kabum_product_name_tag, kabum_product_name_class = kabum.get_kabum_product_class_tag()

    kabum_product_names_list = kabum_soup.get_text_all(kabum_product_name_tag, kabum_product_name_class)

    # Pegar a tag e a classe do componente que contém os preços.
    kabum_old_price_tag, kabum_old_price_class = kabum.get_kabum_old_price_class_tag()
    kabum_current_price_tag, kabum_current_price_class = kabum.get_kabum_current_price_class_tag()

    kabum_old_price_list = kabum_soup.get_text_all(kabum_old_price_tag, kabum_old_price_class)

    kabum_current_price_list = kabum_soup.get_text_all(kabum_current_price_tag, kabum_current_price_class)

    # Pegar a tag e a classe do componente que contém os descontos.

    kabum_discount_tag, kabum_discount_class = kabum.get_kabum_dicount_class_tag()

    kabum_discount_list = kabum_soup.get_text_all(kabum_discount_tag, kabum_discount_class)

    for i in range(10):
        print(kabum_product_names_list[i])
        print(kabum_old_price_list[i])
        print(kabum_current_price_list[i])
        print(kabum_discount_list[i])

