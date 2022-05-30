# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:32:20 2022

@author: João Correia
"""
import math
import numpy as np
from Data import matrix, d_data, b_data
import random
from copy import deepcopy

class Individual:

    def __init__(self, representation = None):
        if representation is None:
            self.representation = generate_solution()
        else:
            self.representation = representation
        self.fitness = self.calculate_fitness()
    
    def calculate_fitness(self):
        fitness = 0
        for i in range(len(matrix)): 
            ip = np.dot(self.representation[:-2],d_data[i])
            calc_bio = ip + self.representation[-2]
            fitness += np.square(np.subtract(b_data[i],calc_bio))
        fitness = math.sqrt(fitness/len(matrix))
        return fitness
        
    def generate_neighbor(self):
        """ Returns a Solution object, whose representation has 2 cities flipped
        from the original
        """
        index1 = random.randint(0, len(self.representation) - 1)
        index2 = random.randint(0, len(self.representation) - 1)
        new_rpr = deepcopy(self.representation)
        new_rpr[index1], new_rpr[index2] = new_rpr[index2], new_rpr[index1]
        new_sol = Individual(new_rpr)
        return new_sol
    
    # def __str__(self):
    #     return(f"Representation: {self.representation}. Fitness: {self.fitness}")
        
def generate_solution():
    representation = []
    n_descriptors = len(matrix[0])+1
    for i in range(n_descriptors):
        representation.append(np.random.randn())
    return representation

# def is_admissible(representation):
#     return len(set(representation)) == len(cities)
    
    

if __name__ == "__main__":
    my_sol = Individual()
    print(my_sol.representation)
    print(my_sol.fitness)
    




### Ver melhor os valores random iniciais
### Explorar as diferenças dos difererntes operadores na nossa score
### A inverse mutation é mais destrutiva do que a swap


