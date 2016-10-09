import random as rn

class CircleGen(object):
    ''''
       Circle Class

       A circle is defined by its radius, center coordinates,
       background color and alpha component.
    '''

    def __init__( self, height , width , maxopacity ):

        # Define parameters for random circle generation

        self.center = (rn.randint(0, width), rn.randint(0, height))
        self.radius = rn.randint(1, max( height / 3 , width / 3 ))
        self.color = (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))
        self.alpha = maxopacity * rn.random()


    def getInfo ( self ):

        # Retrive information about the class

        return ( self.center, self.radius , self.color , self.alpha )







