# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:32:30 2022

@author: João Correia
"""

import matplotlib.pyplot as plt
from audioop import cross
import random
from operator import attrgetter
from Individuals import *
from Selection import random_selection, tournament_selection, roulette_selection
from Crossover import template_crossover, pmx_co, single_point_co, double_point_co
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
        fitness = []
        constant = []

        champion = self.find_best()
        print(f"Initial best fitness: {champion.fitness}")

        for gen in range(n_gens):
            new_elements = []
            # # Elitism
            # champion = self.find_best()
            # new_elements.append(champion)

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

            fitness.append(champion.fitness)
            constant.append(champion.representation[-1])
            # Thew new population replaces the old population
            self.elements = new_elements
            champion = self.find_best()
            print(f"Gen {gen + 1} best fitness: {champion.fitness}")

        plt.plot(fitness)
        plt.ylim([30, 40])
        plt.ylabel('FitnessZoomed')
        plt.show()
        plt.plot(fitness)
        plt.ylabel('Fitness')
        plt.show()
        plt.plot(constant)
        plt.ylabel('Constant')
        plt.show()

        return champion, fitness


def write_txt(fitness, representation, pop_size, gen, c_prob, m_prob, sel_al, cro_al, mut_al, fitness2):
    with open("GA_results.txt", "a") as f:
        sep = str("_" * 250) + "\n"
        par = "Pop_size: " + str(pop_size) + ", " + "Gen number: " + str(gen) + ", " + "Crossover prob: " + str(
            c_prob) + ", " + "Mutation prob: " + str(m_prob) + "\n"
        al = "Selection algorithm: " + str(sel_al) + ", " + "Crossover algorithm: " + str(
            cro_al) + ", " + "Mutation algorithm: " + str(mut_al) + "\n"
        fit2 = "Fitness at each generation: " + str(fitness2) + "\n"
        fit = "Best Fitness: " + str(fitness) + "\n"
        rep = "Best Representation: " + str(representation) + "\n"
        lis = [sep, par, al, fit2, fit, rep]
        f.writelines(lis)
        f.close()


if __name__ == "__main__":
    pop_size = 100
    gen = 300
    c_prob = 0.7
    m_prob = 0.2
    selection_al = "tournament_selection"  # É preciso mudar isto para o ficheiro
    crossover_al = "double_point_co"  # É preciso mudar isto para o ficheiro
    mutation_al = "swap_mutation"  # É preciso mudar isto para o ficheiro
    my_pop = Population(pop_size=pop_size)
    my_sol, fit = my_pop.evolve(gen, c_prob, m_prob,
                                selection_algorithm=tournament_selection,
                                crossover_algorithm=double_point_co,
                                mutation_algorithm=swap_mutation,
                                )
    print(my_sol)
    print(my_sol.representation)
    write_txt(my_sol.fitness, my_sol.representation, pop_size, gen, c_prob, m_prob, selection_al, crossover_al,
              mutation_al, fit)