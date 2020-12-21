def read():
    import csv
    with open('python.csv', 'r') as file:
        count = 1
        reader = csv.reader(file)
        print('{:<3} {:<33}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format("No","Name","myKIDNumber","Guardian Name","Relationship","City","Phone Number","Car Plate"))
        for row in reader:
            print(count,' {:<34}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format(*row))
            count +=1      

def find_gender():
    import csv
    with open('python.csv', 'r') as file:
        count = 1
        reader = csv.reader(file)
        ans = input("Enter the gender to search (male or female) : ")
        if(ans=="male" or ans=="female"):
            print('{:<3} {:<33}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format("No","Name","myKIDNumber","Guardian Name","Relationship","City","Phone Number","Car Plate"))
        for row in reader:
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
                print("Enter male or female!")
                
def oneKeyword():

def twoKeyword():

def update():

def append():

def delete():
    
def exit():