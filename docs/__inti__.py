import hill_climb
import sim_annealing
import cv2

# Load the image
target = cv2.imread("/home/alfredo/PycharmProjects/PolyPic/examples/IM_03.jpg")
height, width = target.shape[:2]

#Run Hill Climbing Algorithm
#hc = hill_climb.HillClimbing( 100000 , target , 60 )
#hc.run("Solution_Error_95000_735.151582599.txt")

#Run Simulated Annealing Algorithm
sa = sim_annealing.Simulated_Annealing(10000,target,60)
sa.run()


#Run Genetic Algorithm
#ga = gen_algo.GeneticAlgorithm(100,200,40,height,width,target)
#p = ga.selection(30)

#ans = individual.IndividualGen("Solution_Error_0_9013.73399178.txt")
#ans.write("ans.jpg")
