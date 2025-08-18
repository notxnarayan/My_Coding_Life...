import csv

with open("CSVTest.csv","wr", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow("Hi")

