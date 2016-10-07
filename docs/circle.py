class CircleGen(object):
    ''''
       Circle Class

       A circle is defined by its radius, center coordinates,
       background color and alpha component.
    '''

    def __init__( self, center,radius,color,alpha ):

        # Define parameters

        self.center = center
        self.radius = radius
        self.color = color
        self.alpha = alpha

    def getInfo ( self ):

        # Retrive information about the class

        return ( self.center, self.radius , self.color , self.alpha )



