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
                - Type of Polygon

     '''

    def __init__(self, generations, population, size, height, width , target):

        # Set hyperparameters

        self.generations = generations
        self.population = population
        self.size = size
        self.height = height
        self.width = width
        self.target = target
        self.type = type

        self.cur_gen = []
        for i in range(population):
            self.cur_gen.append(individual.IndividualGen(self.size,self.height,self.width, self.type, 0.1))


    def run ( self , best_k , mutation_rate ):

        # Performs generations update

        for gen in range(self.generations):

            # Sort individuals by Fitness
            scores = []
            for i in range(self.population):
                scores.append((self.cur_gen[i].fitness(self.target), self.cur_gen[i]))

            scores.sort(key=lambda x: x[0])

            # Report best individual per generation
            if gen % 100 == 0:
                scores[0][1].write("SolutionGA_Error_" + str(gen) + "_" + str(scores[0][0]) + ".jpg")
                scores[0][1].encode("SolutionGA_Error_" + str(gen) + "_" + str(scores[0][0]) + ".txt")

            # Create a new generation
            next_gen = []

            # Keep Top K Ranked individuals for next generation ( Ellitism )
            for i in range(best_k):
                next_gen.append(copy.deepcopy(scores[i][1]))

            # Apply genetic operations to produce the next generation
            while len(next_gen) < self.population:

                # Selection based on Fitness ( Roulette Wheel Sampling )

                order = np.random.permutation(self.population)
                rank = np.random.uniform(scores[0][0], scores[self.population-1][0])
                parent1_index = -1
                for i in range(self.population):
                    if ( scores[order[i]][0] <= rank ):
                        parent1_index = order[i]
                        break

                parent1 = copy.deepcopy( scores[parent1_index][1] )

                order = np.random.permutation(self.population)
                rank = np.random.uniform(scores[0][0], scores[self.population - 1][0])
                parent2_index = -1
                for i in range(self.population):
                    if (scores[order[i]][0] <= rank):
                        parent2_index = order[i]
                        break

                parent2 = copy.deepcopy(scores[parent2_index][1])

                # Crossover
                child1 = parent1
                child2 = parent2

                index = np.random.randint(0,self.size-1)
                child1.genes[:index] = scores[parent2_index][1].genes[:index]
                child2.genes[:index] = scores[parent1_index][1].genes[:index]

                # Mutation
                if np.random.random() < mutation_rate: child1.mutate()
                if np.random.random() < mutation_rate: child2.mutate()

                next_gen.append(child1)
                next_gen.append(child2)

            # Update new generation
            self.cur_gen = copy.deepcopy(next_gen)
