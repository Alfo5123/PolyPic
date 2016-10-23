import random as rn
import numpy as np

class Rectangle( object ):
    ''''
          Rectangle Class

          A rectangle is defined by its top-left corner and bottom-right corner
          coordinates, it's color and alpha components
       '''

    def __init__( self , *args ):

        # Define parameters for circle generation

        if len ( args ) == 3:

            # Explicit definition with parameters: height , width , max_opacity

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            self.top_left = (rn.randint(0, self.width), rn.randint(0, self.height))
            self.bottom_right  = ( self.top_left[0] + rn.randint(0,self.width) ,
                                   self.top_left[1] + rn.randint(0,self.height))

            self.color = (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))
            self.alpha = self.maxopacity * rn.random()


        elif len(args) == 4 :

            # Implicit definition by taking: height , width , max_opacity, decoding gene string

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            info = args[3].split('-')
            self.top_left = (int(info[0]), int(info[1]))
            self.bottom_right = ( int(info[2]), int(info[3]) )
            self.color = (int(info[4]), int(info[5]), int(info[6]))
            self.alpha = float(info[7])


    def getInfo(self):

        # Retrive information about the object

        return (self.top_left, self.bottom_right, self.color, self.alpha)


    def encodeGene(self):

        # Returns a string encoding the gene information

        return ("{0}-{1}-{2}-{3}-{4}-{5}-{6}-{7}\n".format(self.top_left[0], self.top_left[1],
                                                           self.bottom_right[0], self.bottom_right[1],
                                                           self.color[0], self.color[1],
                                                           self.color[2], self.alpha))


    def randomize( self ):

        # Produces  variations in gene parameters to a certain degree specified

        new_top_left =  ( int ( self.top_left[0] + np.random.normal ( 0 , 5 ) ) ,
                          int ( self.top_left[1] + np.random.normal(0, 5)) )

        new_bottom_right =  ( int ( self.bottom_right[0] + np.random.normal( 0 , 5 ) ) ,
                              int ( self.bottom_right[1] + np.random.normal(0, 5) ) )


        new_color_r = int ( self.color[0] + np.random.normal(0,5) )
        new_color_g = int ( self.color[1] + np.random.normal(0, 5) )
        new_color_b = int ( self.color[2] + np.random.normal(0, 5) )
        new_alpha = self.alpha + np.random.normal(0, 0.5)

        # Update randomized values
        self.top_left = ( max ( 0 , min ( self.width , new_top_left[0] ) ) ,
                          max ( 0 , min ( self.height, new_top_left[1] ) ) )

        self.bottom_right = ( max ( self.top_left[0] , min ( self.width , new_bottom_right[0] ) )  ,
                              max ( self.top_left[1] , min ( self.height, new_bottom_right[1]) ) )

        self.color = ( max ( 0 , min ( 255 , new_color_r ) ) ,
                       max ( 0 , min ( 255 , new_color_g) ) ,
                       max ( 0 , min ( 255 , new_color_b) ) )

        self.alpha = max ( 0.0 , min ( self.maxopacity , new_alpha ) )