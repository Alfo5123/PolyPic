import hill_climb
import sim_annealing
import gen_algo
import cv2

# Load the image
target = cv2.imread("/home/alfredo/PycharmProjects/PolyPic/examples/IM_03.jpg")
height, width = target.shape[:2]

#Run Hill Climbing Algorithm
#hc = hill_climb.HillClimbing( 100000 , target , 60 )
#hc.run("Solution_Error_95000_735.151582599.txt")

#Run Simulated Annealing Algorithm
#sa = sim_annealing.Simulated_Annealing(10001,target,60)
#sa.run()


#Run Genetic Algorithm
ga = gen_algo.GeneticAlgorithm(1,200,40,height,width,target)
ga.run(10,0.1)
