import hill_climb
import sim_annealing
import gen_algo
import individual
import cv2

# Load the image
target = cv2.imread("/home/alfredo/PycharmProjects/PolyPic/examples/IM_04.jpg")
height, width = target.shape[:2]

#Run Hill Climbing Algorithm
#hc = hill_climb.HillClimbing( 100001 , target , 60 , 2)
#hc.run("SolutionHC_Error_100000_337.268905473.txt")

#Run Simulated Annealing Algorithm
sa = sim_annealing.Simulated_Annealing(100001,target,60,3)
sa.run()

#ind = individual.IndividualGen("SolutionHC_Error_100000_332.787960199.txt")
#ind.write("MONA_LISA_APROX_2.jpg")

#Run Genetic Algorithm
#ga = gen_algo.GeneticAlgorithm

#ga.run(20,0.25)
