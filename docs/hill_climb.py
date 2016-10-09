import numpy as np
import cv2
import circle
import individual
import copy

class HillClimbing(object):
    ''''
           Hill Climbing

           is a mathematical optimization technique which belongs to the family of local search.
           It is an iterative algorithm that starts with an arbitrary solution to a problem,
           then attempts to find a better solution by incrementally changing a single element
           of the solution. If the change produces a better solution, an incremental change
           is made to the new solution, repeating until no further improvements can be found.

           We will consider an initial pool of polygons and we keep adding more polygons as long
           as the total mean squared error is significantly reduced with respect to the target
           image we want to approximate.
    '''

    def __init__(self,iterations,target, length ):

        self.iterations = iterations
        self.target = target
        self.height , self.width = target.shape[:2]
        self.length = length


    def run ( self ):

        # Run the hill climbing optimization and print

        # Start with a random initial solution
        solution = individual.IndividualGen( self.length , self.height , self.width )
        min_err = self.height * self. width

        # Start iterative optimization to minimize error
        for i in range(self.iterations):

            # Store solution
            temp = copy.deepcopy(solution)
            # Modify one random polygon in solution
            temp.mutation()
            # Compute dissimilarity
            err = temp.fitness(self.target)

            # Update the solution that provides more fitness
            if err < min_err  :
                min_err = err
                solution = copy.deepcopy(temp)

            # Print results evolution
            if i % 50 == 0 :
                solution.write("Solution_Error_" + str(i) + "_" + str(min_err) + ".jpg")










