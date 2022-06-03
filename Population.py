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
import matplotlib.pyplot as plt

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

    def diversity_champion(self):
        """Returns the individual in the population with the best diversity
        """

        best = min(self.elements, key=attrgetter('fitness'))
        bestdiv = []
        currbest = 1000000
        for i in self.elements:
            divfitness = i.fitness * 1 - float(math.sqrt(math.pow(best.representation[-3] - i.representation[-3], 2))) / max(best.representation[-3], i.representation[-3])
            if divfitness < currbest:
                currbest = divfitness
                bestdiv = i

        return bestdiv

    def __str__(self):
        return f"Population of size {self.pop_size}"
    
    def evolve(self, n_gens, prob_crossover,selection_algorithm, crossover_algorithm, mutation_algorithm):
        # Iterate over a certain of generations
        # Each iteration:
        mutchance = []
        mutameta = []
        constant = []
        divconstant = []
        divfitness = []
        popsize = []
        fitness = []

        stagnancy = 0
        champion = self.find_best()
        championdiv = self.diversity_champion()
        last_champion = champion
        print(f"Initial best fitness: {champion.fitness}")
        try:

            for gen in range(n_gens):
                new_elements = []

                # Elitism
                champion = self.find_best()
                championdiv = self.diversity_champion()
                new_elements.append(champion)
                new_elements.append(championdiv)

                while len(new_elements) < self.pop_size+stagnancy:
                    #Always mutate the champions
                    p1, p2 = champion, championdiv
                    # Apply Crossover and/or Mutation
                    if random.random() < prob_crossover:
                        child1, child2 = crossover_algorithm(p1, p2)
                    else:
                        child1, child2 = p1, p2

                    child1 = mutation_algorithm(child1)
                    child2 = mutation_algorithm(child2)
                    # Put the new individuals into a new population
                    new_elements.append(child1)
                    new_elements.append(child2)

                    # Apply Selection
                    p1, p2 = selection_algorithm(self.elements,(int(5)))
                    # Apply Crossover and/or Mutation
                    if random.random() < prob_crossover:
                        child1, child2 = crossover_algorithm(p1, p2)
                    else:
                        child1, child2 = p1, p2

                    child1 = mutation_algorithm(child1)
                    child2 = mutation_algorithm(child2)
                    # Put the new individuals into a new population
                    new_elements.append(child1)
                    new_elements.append(child2)

                # Thew new population replaces the old population
                self.elements = new_elements
                #champion = self.find_best()
                print(f"Gen {gen+1} best fitness: {champion.fitness} mutchance: {abs(np.arctan(champion.representation[-1]))/(np.pi*0.5)*(100)} metamut: {champion.representation[-2]} constant: {champion.representation[-3]}\r\n Gen {gen+1} divfitness: {championdiv.fitness} mutchance: {abs(np.arctan(championdiv.representation[-1]))/(np.pi*0.5)*(100)} metamut: {championdiv.representation[-2]} constant: {championdiv.representation[-3]} " )
                #save



                fitness.append(champion.fitness)
                popsize.append(pop_size+stagnancy)
                constant.append(champion.representation[-3])
                mutchance.append(abs(np.arctan(champion.representation[-1]))/(np.pi*0.5)*(100))
                mutameta.append(champion.representation[-2])

                if champion.fitness == last_champion.fitness:
                    stagnancy += 10
                else:
                    stagnancy = int((stagnancy+450)*0.95)-450
                last_champion = champion
                if stagnancy < -450:
                    stagnancy = -450
                print(pop_size+stagnancy)

        except KeyboardInterrupt:
            pass
        plt.plot(fitness)
        plt.ylim([24, 30])
        plt.ylabel('FitnessZoomed')
        plt.show()
        plt.plot(fitness)
        plt.ylabel('Fitness')
        plt.show()
        plt.plot(popsize)
        plt.ylabel('Population size')
        plt.show()
        plt.plot(mutchance)
        plt.ylabel('Mutation chance')
        plt.show()
        plt.plot(mutameta)
        plt.ylabel('Mutation meta')
        plt.show()
        plt.plot(constant)
        plt.ylabel('Constant')
        plt.show()
        plt.plot(constant)
        plt.ylabel('Constant zoomed')
        plt.ylim([80, 110])
        plt.show()

        return champion

def plot_fitness(fitness,gen,):
    plt.plot()
    plt.ylim([22, 35])
    plt.scatter(gen, fitness)


def write_txt(fitness, representation, pop_size, gen, c_prob, sel_al, cro_al, mut_al):
    with open("Results.txt", "a") as f:
        sep = str("_"*250) + "\n"
        par = "Pop_size: " + str(pop_size) + ", " +  "Gen number: "  + str(gen) + ", " + "Crossover prob: " + str(c_prob) + ", " +  "\n"
        al = "Selection algorithm: " + str(sel_al) + ", " + "Crossover algorithm: " + str(cro_al) + ", " + "Mutation algorithm: " + str(mut_al) + "\n"
        fit = "Best Fitness: " + str(fitness) + "\n"
        rep = "Best Representation: " + str(representation) + "\n"
        lis = [sep,par,al,fit,rep]
        f.writelines(lis)
        f.close()

if __name__ == "__main__":
    pop_size = 500
    gen = 100000
    c_prob = 0.75
    selection_al = "tournament_selection" # É preciso mudar isto para o ficheiro
    crossover_al = "double_point_co" # É preciso mudar isto para o ficheiro
    mutation_al = "boundary_mutation" # É preciso mudar isto para o ficheiro
    my_pop = Population(pop_size = pop_size)
    my_sol = my_pop.evolve(gen, c_prob,
        selection_algorithm = tournament_selection,
        crossover_algorithm =  double_point_co,
        mutation_algorithm = boundary_mutation
                           )
    print(my_sol)
    print(my_sol.representation)
    write_txt(my_sol.fitness, my_sol.representation, pop_size, gen, c_prob,  selection_al,crossover_al,  mutation_al)
    plt.show()

