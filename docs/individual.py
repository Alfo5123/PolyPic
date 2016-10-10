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

    def __init__( self, *args ):

        if len(args) == 4 :

            # Randomly generate an individual taking as inputs: size , height , width ,  maxopacity
            self.size = args[0]
            self.height = args[1]
            self.width = args[2]

            self.individual = []
            for i in range(self.size):
                self.individual.append(circle.Circle(args[1], args[2], args[3]))

        else:  # len(args) == 1 :

            # Implicity define an individual based on its genes encoding
            file = open(args[0], 'r')

            self.size = int(file.readline())
            self.height = int(file.readline())
            self.width = int(file.readline())

            self.individual = []

            for i in range(self.size):
                self.individual.append(circle.Circle(self.height, self.width, 0.1, file.readline()))

            file.close()


    def generate( self ):

        # Create black background image and fill it up with random polygons

        img = np.zeros((self.height, self.width, 3), np.uint8)

        overlay = img.copy()
        output = img.copy()

        for i in range(self.size):
            info = self.individual[i].getInfo()
            cv2.circle(overlay,info[0],  info[1], info[2], -1)
            cv2.addWeighted(overlay, info[3], output, 1 - info[3], 0, output)

        return output

    def write( self , filename):

        # Write image in file

        cv2.imwrite(filename,self.generate())


    def fitness( self , target ):

        # Calculate dissimilarity in pictures by MSE

        current = self.generate()
        err = np.sum((current.astype("float") - target.astype("float")) ** 2)
        err /= float(current.shape[0] * current.shape[1]* current.shape[2] )
        return err


    def mutate( self , degree ):

        # Pick a random polygons and randomize its properties

        for i in range(self.size):
            if rn.random() < 0.33 :
                self.individual[i] = circle.Circle(self.height , self.width , 0.1 )
                # self.individual[i].randomize(0.5)


    def encode( self , filename ):

        # Store the current state of the individual in txt file

        file = open(filename, "w")

        file.write(str(self.size)+"\n")
        file.write(str(self.height)+"\n")
        file.write(str(self.width)+"\n")

        for i in range ( self.size ):
            file.write(self.individual[i].encodeGene())

        file.close()