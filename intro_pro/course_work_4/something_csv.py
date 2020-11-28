import csv


with open('csv_score.csv', 'r') as file:
    readers = csv.reader(file)

    for line in readers:
        print(line)
        