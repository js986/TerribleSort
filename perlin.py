
import random
from perlin_noise import PerlinNoise


class PerlinMatrix:
    def __init__(self):
        self.noise = PerlinNoise(octaves=10)
        self.noiseList = list()
        for i in range(0,50):
            for j in range(0,50):
                self.noiseList.append(self.noise([random.uniform(0,1),random.uniform(0,1)]))


