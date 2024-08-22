import sites.kabum as kabum
import sites.pichau as pichau
import sites.terabyte as terabyte
import sites.magalu as magalu
import sites.americanas as americanas
import sites.mercado_livre as mercadolivre

def get_kabum_info(input_search) -> dict:
    kabum_soup = kabum.get_kabum_soup(input_search, "1")
    kabum_product_names = kabum.get_kabum_product_names(kabum_soup)
    kabum_old_prices = kabum.get_kabum_old_prices(kabum_soup)
    kabum_current_prices = kabum.get_kabum_current_prices(kabum_soup)
    kabum_discounts = kabum.get_kabum_discounts(kabum_soup, kabum_old_prices)
    kabum_product_links = kabum.get_kabum_product_links(kabum_soup)

    kabum_dict = {
        'product_names': kabum_product_names,
        'old_prices': kabum_old_prices,
        'current_prices': kabum_current_prices,
        'discounts': kabum_discounts,
        'product_links': kabum_product_links,
    }

    # for i in range(10):
    #     print(kabum_product_names[i])
    #     if kabum_old_prices[i] != '':
    #         print(kabum_discounts[i])
    #         print(kabum_old_prices[i])
    #     print(kabum_current_prices[i])
    #     print(kabum_product_links[i])

    return kabum_dict

def get_magalu_info(input_search) -> dict:
    magalu_soup = magalu.get_magalu_soup(input_search, "1")
    magalu_product_names = magalu.get_magalu_product_names(magalu_soup)
    magalu_all_prices = magalu.get_magalu_all_prices(magalu_soup)
    magalu_old_prices, magalu_current_prices = magalu.get_magalu_prices(magalu_all_prices)
    magalu_product_links = magalu.get_magalu_product_links(magalu_soup)

    magalu_dict = {
        'product_names': magalu_product_names,
        'old_prices': magalu_old_prices,
        'current_prices': magalu_current_prices,
        'product_links': magalu_product_links,
    }
    # for i in range(10):
    #     print(magalu_product_names[i])
    #     print(magalu_old_prices[i])
    #     print(magalu_current_prices[i])
    #     print(magalu_product_links[i])

    return magalu_dict

def get_mercadolivre_info(input_search) -> dict:
    mercadolivre_soup = mercadolivre.get_mercadolivre_soup(input_search, "1")
    mercadolivre_product_names = mercadolivre.get_mercadolivre_product_names(mercadolivre_soup)
    mercadolivre_all_prices = mercadolivre.get_mercadolivre_all_prices(mercadolivre_soup)
    mercadolivre_old_prices, mercadolivre_current_prices = mercadolivre.get_mercadolivre_prices(mercadolivre_all_prices)
    mercadolivre_product_links = mercadolivre.get_mercadolivre_product_links(mercadolivre_soup)

    mercadolivre_dict = {
        'product_names': mercadolivre_product_names,
        'old_prices': mercadolivre_old_prices,
        'current_prices': mercadolivre_current_prices,
        'product_links': mercadolivre_product_links,
    }
    # for i in range(10):
    #     print(mercadolivre_product_names[i])
    #     print(mercadolivre_old_prices[i])
    #     print(mercadolivre_current_prices[i])
    #     print(mercadolivre_product_links[i])

    return mercadolivre_dict

def get_pichau_info(input_search) -> dict:
    pichau_soup = pichau.get_pichau_soup(input_search, "1")
    pichau_product_names = pichau.get_pichau_product_names(pichau_soup)
    pichau_all_prices = pichau.get_pichau_all_prices(pichau_soup)
    pichau_old_prices, pichau_current_prices = pichau.get_pichau_prices(pichau_all_prices)
    pichau_product_links = pichau.get_pichau_product_links(pichau_soup)

    pichau_dict = {
        'product_names': pichau_product_names,
        'old_prices': pichau_old_prices,
        'current_prices': pichau_current_prices,
        'product_links': pichau_product_links,
    }
    # for i in range(10):
    #     print(pichau_product_names[i])
    #     print(pichau_old_prices[i])
    #     print(pichau_current_prices[i])
    #     print(pichau_product_links[i+8])

    return pichau_dict

def get_terabyte_info(input_search) -> dict:
    terabyte_soup = terabyte.get_terabyte_soup(input_search, "1")
    terabyte_product_names = terabyte.get_terabyte_product_names(terabyte_soup)
    terabyte_all_prices = terabyte.get_terabyte_all_prices(terabyte_soup)
    terabyte_old_prices, terabyte_current_prices = terabyte.get_terabyte_prices(terabyte_all_prices)
    terabyte_product_links = terabyte.get_terabyte_product_links(terabyte_soup)

    terabyte_dict = {
        'product_names': terabyte_product_names,
        'old_prices': terabyte_old_prices,
        'current_prices': terabyte_current_prices,
        'product_links': terabyte_product_links,
    }
    # for i in range(10):
    #     print(terabyte_product_names[i])
    #     print(terabyte_old_prices[i])
    #     print(terabyte_current_prices[i])
    #     print(terabyte_product_links[i])

    return terabyte_dict
    
def get_americanas_info(input_search) -> dict:
    americanas_soup = americanas.get_americanas_soup(input_search, "1")
    americanas_product_names = americanas.get_americanas_product_names(americanas_soup)
    americanas_all_prices = americanas.get_americanas_all_prices(americanas_soup)
    americanas_old_prices, americanas_current_prices = americanas.get_americanas_prices(americanas_all_prices)
    americanas_product_links = americanas.get_americanas_product_links(americanas_soup)

    americanas_dict = {
        'product_names': americanas_product_names,
        'old_prices': americanas_old_prices,
        'current_prices': americanas_current_prices,
        'product_links': americanas_product_links,
    }
    # for i in range(10):
    #     print(americanas_product_names[i])
    #     print(americanas_old_prices[i])
    #     print(americanas_current_prices[i])
    #     print(americanas_product_links[i])

    return americanas_dict

if __name__ == "__main__":
    input_search = input('Digite o que deseja procurar: ')

    kabum_scraper = get_kabum_info(input_search)
    magalu_scraper = get_magalu_info(input_search)
    mercadolivre_scraper = get_mercadolivre_info(input_search)
    pichau_scraper = get_pichau_info(input_search)
    terabyte_scraper = get_terabyte_info(input_search)
    # americanas_scraper = get_americanas_info(input_search)

    # for i in range(10):
    #     print(kabum_scraper['product_names'][i])
    #     print(kabum_scraper['old_prices'][i])
    #     print(kabum_scraper['current_prices'][i])
    #     print(kabum_scraper['product_links'][i])