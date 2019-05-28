import csv

csv.register_dialect('aa',
                     delimiter=';',
                     skipinitialspace=True)
results = []
with open('C:\\Users\\Vesal\\Documents\\Uni\\97-2 Semester\\Information '
          'Retrival\\Project\\BX-CSV-Dump\\BX-Books.csv') as csvFile:
    reader = csv.reader(csvFile, dialect='aa')
    for row in reader:
        results.append(row[0])
results.remove('ISBN')
myFile = open("output.txt", "w")
for item in results:
    myFile.write("%s,%d \n" % (item ,results.index(item)))

