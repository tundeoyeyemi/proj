import csv
file  = open("test.csv")
reader = csv.reader(file)
lines = len(list(reader))


