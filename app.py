from perlin import PerlinMatrix
from conways import Conways
import random
import math





def terribleSort(lst):
    sorted = lst.sort()
    pm = PerlinMatrix()

    cgol = Conways()

    for i in range(0,10000):
        cgol.generation()

    matrix = list()
    for i in range(0,50):
        for j in range(0,50):
            matrix.append(0)

    while(lst != sorted):
        num = 0
        for i in range(0,50):
            for j in range(0,50):
                for k in range(0,50):
                    matrix[j * 50 + i] += (math.fabs(pm.noiseList[j * 50 + i]) * cgol.cells[j * 50 + i])
        for ugh in range(0,len(matrix)):
            num =+ matrix[ugh]
        intNum1 = math.floor(num) % len(lst)-1
        num = 0
        for i in range(0,50):
            for j in range(0,50):
                for k in range(0,50):
                    matrix[j * 50 + i] += math.fabs(pm.noiseList[j * 50 + i]) * cgol.cells[j * 50 + i]
        for ahh in range(0,len(matrix)):
            num =+ matrix[ahh]
        intNum2 = math.floor(num) % len(lst)-1

        temp = lst[intNum1]
        lst[intNum1] = lst[intNum2]
        lst[intNum2] = temp

testLst = [ random.randint(0,1000000) for i in range(0,100)]
terribleSort(testLst)