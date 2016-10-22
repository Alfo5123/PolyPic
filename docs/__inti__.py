import hill_climb
import sim_annealing
import gen_algo
import cv2

# Load the image
target = cv2.imread("/home/alfredo/PycharmProjects/PolyPic/examples/MONA_LISA.jpg")
height, width = target.shape[:2]

#Run Hill Climbing Algorithm
#hc = hill_climb.HillClimbing( 100001 , target , 60 )
#hc.run("SolutionSA_Error_100000_592.60820744.txt")

#Run Simulated Annealing Algorithm
sa = sim_annealing.Simulated_Annealing(100001,target,5,3)
sa.run()


#Run Genetic Algorithm
#ga = gen_algo.GeneticAlgorithm

#ga.run(20,0.25)
