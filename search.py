"""This is a part of robot 
which is an advance file management software 
with different capabilities

The main work of this program is to search for required file
and folder. It is easy to use."""

#update it by creating sql databases for reducing time and increasing speed
#current Version 4.2

import time
import os
import argparse
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
                    print(f"found in : {dirpath}\{folder}")
               
           
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", help = "Specify the path ro search in")
    parser.add_argument("--name", "-n", help = "specify the name of file/folder")    
    parser.add_argument("--search", "-s", help = "Specify file or folder you are looking for (f = file/d = directory)", choices=["f", "d"])
    parser.add_argument("--version", "-v", help = "check the version", action = "store_true")

    args = parser.parse_args()  #parsing arguments

    path = os.getcwd()  #so if user specify nothing it takes default directory
    question = None

    if args.version:
        print("4.5")

    
    if args.path:
        path = args.path

    question = args.search
    
    #for files searching
    
    if question == "f":
        name = args.name
        start = time.perf_counter()
        run = Main(path, name, None)  #here none is used as this is not required
        run.search_file()
        stop = time.perf_counter()
        print(f"Time taken = {stop - start}")

    #for directory searching

    elif question == "d":
        name = args.name
        start = time.perf_counter()
        run = Main(path, None, name)
        run.search_folder()
        stop = time.perf_counter()
        print(f"Time taken = {stop - start}")

    