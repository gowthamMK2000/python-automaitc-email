import csv

with open("contact.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for name,email,age in reader:
        print(name,email,age)
