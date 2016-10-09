import numpy as np
import individual
import hill_climb
import cv2

# Load the image
target = cv2.imread("/home/alfredo/PycharmProjects/PolyPic/examples/IM_04.jpg")
height, width = target.shape[:2]

#Run Hill Climbing Algorithm
hc = hill_climb.HillClimbing( 100000 , target , 40 )
hc.run()




