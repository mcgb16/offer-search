from bs4 import BeautifulSoup

class Scraper():
    def __init__(self, content) -> None:
        self.content = content
        self.soup = BeautifulSoup(self.content, 'html.parser')

    def get_href_all(self, tag, attr_search, attr_type) -> list:
        all_links = self.soup.find_all(tag, attrs={attr_type:attr_search})
        links = []
        
        for l in all_links:
            links.append(l.get('href'))

        return links
    
    def get_text_all(self, tag, attr_search, attr_type) -> list:
        all_response = self.soup.find_all(tag, attrs={attr_type:attr_search})
        response_list = []
        
        for l in all_response:
            response_list.append(l.get_text())

        return response_list
    
    def get_soup_all(self, tag, attr_search, attr_type) -> list:
        all_response = self.soup.find_all(tag, attrs={attr_type:attr_search})
        
        return all_response
    
    # CÓDIGO POSSIVELMENTE NÃO SERÁ MAIS NECESSÁRIO
    # def get_soup_all_data_testid(self, tag, search_testid) -> list:
    #     all_response = self.soup.find_all(tag, attrs={"data-testid":search_testid})
        
    #     return all_response
    
    # def get_text_all_data_testid(self, tag, search_testid) -> list:
    #     all_response = self.soup.find_all(tag, attrs={"data-testid":search_testid})
    #     response_list = []
        
    #     for l in all_response:
    #         response_list.append(l.get_text())

    #     return response_list
    
    # def get_href_all_data_testid(self, tag, search_testid) -> list:
    #     all_links = self.soup.find_all(tag, attrs={"data-testid":search_testid})
    #     links = []
        
    #     for l in all_links:
    #         links.append(l.get('href'))

    #     return links