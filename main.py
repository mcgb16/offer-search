import scraper_code
import get_requests_code
import kabum

if __name__ == "__main__":
    input_search = input('Digite o que deseja procurar: ')

    kabum_search = kabum.get_kabum_search_url(input_search, page='1')
    
    kabum_html = get_requests_code.get_response(kabum_search)
    kabum_soup = scraper_code.Scraper(kabum_html)

    # Pegar a tag e a classe do componente que contém os nomes dos produtos.
    kabum_product_name_tag, kabum_product_name_class = kabum.get_kabum_product_class_tag()

    kabum_product_names_list = kabum_soup.get_text_all(kabum_product_name_tag, kabum_product_name_class)

    # Pegar a tag e a classe do componente que contém os preços.
    # Pegar a tag e a classe do componente que contém os descontos.