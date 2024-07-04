from bs4 import BeautifulSoup

class Scraper():
    def __init__(self, content) -> None:
        self.content = content

    def initiate_soup(self) -> BeautifulSoup:
        soup = BeautifulSoup(self.content, 'html.parser')
        return soup