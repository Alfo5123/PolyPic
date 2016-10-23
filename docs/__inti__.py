import hill_climb
import sim_annealing
import gen_algo
import individual
import refine
import cv2

# Load the image
#target = cv2.imread("/home/alfredo/PycharmProjects/PolyPic/examples/IM_09_TRAIN.jpg")
#height, width = target.shape[:2]

#Run Hill Climbing Algorithm
#hc = hill_climb.HillClimbing( 100001 , target , 60 , 2)
#hc.run()

#Run Simulated Annealing Algorithm
#sa = sim_annealing.Simulated_Annealing(100001,target,2,5)
#sa.run()

# Refine
source = cv2.imread("/home/alfredo/PolyPic/examples/MONA_LISA_APROX.jpg")
target = cv2.imread("/home/alfredo/PolyPic/examples/MONA_LISA.jpg")

ex = refine.Refine( 10000 , 3 , source , target )
ex.run()

#ind = individual.IndividualGen("SolutionHC_Error_100000_429.987412935.txt")
#ind.write("MONA_LISA_APROX_3.jpg")

#Run Genetic Algorithm
#ga = gen_algo.GeneticAlgorithm(10, 100, 100, height, width , target , 2)
#ga.run(20,0.25)
