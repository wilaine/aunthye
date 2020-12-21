from functions import read
from functions import find_gender
"""from functions import oneKeyword
from functions import twoKeyword
from functions import update
from functions import append
from functions import delete
from functions import exit """
    
def main():
        
        chk = True
        while chk:
                print("**********************************")
                print("1. List                          *")
                print("2. Search by gender              *")
                print("3. Search by one keyword         *")
                print("4. Search by two keywords        *")
                print("5. Update                        *")
                print("6. Add                           *")
                print("7. Delete                        *")
                print("8. Exit                          *")
                print("**********************************")
                option = input("Please enter an option ")
                if option == "1":
                        read()
                elif option == "2":
                        find_gender()
                elif option == "3":
                        oneKeyword()                
                elif option == "4":
                        twoKeyword()
                elif option == "5":
                        update()        
                elif option == "6":
                        append()        
                elif option == "7":
                        delete()        
                elif option == "8":
                        exit()                        
                else:
                        print("Not Valid option")
                repeat = input("Continue? (y/n) ")
        if repeat == 'n':
                chk = False
