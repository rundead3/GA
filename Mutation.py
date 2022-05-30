# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:34:32 2022

@author: João Correia
"""


### O template mutation é só para ver se o algoritmo funciona, depois adiciona-se operadores
    
from copy import deepcopy
from Individuals import Individual
from random import sample, random, randint

def template_mutation(parent1):
    """ Given 1 parent, generates a child
    
    Inputs:
        - parent1: Individual
    Output:
        - child1: Individual
    """
    return parent1

def swap_mutation(parent1):
    """ Given 1 parent, generates a child, which is the same
    as the parent, but with two numbers swapped
    
    Inputs:
        - parent1: Individual
    Output:
        - child1: Individual
    """
    new_representation = deepcopy(parent1.representation)
    swap_points = sample(range(0, len(new_representation)),2)
    a,b = swap_points[0], swap_points[1]
    new_representation[a], new_representation[b] = new_representation[b], new_representation[a]
    new_indiv = Individual(new_representation)
    return new_indiv

def inverse_mutation(parent1):
    new_representation = deepcopy(parent1.representation)
    swap_points = sample(range(0,len(new_representation)),2)
    swap_points.sort()
    chosen_slice = new_representation[swap_points[0]:swap_points[1]]
    chosen_slice = chosen_slice[::-1]   
    new_representation[swap_points[0]:swap_points[1]] = chosen_slice
    new_indiv = Individual(new_representation)
    return new_indiv


def boundary_mutation(parent1):
    new_representation = deepcopy(parent1.representation)
    i = randint(0,len(new_representation)-1)
    r = random()
    if r >= 0.5:
        new_representation[i] = new_representation[i] * new_representation[-1]
    else:
        new_representation[i] = new_representation[i] *-1.1*new_representation[-1]
    new_indiv = Individual(new_representation)
    return new_indiv



if __name__=="__main__":
    a = Individual()
    child = inverse_mutation(a)
    print(a)
    print(child)


    
    
### Fazer sempre uma cópia (deepcopy)
    