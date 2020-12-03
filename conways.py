import random

class Conways:
    def __init__(self):
        self.cells = list()

        for i in range(0,2500):
            cell = random.randint(0,100000) % 2
            self.cells.append(cell)
        
    def getCell(self, x,y):
        return self.cells[y * 50 + x]

    def setCell(self,x,y, num):
        self.cells[y * 50 + x] = num

    def getNeighbors(self,x,y):
        return self.getCell(x-1,y-1) + self.getCell(x,y-1) + self.getCell(x+1,y-1) + self.getCell(x-1,y) + 0 + self.getCell(x+1,y) + self.getCell(x-1,y+1) + self.getCell(x,y+1) + self.getCell(x+1,y+1)

    def generation(self):
        for i in range(0,49):
            for j in range(0,49):
                numNeighbors = self.getNeighbors(i,j)
                if numNeighbors < 2 and self.getNeighbors(i,j) == 1:
                    self.setCell(i,j,0)
                if numNeighbors == 2 or numNeighbors == 3 and self.getNeighbors(i,j) == 1:
                    self.setCell(i,j,1)
                if numNeighbors > 3 and self.getNeighbors(i,j) == 1:
                    self.setCell(i,j,0)
                if self.getNeighbors(i,j) == 0 and numNeighbors == 3:
                    self.setCell(i,j,1)

