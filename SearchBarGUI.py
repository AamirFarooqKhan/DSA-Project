from tkinter import *
from Search import Search
import webbrowser
def search():
   my_search = Search()
   document_name = my_search.searching(e1.get())
   if len(document_name) > 0:
       url = "D:\SearchEngine\\Dataset\\"+document_name
       webbrowser.open_new_tab(url)
   else:
       webbrowser.open_new_tab("Error.html")

master = Tk()
Label(master).grid(row=0)


e1 = Entry(master)


e1.grid(row=0, column=1)



Button(master,bg="Grey",  fg='#b7f731',relief="flat", text='Search',width=10, command=search).grid(row=1, column=1, sticky=W, pady=1)


mainloop( )