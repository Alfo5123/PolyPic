import random as rn
import numpy as np


class Quadrilateral(object):
    '''
        Quadrilateral Class

        A quadrilateral is defined by the one vertex,
        the rotation angle, sides lengths,
        background color and alpha component.
    '''

    def __init__(self, *args):

        # Define parameters for triangle generation

        if len(args) == 3:

            #  Explicit definition with parameters: height , width , max_opacity

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            self.angle = rn.randint(0,360)
            self.side_1 = rn.randint(0,30)
            self.side_2 = rn.randint(0,30)

            self.p1 = (rn.randint(0, self.width), rn.randint(0, self.height))

            p2 = ( int ( self.p1[0] + self.side_1 * np.cos( np.pi * self.angle / 180. ) ) ,
                   int ( self.p1[1] + self.side_1 * np.sin( np.pi * self.angle / 180. ) ) )

            p3 = ( int ( self.p1[0] + self.side_2 * np.sin( np.pi * self.angle / 180. ) ) ,
                   int ( self.p1[1] - self.side_2 * np.cos( np.pi * self.angle / 180. ) ) )

            p4 = ( int (  p2[0] + p3[0] - self.p1[0] ),
                   int (  p2[1] + p3[1] - self.p1[1] ) )

            self.points = ( self.p1 , p2 , p4 , p3 )

            self.color = (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))

            self.alpha = self.maxopacity * rn.random()

        elif len(args) == 4:

            # Implicit definition by taking: height , width , max_opacity, decoding gene string

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            info = args[3].split('-')
            self.p1 = ((int(info[0]),(int(info[1]))))
            self.side_1 = int(info[2])
            self.side_2 = int(info[3])
            self.angle = int(info[4] )

            p2 = (int(self.p1[0] + self.side_1 * np.cos(np.pi * self.angle / 180.)),
                  int(self.p1[1] + self.side_1 * np.sin(np.pi * self.angle / 180.)))

            p3 = (int(self.p1[0] + self.side_2 * np.sin(np.pi * self.angle / 180.)),
                  int(self.p1[1] - self.side_2 * np.cos(np.pi * self.angle / 180.)))

            p4 = (int(p2[0] + p3[0] - self.p1[0]),
                  int(p2[1] + p3[1] - self.p1[1]))

            self.points = (self.p1, p2, p4, p3)

            self.color = (int(info[5]), int(info[6]), int(info[7]))
            self.alpha = float(info[8])


    def getInfo(self):

        # Retrive information about the object

        return (self.points, self.color, self.alpha)

    def encodeGene(self):

        # Returns a string encoding the gene information

        return ("{0}-{1}-{2}-{3}-{4}-{5}-{6}-{7}-{8}\n".format(self.p1[0], self.p1[1],
                                                               self.side_1 , self.side_2,
                                                               self.angle,self.color[0],
                                                               self.color[1],self.color[2],
                                                               self.alpha))

    def randomize(self):

        # Produces  variations in gene parameters to a certain degree specified

        new_p_0 = int(self.p1[0] + np.random.normal(0, 30))
        new_p_1 = int(self.p1[1] + np.random.normal(0, 30))

        new_side_1 = int(self.side_1 + np.random.normal(0, 10))
        new_side_2 = int(self.side_2 + np.random.normal(0, 10))

        new_angle = int(self.angle + np.random.normal(0, 30))

        new_color_r = int(self.color[0] + np.random.normal(0, 5))
        new_color_g = int(self.color[1] + np.random.normal(0, 5))
        new_color_b = int(self.color[2] + np.random.normal(0, 5))

        new_alpha = self.alpha + np.random.normal(0, 0.5)

        # Update randomized values

        self.p1 = ( max ( 0 , min ( self.width , new_p_0 ) ) ,
                    max ( 0 , min ( self.height , new_p_1 ) ) )

        self.side_1 = max ( 0 , min ( 50 , new_side_1 ) )
        self.side_2 = max ( 0 , min ( 50 , new_side_2 ) )

        self.angle = max ( 0 , min ( 360 , new_angle ) )

        p2 = (int(self.p1[0] + self.side_1 * np.cos(np.pi * self.angle / 180.)),
              int(self.p1[1] + self.side_1 * np.sin(np.pi * self.angle / 180.)))

        p3 = (int(self.p1[0] + self.side_2 * np.sin(np.pi * self.angle / 180.)),
              int(self.p1[1] - self.side_2 * np.cos(np.pi * self.angle / 180.)))

        p4 = (int(p2[0] + p3[0] - self.p1[0]),
              int(p2[1] + p3[1] - self.p1[1]))

        self.points = (self.p1, p2, p4, p3)

        self.color = (max(0, min(255, new_color_r)),
                      max(0, min(255, new_color_g)),
                      max(0, min(255, new_color_b)))

        self.alpha = max(0.0, min(self.maxopacity, new_alpha))

