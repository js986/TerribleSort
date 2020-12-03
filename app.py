from perlin import PerlinMatrix
from conways import Conways
import math

pm = PerlinMatrix()

cgol = Conways()

for i in range(0,10):
    cgol.generation()

matrix = list()
for i in range(0,50):
    for j in range(0,50):
        matrix.append(0)

for i in range(0,50):
    for j in range(0,50):
        for k in range(0,50):
            matrix[j * 50 + i] += math.fabs(pm.noiseList[j * 50 + i]) * cgol.cells[j * 50 + i]



def terribleSort(list):
    sorted = list.sort()
    while(list != sorted):
        #Not finished
