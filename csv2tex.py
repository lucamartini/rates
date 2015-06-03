import glob
import re
import csv


def getCell(path, column):
    with open("path_rates_7E33.csv", 'r') as rates:
        ratereader = csv.reader(rates)
        for row in ratereader:
            if (path in row[0]) or ("LMNR" in path and "LowMass" in row[0]):
                return row[column]
    print "did not find", path


texFiles = glob.glob("./*_DEF.tex")
for texFile in texFiles:
    print texFile
    outFileName = texFile.replace("_DEF", "")
    outFile = open(outFileName, "w")

    with open(texFile, 'r') as tabular:
        for line in tabular:
            # print line
            reg = r'^\ *\\rowcolor\{[a-zA-Z0-9]+\} ([a-zA-Z0-9\_\\]+)\ +\&'
            pathreg = re.search(reg, line)

            if pathreg:
                path = pathreg.group(1).replace('\\', '')
                min = getCell(path, 1)
                max = getCell(path, 2)
                DEF_reg = r'(DEF)\ *\\\\$'
                rep = str("$" + min + "-" + max + "$ \\\\\\\\")
                line = re.sub(DEF_reg, rep, line)
                print line
            outFile.write(line)
