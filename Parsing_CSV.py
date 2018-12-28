
import csv #For read/write of CSV files
import os,sys   #Helps in functionality related to OS and system
from Parser import Parser   #Our implemented class

class Parsing_CSV:
    '''This class is particularly designed for implementing CSV file reading/writing according to our needs as well as certain
    important algorithms are implemented here like ranking of pages according to number of links that are pointing towards the pages'''

    #Constructor
    def __init__(self, path):
        self.all_files = []  #Will store the names of all HTML files
        self.path = path     #Stores the absolute path URL of the folder containing all the HTML files.
        for x in os.listdir(self.path): #Itreates the listDir and appends file names to all_files[]
            self.all_files.append(x)


    #Get all html files stored in Dataset folder,parse them and store keywords and corresponding file names
    def storeKeywords(self):
        #Grab the html file one by one stored in all_files list.
        for htmlfile_name in self.all_files:
            my_parser = Parser(self.path+"\\"+htmlfile_name)    #Instantiate ParserObj in my_parser.
            with open("Catalogue.csv",'a') as csv_file:         #Create file catalogue.
                csv_generator = csv.writer(csv_file, delimiter=",")

                #Grab each keyword generated.
                for keyword in my_parser.get_keywords():
                    csv_generator.writerow([keyword.string,htmlfile_name])



   #This method generates ranking for each page i.e Its importance according to the number of links pointing towards that page from different html pages
    def generateRankings(self):
            ranks = {} #Empty dictionary
            for htmlfile_name in self.all_files:
                ranks[htmlfile_name] = [0] #Store html file names as keys and set their pair to a list containing zero.

            for htmlfile_name in self.all_files: #For each html file stored in dataset

                my_parser = Parser(self.path + "\\" + htmlfile_name)  # Instantiate ParserObj in my_parser.
                # Grab the links from the page.
                for ahref in my_parser.get_links():
                    ranks[ahref][0] += 1    #link pointing t a page, the rank of that page is increased by 1.

            return ranks  #Dictionary with file names as keys and their ranks in a single element list.



    #Generate Inverted Index
    def generateInvertedIndex(self):
       with open("Catalogue.csv", 'r') as keywords_file:     #Opens the already created catalouge file
           get_forward_index = csv.reader(keywords_file)

           documents = {}   #Dictionary that will store Document:Keywords pair

           for line in get_forward_index:
               if len(line) > 0:
                  documents[line[1]] = []   #Creates keys with document names and set it to empty list
       with open("Catalogue.csv", 'r') as keywords_file:
           get_forward_index = csv.reader(keywords_file)
           for line in get_forward_index:
               if len(line) > 0:
                   documents[line[1]].append(line[0])   #Creates keyword:documents pair


           return documents

    def writeInvertedIndex(self):
         with open("Inverted_Index.txt",'a') as invert_file:
           documents = self.generateInvertedIndex()
           write_inverted = csv.writer(invert_file,delimiter="\t")
           write_inverted.writerow(["Document Name","Keywords"])
           for docname in documents:
               write_inverted.writerow([docname,documents[docname]])


    #Generates Forward Index
    def generateForwardIndex(self):
        with open("Catalogue.csv", 'r') as keywords_file:   #Opens the already created catalouge file
            get_forward_index = csv.reader(keywords_file)

            keywords = {}   #Dictionary that will store Keyword:Documents pair

            for line in get_forward_index:
                if len(line) > 0:
                    keywords[line[0]] = []  #Creates keys with keywords and set it to empty list
        with open("Catalogue.csv", 'r') as keywords_file:
            get_forward_index = csv.reader(keywords_file)
            for line in get_forward_index:
                if len(line) > 0:
                    keywords[line[0]].append(line[1])   #Creates document:keywords pair

            return keywords

    #Write/Appends forward index to txt file.
    def writeForwardIndex(self):
        with open("Forward_Index.txt", 'a') as invert_file: #Create new txt file
            keywords = self.generateForwardIndex()  #Get keywords dictionary
            write_forward = csv.writer(invert_file, delimiter=",")
            write_forward.writerow(["Keywords", "Documents"])   #Write keywords:Documents pair to a txt
            for key in keywords:
                write_forward.writerow([key, keywords[key]])

    #Write the page rank generated into a csv file.
    def writePagerank(self):
        with open("Pagerank.csv", 'a') as pagerank_file:
            ranks = self.generateRankings()
            write_forward = csv.writer(pagerank_file, delimiter=",")
            write_forward.writerow(["Documents", "Ranks"])
            for rank in ranks:
                write_forward.writerow([rank, ranks[rank]])

    #This method operates on a string to extract its useful components. In this case a number(rank of page) which is stored as a string in csv file.
    def extractNumber(self,x):
        num = ""
        for char in x:

            if char != '[' and char != "]" and char != ',':
                num += char
        result = int(num)
        return result

    #For a given page,returns its rank
    def giveRank(self,docname):

        with open("Pagerank.csv", 'r') as pagerank_file: #Create new txt file

            reading_file = csv.reader(pagerank_file)
            next(reading_file)
            for line in reading_file:
                if len(line) > 0 :
                    if line[0] == docname:
                        x = self.extractNumber(line[1])
            return(x)


    #Give the documents that have the desired keyword. The page with highest rank is opened.
    def giveDocs(self,keyword):
        x = []
        with open("Catalogue.csv", 'r') as searcher: #Create new txt file

            reading_file = csv.reader(searcher)
            next(reading_file)
            for line in reading_file:
                if len(line) > 0 :
                    if keyword in line[0]:
                       x.append(line[1])
        return x

#my = Parsing_CSV("D:\\SearchEngine\\Dataset")
#my.storeKeywords()
#my.generateForwardIndex()
#my.generateInvertedIndex()
#my.writeInvertedIndex()
#my.generateForwardIndex()
#my.generateRankings()
#my.writePagerank()