import random as rn

class Circle(object):
    ''''
       Circle Class

       A circle is defined by its radius, center coordinates,
       background color and alpha component.
    '''

    def __init__( self, *arg ):

        # Define parameters for random circle generation

        if len(arg) == 3 :

            #  Explicit definition with parameters: height , width , max_opacity

            self.center = (rn.randint(0, arg[1]), rn.randint(0, arg[0]))
            self.radius = rn.randint(1, max( arg[1] / 3 , arg[0] / 3 ))
            self.color = (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))
            self.alpha = arg[2] * rn.random()

        elif len(arg) == 1 :

            # Implicit definition by decoding gene string

            info = arg[0].split('-')
            self.center = (int(info[0]), int(info[1]))
            self.radius = int(info[2])
            self.color = (int(info[3]), int(info[4]), int(info[5]))
            self.alpha = float(info[6])

    def getInfo( self ):

        # Retrive information about the object

        return ( self.center, self.radius , self.color , self.alpha )

    def encodeGene( self ):

        # Returns a string encoding the gene information

        return ("{0}-{1}-{2}-{3}-{4}-{5}-{6}\n".format(self.center[0], self.center[1],
                                                       self.radius,self.color[0],
                                                       self.color[1], self.color[2],
                                                       self.alpha))

