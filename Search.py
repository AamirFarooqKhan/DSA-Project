import webbrowser
import csv
from Parsing_CSV import Parsing_CSV
import webbrowser
class Search:

    def __init__(self):
        self.docs = []
        self.path = "D:\SearchEngine\Dataset\\"
        self.Parsing = Parsing_CSV(self.path)

    #For a given keyword search the documents it is included in and compute each document's rank. Then return a document with highest rank
    def searching(self,keyword):

        ranks = []
        documents = self.Parsing.giveDocs(keyword.capitalize())
        if len(documents) > 0:
                for x in documents:
                    ranks.append(self.Parsing.giveRank(x))
                index = ranks.index(max(ranks))
                return documents[index]
        else:
            return ""







my = Search()
my.searching("Titanic")