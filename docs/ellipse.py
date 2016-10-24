import random as rn
import numpy as np

class Ellipse ( object ):
    ''''
           Ellipse Class

           An ellipse is defined by its center coordinates,
           size of axes, angle of rotation, background color
           and alpha component
        '''

    def __init__( self , *args ):

        # Define parameters for ellipse generation

        if len ( args ) == 3 :

            #  Explicit definition with parameters: height , width , max_opacity

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            self.center = ( rn.randint(0, self.width), rn.randint(0, self.height) )
            self.axes =  (  rn.randint(1, max(self.width/5, self.height/5) ) ,
                            rn.randint(1, max(self.width/5, self.height/5) ) )
            self.rotation = rn.randint ( 0 , 360 )

            self.color = (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))
            self.alpha = self.maxopacity * rn.random()

        elif len ( args ) == 4 :

            # Implicit definition by taking: height , width , max_opacity, decoding gene string

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            info = args[3].split('-')
            self.center = (int(info[0]), int(info[1]))
            self.axes = (int(info[2] ) , int(info[3]) )
            self.rotation = int(info[4])
            self.color = (int(info[5]), int(info[6]), int(info[7]))
            self.alpha = float(info[8])

    def getInfo( self ):

        # Retrive information about the object

        return ( self.center, self.axes ,  self.rotation , self.color , self.alpha )


    def encodeGene( self ):

        # Returns a string encoding the gene information

        return ("{0}-{1}-{2}-{3}-{4}-{5}-{6}-{7}-{8}\n".format(self.center[0], self.center[1],
                                                               self.axes[0], self.axes[1],
                                                               self.rotation , self.color[0],
                                                               self.color[1], self.color[2],
                                                               self.alpha))

    def randomize( self ):

        # Produces  variations in gene parameters to a certain degree specified

        new_center_x = int ( self.center[0] + np.random.normal(0,5) )
        new_center_y = int ( self.center[1] + np.random.normal(0,5) )
        new_axes_0 = int ( self.axes[0] + np.random.normal(0,10) )
        new_axes_1 = int ( self.axes[1] + np.random.normal(0,10) )
        new_rotation = int ( self.rotation + np.random.normal(0,5) )

        new_color_r = int ( self.color[0] + np.random.normal(0,5) )
        new_color_g = int ( self.color[1] + np.random.normal(0, 5) )
        new_color_b = int ( self.color[2] + np.random.normal(0, 5) )
        new_alpha = self.alpha + np.random.normal(0, 0.5)

        # Update randomized values
        self.center = ( max ( 0 , min ( self.width , new_center_x ) ) ,
                        max ( 0 , min ( self.height, new_center_y ) ) )

        self.axes =  ( max ( 1 , min ( max( self.width/3, self.height/3 ), new_axes_0 ) ) ,
                       max ( 1,  min ( max( self.width/3, self.height/3 ), new_axes_1) ) )

        self.rotation = max ( 0 , min ( 360 , new_rotation ) )

        self.color = ( max ( 0 , min ( 255 , new_color_r ) ) ,
                       max ( 0 , min ( 255 , new_color_g) ) ,
                       max ( 0 , min ( 255 , new_color_b) ) )

        self.alpha = max ( 0.0 , min ( self.maxopacity , new_alpha ) )