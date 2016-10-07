import numpy as np
import individual
import hill_climb
import cv2

# Load the image
target = cv2.imread("/home/alfredo/PycharmProjects/PolyPic/examples/IM_01.jpg")
height, width = target.shape[:2]

#Create an individual
ind = individual.IndividualGen( 10 , height , width )

# Measure its dissimilarity
print ind.fitness(target) ;

#Run Hill Climbing Algorithm
hc = hill_climb.HillClimbing( 1000, target )
hc.run()




