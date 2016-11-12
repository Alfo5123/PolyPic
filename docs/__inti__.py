import hill_climb
import sim_annealing
import gen_algo
import individual
import refine
import cv2

# Load the image
#workdir = "/home/alfredo/PolyPic/examples/"
#image_name = "BIRDS.jpg"
#target = cv2.imread(workdir+image_name)
#height, width = target.shape[:2]

# Resize Image for speeding up training
#scale = 0.5
#train = cv2.resize( target, (0,0), fx=scale, fy=scale)
#train_name = image_name[:-4] + "_TRAIN.jpg"
#cv2.imwrite(workdir + train_name,train)

#Run Hill Climbing Algorithm
#hc = hill_climb.HillClimbing( 100001 , target , 200 , 4)
#hc.run("SolutionHC_Error_100000_437.822713675.txt")

#Run Simulated Annealing Algorithm
#sa = sim_annealing.Simulated_Annealing(100001,target,200,4)
#sa.run()

# Refine
#source = cv2.imread("/home/alfredo/PolyPic/examples/STARRY_NIGHT_APROX.jpg")
#target = cv2.imread("/home/alfredo/PolyPic/examples/STARRY_NIGHT.jpg")
#ex = refine.Refine( 10000 , 50 , 1 , source , target )
#ex.run()

# Generate Individual
#ind = individual.IndividualGen("SolutionHC_Error_100000_430.692232906.txt")
#ind.write("BIRDS_APROX.jpg")

#Run Genetic Algorithm
#ga = gen_algo.GeneticAlgorithm(100, 100, 100, height, width , target , 3)
#ga.run(20,0.25)
