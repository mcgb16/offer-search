import sites
import kabum

if __name__ == "__main__":
    input_search = input('Digite o que deseja procurar: ')

    kabum_search = kabum.get_kabum_search_url(input_search, page='1')
    
    kabum_html = sites.get_html(kabum_search)
    kabum_soup = sites.create_scraper(kabum_html)

    # Pegar a tag e a classe do componente que contém os nomes dos produtos.
    kabum_product_name_tag, kabum_product_name_class = kabum.get_kabum_product_class_tag()

    kabum_product_names_list = sites.get_products_name(kabum_soup, 
    kabum_product_name_tag, kabum_product_name_class)

    for i in kabum_product_names_list:
        print(i)

    # Pegar a tag e a classe do componente que contém 