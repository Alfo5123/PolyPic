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
                - Number of polygons in solution
                - Height of Image
                - Width of Image
                - Target Image

     '''

    def __init__(self, generations, population, size, height, width , target):

        # Set hyperparameters

        self.generations = generations
        self.population = population
        self.size = size
        self.height = height
        self.width = width
        self.target = target

        self.cur_gen = []
        for i in range(population):
            self.cur_gen.append(individual.IndividualGen(self.size,self.height,self.width,0.1))


    def run ( self , best_k , mutation_rate ):

        # Performs generations update

        for gen in range(self.generations):

            # Sort individuals by Fitness
            scores = []
            for i in range(self.population):
                scores.append((self.cur_gen[i].fitness(self.target), self.cur_gen[i]))

            scores.sort(key=lambda x: x[0])

            # Report best individual per generation
            if gen % 500 == 0:
                scores[0][1].write("SolutionGA_Error_" + str(gen) + "_" + str(scores[0][0]) + ".jpg")

            # Create a new generation
            next_gen = []

            # Keep Top K Ranked individuals for next generation
            for i in range(best_k):
                next_gen.append(copy.deepcopy(scores[i][1]))

            parent1 = np.random.choice(scores[:][1], scores[:][0])
            parent2 = np.random.choice(scores[:][1], scores[:][0])

            print parent1
            print parent2

''''
            # Apply genetic operations to produce the next generation
            while len(next_gen) < self.population:

                # Selection
                parent1 = np.choice(scores[:][1],scores[:][0])
                parent2 = np.choice(scores[:][1], scores[:][0])

                # Crossover
                child1 =
                child2 =

                # Mutation
                if ( np.random.random() < mutation_rate ): child1.mutate()
                if ( np.random.random() < mutation_rate ): child2.mutate()

                next_gen.append(child1)
                next_gen.append(child2)

'''





