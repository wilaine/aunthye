def list():
    import csv
    with open('python.csv', 'r') as file:
        count = 1
        reader = csv.reader(file)
        print('{:<3} {:<33}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format("No","Name","myKIDNumber","Guardian Name","Relationship","City","Phone Number","Car Plate"))
        for row in reader:
            print(count,' {:<34}  {:<15}  {:<25} {:<15} {:<15} {:<15} {:<15}'.format(*row))
            count +=1      
