import sites.kabum as kabum
import sites.pichau as pichau
import sites.terabyte as terabyte
import sites.magalu as magalu
import sites.americanas as americanas
import sites.mercado_livre as mercadolivre

if __name__ == "__main__":
    input_search = input('Digite o que deseja procurar: ')

    # KABUM 
 
    # kabum_soup = kabum.get_kabum_soup(input_search, "1")
    # kabum_product_names = kabum.get_kabum_product_names(kabum_soup)
    # kabum_old_prices = kabum.get_kabum_old_prices(kabum_soup)
    # kabum_current_prices = kabum.get_kabum_current_prices(kabum_soup)
    # kabum_discounts = kabum.get_kabum_discounts(kabum_soup)
    # kabum_product_links = kabum.get_kabum_product_links(kabum_soup)

    # for i in range(10):
    #     print(kabum_product_names[i])
    #     if kabum_old_prices[i] != '':
    #         print(kabum_discounts[i])
    #         print(kabum_old_prices[i])
    #     print(kabum_current_prices[i])
    #     print(kabum_product_links[i])
    
    # MAGALU
    
    # magalu_soup = magalu.get_magalu_soup(input_search, "1")
    # magalu_product_names = magalu.get_magalu_product_names(magalu_soup)
    # magalu_all_prices = magalu.get_magalu_all_prices(magalu_soup)
    # magalu_old_prices, magalu_current_prices = magalu.get_magalu_prices(magalu_all_prices)
    # magalu_product_links = magalu.get_magalu_product_links(magalu_soup)

    # for i in range(10):
    #     print(magalu_product_names[i])
    #     print(magalu_old_prices[i])
    #     print(magalu_current_prices[i])
    #     print(magalu_product_links[i])