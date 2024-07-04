from bs4 import BeautifulSoup

class Scraper():
    def __init__(self, content) -> None:
        self.content = content
        self.soup = BeautifulSoup(self.content, 'html.parser')

    def get_href_all(self, param, search_class) -> list:
        all_links = self.soup.find_all(param, class_= search_class)
        links = []
        
        for l in all_links:
            links.append(l.get('href'))

        return links
    
    def get_text_all(self, param, search_class) -> list:
        all_response = self.soup.find_all(param, class_= search_class)
        response_list = []
        
        for l in all_response:
            response_list.append(l.get_text())

        return response_list
    