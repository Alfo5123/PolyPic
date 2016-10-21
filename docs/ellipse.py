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

        # Define parameters for random circle generation

        if len ( args ) == 6 :

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            self.center = ( rn.randint(0, self.width), rn.randint(0, self.height) )
            self.axes =  (  rn.randint(1, max(self.width/3, self.height/3) ) ,
                            rn.randint(1, max(self.width/3, self.height/3) ) )
            self.rotation = rn.randint ( 0 , 360 )


