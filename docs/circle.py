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
    def randomize( self , degree ):

        # Produces  variations in gene parameters to a certain degree specified

        var_center_x = int( degree * self.center[0] )
        var_center_y = int( degree * self.center[1] )
        var_radius = int(degree * self.radius )

        var_color_r = int( degree * self.color[0] )
        var_color_g = int(degree * self.color[1] )
        var_color_b = int(degree * self.color[2] )
        var_alpha = degree* self.alpha

        new_center_x = rn.randint( self.center[0] - var_center_x ,
                                   self.center[0] + var_center_x)

        new_center_y = rn.randint(self.center[1] - var_center_y,
                                  self.center[1] + var_center_y)

        new_radius = rn.randint(self.radius - var_radius,
                                self.radius + var_radius)

        new_color_r = rn.randint(self.color[0] - var_color_r,
                                 self.color[0] + var_color_r)

        new_color_g = rn.randint(self.color[1] - var_color_g,
                                 self.color[1] + var_color_g)

        new_color_b = rn.randint(self.color[2] - var_color_b,
                                 self.color[2] + var_color_b)

        new_alpha = rn.uniform(self.alpha - var_alpha,
                               self.alpha + var_alpha)

        # Update randomized values
        self.center = ( max ( 0 , min ( self.width , new_center_x ) ) ,
                        max ( 0 , min ( self.height, new_center_y ) ) )

        self.radius = max ( 1 , min ( 20, new_radius ) )

        self.color = ( max ( 0 , min ( 255 , new_color_r ) ) ,
                       max ( 0 , min ( 255 , new_color_g) ) ,
                       max ( 0 , min ( 255 , new_color_b) ) )

        self.alpha = max ( 0.0 , min ( self.maxopacity , new_alpha ) )

