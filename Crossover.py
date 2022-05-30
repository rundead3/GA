# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:33:17 2022

@author: João Correia
"""

### O template crossover é só para ver se o algoritmo funciona, depois adiciona-se operadores

from random import randint, sample
from Individuals import Individual#, is_admissible

def template_crossover(parent1, parent2):
    """ Given 2 parents, generates 2 children.
    
    Inputs:
        - parent1: Individual
        - parent2: Individual
    Output:
        - child1: Individual
        - child2: Individual
    """
    return parent1, parent2

def single_point_co(parent1, parent2):
    """ Given 2 parents, generates 2 children.
    
    Inputs:
        - parent1: Individual
        - parent2: Individual
    Output:
        - child1: Individual
        - child2: Individual
    """
    co_point = randint(1, len(parent1.representation)-2)

    child1_repr = parent1.representation[:co_point] + parent2.representation[co_point:]
    child2_repr = parent2.representation[:co_point] + parent1.representation[co_point:]

    child1 = Individual(child1_repr)
    child2 = Individual(child2_repr)

    return child1, child2


def double_point_co(parent1, parent2):
    """ Given 2 parents, generates 2 children.

    Inputs:
        - parent1: Individual
        - parent2: Individual
    Output:
        - child1: Individual
        - child2: Individual
    """
    co_point1 = randint(1, len(parent1.representation) - 4)
    co_point2 = randint(co_point1, len(parent1.representation) - 2)

    child1_repr = parent1.representation[:co_point1] + parent2.representation[co_point1:co_point2] + parent1.representation[co_point2:]
    child2_repr = parent2.representation[:co_point1] + parent1.representation[co_point1:co_point2] + parent2.representation[co_point2:]

    child1 = Individual(child1_repr)
    child2 = Individual(child2_repr)

    return child1, child2


def pmx_co(parent1, parent2):
    # Sample 2 random co points
    co_points = sample(range(len(parent1.representation)), 2)
    co_points.sort()

    def PMX(p1, p2):
        # Create placeholder for offspring
        child = [None] * len(p1)

        # Copy co segment into offspring
        child[co_points[0]:co_points[1]] = p1[co_points[0]:co_points[1]]

        # Find set of values not in offspring from co segment in P2
        z = set(p2[co_points[0]:co_points[1]]) - set(p1[co_points[0]:co_points[1]])

        # Map values in set to corresponding position in offspring
        for i in z:
            temp = i
            index = p2.index(p1[p2.index(temp)])
            while child[index] != None:
                temp = index
                index = p2.index(p1[temp])
            child[index] = i
        # Fill in remaining values
        while None in child:
            index = child.index(None)
            child[index] = p2[index]
        return child

    # Call function twice with parents reversed
    child1, child2 = (
        PMX(parent1.representation, parent2.representation),
        PMX(parent2.representation, parent1.representation)
    )
    child1 = Individual(child1)
    child2 = Individual(child2)

    return child1, child2
 
    
if __name__ == "__main__":
    p1 = Individual()
    p2 = Individual()
    print(p1)
    print(p2)
    c1, c2 = pmx_co(p1, p2)
    print(c1)
    #print(is_admissible(p1.representation))
    #print(is_admissible(c1.representation))
