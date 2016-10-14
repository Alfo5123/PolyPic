import random as rn
import numpy as np

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

            self.height = arg[0]
            self.width = arg[1]
            self.maxopacity = arg[2]

            self.center = (rn.randint(0, self.width), rn.randint(0, self.height))
            self.radius = rn.randint(1, max( self.width / 3 , self.height  / 3 ))
            self.color = (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))
            self.alpha = self.maxopacity * rn.random()

        elif len(arg) == 4 :

            # Implicit definition by taking: height , width , max_opacity, decoding gene string

            self.height = arg[0]
            self.width = arg[1]
            self.maxopacity = arg[2]

            info = arg[3].split('-')
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
    def randomize( self ):

        # Produces  variations in gene parameters to a certain degree specified

        new_center_x = self.center[0] + np.random.normal(0,5)
        new_center_y = self.center[1] + np.random.normal(0,5)
        new_radius = self.radius + np.random.normal(0,10)

        new_color_r = self.color[0] + np.random.normal(0,5)
        new_color_g = self.color[1] + np.random.normal(0, 5)
        new_color_b = self.color[2] + np.random.normal(0, 5)
        new_alpha = self.alpha + np.random.normal(0, 0.5)

        # Update randomized values
        self.center = ( max ( 0 , min ( self.width , new_center_x ) ) ,
                        max ( 0 , min ( self.height, new_center_y ) ) )

        self.radius = max ( 1 , min ( 40, new_radius ) )

        self.color = ( max ( 0 , min ( 255 , new_color_r ) ) ,
                       max ( 0 , min ( 255 , new_color_g) ) ,
                       max ( 0 , min ( 255 , new_color_b) ) )

        self.alpha = max ( 0.0 , min ( self.maxopacity , new_alpha ) )

