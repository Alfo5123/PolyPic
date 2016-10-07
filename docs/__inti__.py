import numpy as np
import individual
import cv2

# Load the image
target = cv2.imread("IM_01.jpg")
height, width = target.shape[:2]

#Create an individual
ind = individual.IndividualGen( 10 , height , width )

# Measure its dissimilarity
print ind.fitness(target) ;



