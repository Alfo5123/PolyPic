import numpy as np
import random as rn
import circle
import cv2

class IndividualGen(object):
    ''''
        Individual Class

        An individual is defined as a set of polygons (genes)
        that generates an image. The fitness of the individual
        is measure on the similarity given a target image.

    '''

    def __init__( self, size , height , width ):

        # Randomly generate an individual

        self.size = size
        self.height = height
        self.width = width

        self.individual = []
        for i in range(size):
            center = ( rn.randint(1, self.width) , rn.randint(1,self.height) )
            radius = rn.randint ( 1 , max( self.height/2 , self.width/2 ) )
            color = ( rn.randint(1,255) , rn.randint(1,255) , rn.randint(1,255) )
            alpha = 0.1*rn.random()
            self.individual.append(circle.CircleGen( center, radius, color , alpha )) ;


    def write ( self ):

        # Create white image and fill it up with random polygons

        img = np.zeros((self.height, self.width, 3), np.uint8)
        img[:] = (255, 255, 255)

        overlay = img.copy()
        output = img.copy()

        for i in range(self.size):
            info = self.individual[i].getInfo()
            cv2.circle(overlay,info[0],  info[1], info[2], -1)
            cv2.addWeighted(overlay, info[3], output, 1 - info[3], 0, output)

        cv2.imshow("Individual", output)
        cv2.waitKey(0)

        return output

    def fitness ( self , target ):

        # Calculate dissimilarity in pictures by MSE

        current = self.write()
        err = np.sum((current.astype("float") - target.astype("float")) ** 2)
        err /= float(current.shape[0] * current.shape[1]* current.shape[2] )
        return err







