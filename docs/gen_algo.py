import numpy as np
import individual
import copy

class GeneticAlgorithm(object):
    ''''
            Genetic Algorithm

            A metaheurisic algorithm inspired by the process of natural
            selection that mimics biological evolution to solve constrained
            and unconstrained optimization problems.

            At each step, the genetic algorithm randomly selects individuals
            from the current population and uses them as parents to produce
            the offspring for the next generation. Over successive generations,
            the population "evolves" toward an optimal solution.

            INPUT:
                - Number of generations
                - Number of solutions in initial population
                - Number of polygons in soltion
                - Height of Image
                - Widht of Image
                - Target Image

                	randomly initialize population(t)determine fitness of population(t)
                    repeat

                        select parents from population(t)
                        perform crossover on parents creating population(t+1)
                        perform mutation of population(t+1)
                        determine fitness of population(t+1)

                    until best individual is good enoug

     '''

    def __init__(self, generations, population, size, height, width , target):

        # Set hyperparameters

        self.generations = generations
        self.population = population
        self.size = size
        self.height = height
        self.width = width
        self.target = target

        self.pool = []
        for i in range(population):
            self.pool.append(individual.IndividualGen(self.size,self.height,self.width));


    def mutation ( self , mutationproba ):

        # Mutatate some individuals from pool to allow diversity at exploration

        for i in range(self.population):
            if np.random() < mutationproba :
                self.pool[i].mutate()

    def selection ( self , numparents ):

        # Pick the best elements based on fitness

        scores = []
        for i in range(self.population):
            scores.append ( ( self.pool[i].fitness(self.target) , i ) )

        scores.sort(key=lambda x: x[0])

        parents = []
        for i in range(numparents):
            parents.append ( copy.deepcopy(self.pool[scores[i][1]]) )

        return parents






