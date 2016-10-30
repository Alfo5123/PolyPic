import circle
import ellipse
import triangle
import rectangle
import cv2
import numpy as np
import copy

class Refine ( object ):
    ''''
            Refine Class

            This class provides a aid to improve the approximation

    '''


    def __init__( self , iterations, maximprovements , type , source , target ):

        self.iterations = iterations
        self.maximprovements = maximprovements
        self.type = type
        self.source = source
        self.target = target
        self.height, self.width = target.shape[:2]

    def fitness ( self , current ):

            # Calculate dissimilarity between source and target images

            err = np.sum((current.astype("float") - self.target.astype("float")) ** 2)
            err /= float(current.shape[0] * current.shape[1] * current.shape[2])
            return err

    def run ( self ):

        # Succesively add a new polygon that contributes to reduce overall error
        # until stopping criteria is achieved

        min_err = self.fitness( self.source )
        cur = copy.deepcopy( self.source )
        improvements = 0

        for i in range ( self.iterations ):

            next = copy.deepcopy(cur)

            if self.type == 1:

                c = circle.Circle(self.height,self.width, 0.1)
                info = c.getInfo()

                cv2.circle(cur,info[0],  info[1], info[2], -1)
                cv2.addWeighted(cur, info[3], next, 1 - info[3], 0, next)

            elif self.type == 2:

                e = ellipse.Ellipse(self.height,self.width, 0.1)
                info = e.getInfo()

                cv2.ellipse(cur,info[0],info[1],info[2],0,360,info[3],-1)
                cv2.addWeighted(cur, info[4], next, 1 - info[4], 0, next)

            elif self.type == 3:

                t = triangle.Triangle(self.height,self.width, 0.1)
                info = t.getInfo()

                cv2.fillConvexPoly(cur,np.asarray(info[0]), info[1])
                cv2.addWeighted(cur, info[2], next, 1 - info[2], 0, next)

            elif self.type == 4:

                r = rectangle.Rectangle(self.height,self.width, 0.1)
                info = r.getInfo()

                cv2.rectangle(cur,info[0],info[1],info[2],-1)
                cv2.addWeighted(cur , info[3],next, 1-info[3] , 0, next)


            # Compute dissimilarity
            err = self.fitness(next)

            # Update the solution that provides more fitness
            if err < min_err  :
                min_err = err
                improvements = improvements + 1
                cur = copy.deepcopy(next)
                cv2.imwrite("Refine_Error_" + str(i) + "_" + str(min_err) + ".jpg", cur)

            if improvements == self.maximprovements:
                break

