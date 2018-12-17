
import csv #For read/write of CSV files
import os,sys   #Helps in functionality related to OS and system
from Parser import Parser   #Our implemented class

class Parsing_CSV:
    '''This class is particularly designed for implementing CSV file reading/writing according to our needs'''
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



#TESTING
start_prog = Parsing_CSV("D:\SearchEngine\Dataset")
start_prog.storeKeywords()