import numpy as np
import cv2
import circle

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
     '''
