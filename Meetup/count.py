import csv

with open('cryptogroups.csv', 'r') as file:

    reader = csv.reader(file, delimiter=',')

    count = 0

    for row in reader:

        count += int(row[1])

    print (count)
