import numpy as np
import csv

def loadData(fileName):
    data = []

    with open(fileName) as csvfile:
        datareader = csv.reader(csvfile,  delimiter=';')

        #skip first row
        next(datareader)
        for row in datareader:
            data.append(row)
    
    data = np.array(data)

    X = data[:, :-1]
    Y = data[:, -1]

    return (X, Y)