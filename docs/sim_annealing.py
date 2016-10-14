import individual
import copy
import numpy as np

class Simulated_Annealing(object):
    ''''
        Simulated Annealing

        It is a probabilistic technique for approximating the global optimum of a given function.
        Specifically, it is a metaheuristic to approximate global optimization in a large
        search space. It is often used when the search space is discrete (e.g., all tours
        that visit a given set of cities). For problems where finding an approximate global
        optimum is more important than finding a precise local optimum in a fixed amount of
        time, simulated annealing may be preferable to alternatives such as gradient descent.


        It outperforms hill climbing when there are many suboptimal local points in the search space.
        At each step, the SA heuristic considers some neighbouring state s' of the current state s,
        and probabilistically decides between moving the system to state s' or staying in state s.
        These probabilities ultimately lead the system to move to states of lower energy.
        Typically this step is repeated until the system reaches a state that is good enough for the
        application, or until a given computation budget has been exhausted.

    '''

    def __init__(self, iterations, target, size):

        # Set hyperparameters

        self.iterations = iterations
        self.target = target
        self.height, self.width = target.shape[:2]
        self.size = size


    def run( self , *args ):

        # Run the simmulated annealing optimization and print

        if len(args) == 0:
            # Start with a random initial solution
            solution = individual.IndividualGen(self.size, self.height, self.width , 0.1 )
            min_err = self.height * self.width

        else:
            # Start with a precomputed initial solution
            solution = individual.IndividualGen(args[0])
            data = args[0].split("_")
            min_err = float(data[3][:-4])

        # Iterative optimization to minimize error

        temperature = 100.0

        for i in range(self.iterations):

            # Store solution
            temp = copy.deepcopy(solution)
            # Modify one random polygon in solution
            temp.mutate()
            # Compute dissimilarity
            err = temp.fitness(self.target)

            # Update the solution that provides more fitness
            if err < min_err  :

                min_err = err
                solution = copy.deepcopy(temp)

            elif np.exp((min_err-err)/temperature) > np.random.random():

                min_err = err
                solution = copy.deepcopy(temp)

            # Print results evolution
            if i % 500  == 0 :
                solution.write("SolutionSA_Error_" + str(i) + "_" + str(min_err) + ".jpg")
                solution.encode("SolutionSA_Error_" + str(i) + "_" + str(min_err) + ".txt")

            # Cooling schedule
            temperature *= 0.99