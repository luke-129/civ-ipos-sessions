file_date = "hello there"
file_path = "output.csv"
import csv


with open("output.csv", "r") as file:
    content = csv.reader(file)
    for line in content:
        if line:
            print(line[0])



