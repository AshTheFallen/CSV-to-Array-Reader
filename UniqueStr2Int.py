import csv

csv.register_dialect('aa',
                     delimiter=';',
                     skipinitialspace=True)
results = []
with open('C:\\Users\\Vesal\\Documents\\Uni\\97-2 Semester\\Information '
          'Retrival\\Project\\BX-CSV-Dump\\BX-Book-Ratings.csv') as csvFile:
    reader = csv.reader(csvFile, dialect='aa')
    for row in reader:
        results.append(row[0])
# results.remove('ISBN')

print('listing is done \n')

d = dict([(y, x + 1) for x, y in enumerate(sorted(set(results)))])

print('mapping is done')
myFile = open("output.txt", "w")
for x in d:
    myFile.write("%d \n" % d[x])
