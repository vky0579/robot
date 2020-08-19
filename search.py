"""This is a part of robot 
which is an advance file management software 
with different capabilities

The main work of this program is to search for required file
and folder. It is easy to use."""

#update it by creating sql databases for reducing time and increasing speed
#current Version 4.2

"""This is an open sourch initiative and this code 
could be modified but the copy of modification should have 
the name of its developer that is : Vaibhav

This code should not be sold for money"""


import time
import os

class Main():    #this class will contain main code
    def __init__(self, path, name, directory):
        self.path = path
        self.name = name
        self.directory = directory
    

    def search_file(self):  #this is used to search file
        try:    
            os.chdir(os.path.join(os.getcwd(), self.path))
        except FileNotFoundError:
            print(f"{self.path} does not exists {os.getcwd()}")         
            exit() 
        
        for dirpath, dirname, filename in os.walk(os.getcwd()):
            for file in filename:
                if file.find(self.name) != -1:
                    print(f"found in : {os.path.join(os.getcwd(), file)}")

    def search_folder(self): #this is used to search folder
        try:    
            os.chdir(os.path.join(os.getcwd(), self.path))
        except:
            print(f"{self.path} does not exists {os.getcwd()}")
            exit()
   
        
        for dirpath, dirname, filename in os.walk(os.getcwd()):
            
            for folder in dirname:
                
                if folder.find(self.directory) != -1:

                    #####################################################################
                    """ print(f"found in : {os.path.join(os.getcwd(), folder)}")        
                    the above statement worked fine for files but it gave weird results 
                    for folder check walk.py for details"""
                    #####################################################################
                    
                    print(f"found in : {dirpath}\{folder}")
               
           
if __name__ == "__main__":
    
    path = input("Enter a path : ")
    if path == "":
        path = os.getcwd()    
    question = input("Do you want to search (a)file or (b)folder\n: ")
    
    #for files searching
    
    if question == "a":
        name = input("Enter name of the file\n: ")
        start = time.perf_counter()
        run = Main(path, name, None)  #here none is used as this is not required
        run.search_file()
        stop = time.perf_counter()
        print(stop - start)
        escape = input("press enter key to exit ")

    #for folder searching

    elif question == "b":
        name = input("Enter name of the folder : ")
        start = time.perf_counter()
        run = Main(path, None, name)
        run.search_folder()
        stop = time.perf_counter()
        print(stop - start)
        escape = input("press enter key to exit ")
    
    else:
        print("Please specify correct parameter")
        

#End of code
