import hill_climb
import sim_annealing
import gen_algo
import individual
import refine
import cv2

# Load the image
target = cv2.imread("/home/alfredo/PolyPic/examples/IM_01_TRAIN.jpg")
height, width = target.shape[:2]

#Run Hill Climbing Algorithm
#hc = hill_climb.HillClimbing( 1000001 , target , 60 , 1)
#hc.run("SolutionHC_Error_100000_1108.23972222.txt")

#Run Simulated Annealing Algorithm
#sa = sim_annealing.Simulated_Annealing(100001,target,50,3)
#sa.run("SolutionSA_Error_100000_1206.72011111.txt")

# Refine
#source = cv2.imread("/home/alfredo/PolyPic/examples/STARRY_NIGHT_APROX.jpg")
#target = cv2.imread("/home/alfredo/PolyPic/examples/STARRY_NIGHT.jpg")

#ex = refine.Refine( 10000 , 50 , 1 , source , target )
#ex.run()

#ind = individual.IndividualGen("SolutionHC_Error_1000000_1041.07122222.txt")
#ind.write("STARRY_NIGHT_APROX.jpg")
#ind.encode("STARRY_NIGHT_1_1041.07122222.txt")

#Run Genetic Algorithm
#ga = gen_algo.GeneticAlgorithm(100, 100, 100, height, width , target , 3)
#ga.run(20,0.25)
