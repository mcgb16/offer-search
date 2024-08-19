import sites.kabum as kabum
import sites.pichau as pichau
import sites.terabyte as terabyte
import sites.magalu as magalu
import sites.americanas as americanas
import sites.mercado_livre as mercadolivre

if __name__ == "__main__":
    input_search = input('Digite o que deseja procurar: ')

    # KABUM   
    kabum_soup = kabum.get_kabum_soup(input_search, "1")
    kabum_product_names = kabum.get_kabum_product_names(kabum_soup)
    kabum_old_prices = kabum.get_kabum_old_prices(kabum_soup)
    kabum_current_prices = kabum.get_kabum_current_prices(kabum_soup)
    kabum_discounts = kabum.get_kabum_discounts(kabum_soup)
    kabum_product_links = kabum.get_kabum_product_links(kabum_soup)

    for i in range(10):
        print(kabum_product_names[i])
        if kabum_old_prices[i] != '':
            print(kabum_discounts[i])
            print(kabum_old_prices[i])
        print(kabum_current_prices[i])
        print(kabum_product_links[i])