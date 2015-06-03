import os
import csv

ratedir = "./ratefiles_7E33/"
rateIndexName = "Total"
TnP = False

with open('path_rates_7E33.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile)
    with open('path_list_7E33.csv') as paths:
        for path in paths:
            min = 1000
            max = 0
            path = path.strip()
            if path == "":
                TnP = True
                continue

            for ratefile in os.listdir(ratedir):
                with open(ratedir + ratefile, 'r') as csvfile:
                    ratereader = csv.reader(csvfile)
                    firstRow = ratereader.next()
                    rateIndex = -1
                    for column in firstRow:
                        rateIndex = rateIndex + 1
                        if rateIndexName in str(column):
                            break
                    for row in ratereader:
                        if path in row[0]:
                            # print path, "vs", row[0]
                            if float(row[rateIndex]) < min:
                                min = float(row[rateIndex])
                            if float(row[rateIndex]) > max:
                                max = float(row[rateIndex])
            print "Rates for", path, ":", min, " - ", max
            csvwriter.writerow([path, min, max])
