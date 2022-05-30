# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:32:30 2022

@author: João Correia
"""

   
from audioop import cross
import random
from operator import attrgetter
from Individuals import *
from Selection import random_selection, tournament_selection, roulette_selection
from Crossover import template_crossover, pmx_co, single_point_co ,double_point_co
from Mutation import template_mutation, swap_mutation, inverse_mutation, boundary_mutation

class Population:
    def __init__(self, pop_size):
        self.pop_size = pop_size
        self.elements = []
        for i in range(pop_size):
            new_indiv = Individual()
            self.elements.append(new_indiv)
        
    def find_best(self):
        """Returns the individual in the population with the best fitness
        """
        best = min(self.elements, key=attrgetter('fitness'))
        return best
    
    def __str__(self):
        return f"Population of size {self.pop_size}"
    
    def evolve(self, n_gens, prob_crossover, prob_mutation,
               selection_algorithm, crossover_algorithm, mutation_algorithm):
        # Iterate over a certain of generations
        # Each iteration:
            
        champion = self.find_best()
        print(f"Initial best fitness: {champion.fitness}")
        
        for gen in range(n_gens):
            new_elements = []
            
            # Elitism
            champion = self.find_best()
            new_elements.append(champion)
            
            while len(new_elements) < self.pop_size:
                # Apply Selection
                p1, p2 = selection_algorithm(self.elements)
                # Apply Crossover and/or Mutation
                if random.random() < prob_crossover:
                    child1, child2 = crossover_algorithm(p1, p2)
                else:
                    child1, child2 = p1, p2
                if random.random() < prob_mutation:
                    child1 = mutation_algorithm(child1)
                    child2 = mutation_algorithm(child2)
                # Put the new individuals into a new population
                new_elements.append(child1)
                new_elements.append(child2)
                
            # Thew new population replaces the old population
            self.elements = new_elements
            champion = self.find_best()
            print(f"Gen {gen+1} best fitness: {champion.fitness}")
        return champion
    
if __name__ == "__main__":

    my_pop = Population(pop_size = 121)
    my_sol = my_pop.evolve(2000, 0.7,0.1,
        selection_algorithm = tournament_selection,
        crossover_algorithm = double_point_co,
        mutation_algorithm = boundary_mutation,
    )
    print(my_sol)
    print(my_sol.representation)
    
    