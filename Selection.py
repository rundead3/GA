# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:32:40 2022

@author: João Correia
"""


from random import sample, uniform
from operator import attrgetter
#from Population import *


def random_selection(elements):
    """Given a Population, selects 2 individuals, selected randomly

    Inputs:
        - elements: List of Individuals
    Output:
        - parent1: Individual
        - parent2: Individual
    """
    selected = sample(elements, 2)
    return selected[0], selected[1]


def tournament_selection(population, size= 8):
    # Select individuals based on tournament size
    tournament1 = sample(population, size)
    tournament2 = sample(population, size)
  
    return min(tournament1, key=attrgetter("fitness")), min(tournament2, key=attrgetter("fitness"))


def roulette_selection(population):
    pop_fitness = [1/indiv.fitness for indiv in population]
    total_fitness = sum(pop_fitness)
    # uniform -> Return a flot between (a,b)
    arrow1 = uniform(0, total_fitness)
    arrow2 = uniform(0, total_fitness)
    sum_fitness = 0
    for i in range(len(pop_fitness)):
        sum_fitness += pop_fitness[i]
        if sum_fitness >= arrow1:
            chosen1 = population[i]
            break
    for i in range(len(pop_fitness)):
        sum_fitness += pop_fitness[i]
        if sum_fitness >= arrow2:
            chosen2 = population[i]
            break
    return chosen1,chosen2

# if __name__=="__main__":
#     my_pop = Population(3,"min")
#     for indiv in my_pop.elements:
#         print(indiv)
#     print("Choosing: ")
#     print(roulette_selection(my_pop.elements,"min"))
