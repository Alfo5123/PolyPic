import hill_climb
import sim_annealing
import gen_algo
import individual
import refine
import cv2

# Load the image
target = cv2.imread("/home/alfredo/PolyPic/examples/THREE_PEARS.jpg")
height, width = target.shape[:2]

#Run Hill Climbing Algorithm
#hc = hill_climb.HillClimbing( 100001 , target , 50 , 3)
#hc.run("SolutionSA_Error_100000_646.797153153.txt")

#Run Simulated Annealing Algorithm
sa = sim_annealing.Simulated_Annealing(100001,target,50,4)
sa.run()

# Refine
#source = cv2.imread("/home/alfredo/PolyPic/examples/STARRY_NIGHT_APROX.jpg")
#target = cv2.imread("/home/alfredo/PolyPic/examples/STARRY_NIGHT.jpg")

#ex = refine.Refine( 10000 , 50 , 1 , source , target )
#ex.run()

#ind = individual.IndividualGen("SolutionHC_Error_100000_749.862888889.txt")
#ind.write("STARRY_NIGHT_APROX_2.jpg")
#ind.encode("STARRY_NIGHT_1_749.862888889.txt")

#Run Genetic Algorithm
#ga = gen_algo.GeneticAlgorithm(100, 100, 100, height, width , target , 3)
#ga.run(20,0.25)
