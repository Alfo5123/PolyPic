import random as rn
import numpy as np


class Quadrilateral(object):
    '''
        Quadrilaterl Class

        A quadrilateral is defined by its vertex coordinates,
        background color and alpha component.
    '''

    def __init__(self, *args):

        # Define parameters for triangle generation

        if len(args) == 3:

            #  Explicit definition with parameters: height , width , max_opacity

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            self.points = ((rn.randint(0, self.width), rn.randint(0, self.height)),
                           (rn.randint(0, self.width), rn.randint(0, self.height)),
                           (rn.randint(0, self.width), rn.randint(0, self.height)),
                           (rn.randint(0, self.width), rn.randint(0, self.height)))

            self.color = (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))
            self.alpha = self.maxopacity * rn.random()

        elif len(args) == 4:

            # Implicit definition by taking: height , width , max_opacity, decoding gene string

            self.height = args[0]
            self.width = args[1]
            self.maxopacity = args[2]

            info = args[3].split('-')
            self.points = ((int(info[0]), int(info[1])),
                           (int(info[2]), int(info[3])),
                           (int(info[4]), int(info[5])),
                           (int(info[6]), int(info[7])))

            self.color = (int(info[8]), int(info[9]), int(info[10]))
            self.alpha = float(info[11])

    def getInfo(self):

        # Retrive information about the object

        return (self.points, self.color, self.alpha)

    def encodeGene(self):

        # Returns a string encoding the gene information

        return ("{0}-{1}-{2}-{3}-{4}-{5}-{6}-{7}-{8}-{9}-{10}-{11}\n".format(self.points[0][0], self.points[0][1],
                                                                   self.points[1][0], self.points[1][1],
                                                                   self.points[2][0], self.points[2][1],
                                                                   self.points[3][0], self.points[3][1],
                                                                   self.color[0], self.color[1],
                                                                   self.color[2], self.alpha))

    def randomize(self):

        # Produces  variations in gene parameters to a certain degree specified

        new_points_x_0 = int(self.points[0][0] + np.random.normal(0, 30))
        new_points_y_0 = int(self.points[0][1] + np.random.normal(0, 30))

        new_points_x_1 = int(self.points[1][0] + np.random.normal(0, 30))
        new_points_y_1 = int(self.points[1][1] + np.random.normal(0, 30))

        new_points_x_2 = int(self.points[2][0] + np.random.normal(0, 30))
        new_points_y_2 = int(self.points[2][1] + np.random.normal(0, 30))

        new_points_x_3 = int(self.points[3][0] + np.random.normal(0, 30))
        new_points_y_3 = int(self.points[3][1] + np.random.normal(0, 30))

        new_color_r = int(self.color[0] + np.random.normal(0, 5))
        new_color_g = int(self.color[1] + np.random.normal(0, 5))
        new_color_b = int(self.color[2] + np.random.normal(0, 5))
        new_alpha = self.alpha + np.random.normal(0, 0.5)

        # Update randomized values
        self.points = ( (max(0, min(self.width, new_points_x_0)),
                       max(0, min(self.height, new_points_y_0))),
                       (max(0, min(self.width, new_points_x_1)),
                       max(0, min(self.height, new_points_y_1))),
                       (max(0, min(self.width, new_points_x_2)),
                       max(0, min(self.height, new_points_y_2))),
                       (max(0, min(self.width, new_points_x_3)),
                        max(0, min(self.height, new_points_y_3))))

        self.color = (max(0, min(255, new_color_r)),
                      max(0, min(255, new_color_g)),
                      max(0, min(255, new_color_b)))

        self.alpha = max(0.0, min(self.maxopacity, new_alpha))
