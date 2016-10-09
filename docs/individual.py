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
            self.individual.append(circle.CircleGen( height , width , 0.1 )) ;


    def generate ( self ):

        # Create black background image and fill it up with random polygons

        img = np.zeros((self.height, self.width, 3), np.uint8)

        overlay = img.copy()
        output = img.copy()

        for i in range(self.size):
            info = self.individual[i].getInfo()
            cv2.circle(overlay,info[0],  info[1], info[2], -1)
            cv2.addWeighted(overlay, info[3], output, 1 - info[3], 0, output)

        return output

    def write ( self , filename):

        # Write image in file

        cv2.imwrite(filename,self.generate())

    def fitness ( self , target ):

        # Calculate dissimilarity in pictures by MSE

        current = self.generate()
        err = np.sum((current.astype("float") - target.astype("float")) ** 2)
        err /= float(current.shape[0] * current.shape[1]* current.shape[2] )
        return err


    def mutation ( self ):

        # Pick a random polygon and randomize its properties

        index = rn.randint(0,self.size-1)
        self.individual[index] = circle.CircleGen( self.height , self.width , 0.1 )










