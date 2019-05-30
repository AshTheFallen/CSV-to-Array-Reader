import csv

csv.register_dialect('aa',
                     delimiter=';',
                     skipinitialspace=True)
results = []
user_id=[]
rate=[]
with open('C:\\Users\\Vesal\\Documents\\Uni\\97-2 Semester\\Information '
          'Retrival\\Project\\BX-CSV-Dump\\BX-Book-Ratings.csv') as csvFile:
    reader = csv.reader(csvFile, dialect='aa')
    for row in reader:
        results.append(row[1])
        user_id.append(row[0])
        rate.append(row[2])
results.pop(0)
user_id.pop(0)
rate.pop(0)

print('listing is done \n')

print('user_id len = '+str(len(user_id)) + ' rate len = '+str(len(rate))+'\n')

d = dict([(y, x + 1) for x, y in enumerate(sorted(set(results)))])

print('mapping is done \n')
# print(d)
resultFile = open("output.txt", "w")
for x in results:
    resultFile.write("%s,%d \n" % (x,d[x]))
resultFile.close()
i=0
for x in results:
    results[i]=d[x]
    i=i+1

print('user_id len = '+str(len(results))+'\n')

output =[]
for i in range(len(results)):
    output.append((user_id[i],results[i],rate[i]))
myFile = open("new results.txt", "w")
for t in output:
    line = ','.join(str(x) for x in t)
    myFile.write(line + '\n')
myFile.close()


