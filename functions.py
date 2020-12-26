def read():
    import csv
    with open('children_record.csv', 'r') as file:
        count = 1
        reader = csv.reader(file)
        for row in reader:
            if(count==1):
                print('{:<3} {:<33}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format("No","Name","myKIDNumber","Guardian Name","Relationship","City","Phone Number","Car Plate"))
            print(count,' {:<34}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format(*row))
            count +=1      

def find_gender():
    import csv
    with open('children_record.csv', 'r') as file:
        count = 1
        reader = csv.reader(file)
        ans = input("Enter the gender to search (male or female) : ")
        for row in reader:
            if(ans=="male" or ans=="female"):
                if(count==1):
                    print('{:<3} {:<33}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format("No","Name","myKIDNumber","Guardian Name","Relationship","City","Phone Number","Car Plate"))
                gender = int(row[1].split('-')[2])
                if(ans=="male"):
                    if(gender%2==0):
                        continue
                    else:
                        print(count,' {:<34}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format(*row))
                        count +=1  
                elif(ans=="female"):
                    if(gender%2==0):
                        print(count,' {:<34}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format(*row))
                    count +=1 
            else:
                print("Please try again!! Enter male or female!")
                count +=1
                break
                


"""def twoKeyword():

def update():

def append():

def delete():
    
def exit():"""


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'