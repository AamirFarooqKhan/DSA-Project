from bs4 import BeautifulSoup
import re

class Parser:
    """This class is implementation of indexer
        ,it takes file names as arguments and parse those
        files, take out the keywords and store it in a file"""

    def __init__(self, file_name):
        self.html_file = file_name
        with open(self.html_file) as fp:
                    self.soup = BeautifulSoup(fp,'html.parser')

    #Just read the html file
    def read_html(self):
        print(self.soup.prettify())

    #Get all the keywords from html page by extracting contents of <title>,<b>,<h1>,<h2>,<h3>
    def get_keywords(self):
        keywords_list = self.soup.find_all('title')
        keywords_list.extend(self.soup.find_all('b'))
        keywords_list.extend(self.soup.find_all('h1'))
        keywords_list.extend(self.soup.find_all('h2'))
        keywords_list.extend(self.soup.find_all('h3'))
        return keywords_list


    def get_links(self):

        links = []

        for link in self.soup.findAll('a', attrs={'href': re.compile("^doc")}):
            links.append(link.get('href'))



        return links



















