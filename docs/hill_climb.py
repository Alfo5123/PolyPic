import numpy as np
import cv2
import circle

class HillClimbing(object):
    ''''
           Hill Climbing

           is a mathematical optimization technique which belongs to the family of local search.
           It is an iterative algorithm that starts with an arbitrary solution to a problem,
           then attempts to find a better solution by incrementally changing a single element
           of the solution. If the change produces a better solution, an incremental change
           is made to the new solution, repeating until no further improvements can be found.


           We will consider an initial pool of polygons and we keep adding more polygons as long
           as the total mean squared error is significantly reduced with respect to the target
           image we want to approximate.
    '''

    def __init__(self,iterations,target):

        self.iterations = iterations
        self.target = target
        self.height , self.width = target.shape[:2]


    def fitness(self):

        # Calculate dissimilarity in pictures by MSE

        current = self.write()
        err = np.sum((current.astype("float") - target.astype("float")) ** 2)
        err /= float(current.shape[0] * current.shape[1] * current.shape[2])
        return err


    def run ( self ):

        # Run the hill climbing optimization and print

        #Set white background image
        img = np.zeros((self.height, self.width, 3), np.uint8)
        img[:] = (255, 255, 255)

        solution = []
        img_solution = img.copy()
        img_temp = img.copy()

        min_err = np.sum((img_solution.astype("float") - self.target.astype("float")) ** 2)
        min_err /= float(img_solution.shape[0] * img_solution.shape[1] * img_solution.shape[2])

        # Start iterative optimization ( minimize error )
        for i in range(self.iterations):

            # Add new point to solution
            solution.append(circle.CircleGen(self.height,self.width,0.1) )

            img_cur = img_solution.copy()
            info = solution[-1].getInfo()
            cv2.circle(img_cur, info[0], info[1], info[2], -1)
            cv2.addWeighted(img_cur, info[3], img_solution, 1 - info[3], 0, img_temp )

            # Compute dissimilarity
            err = np.sum((img_temp.astype("float") - self.target.astype("float")) ** 2)
            err /= float(img_temp.shape[0] * img_temp.shape[1] * img_temp.shape[2])

            # If we are reducing overall error, we take this polygon
            if err + 100 < min_err :
                min_err = err
                img_solution = img_temp
            else:
                solution.pop()

            # Print results evolution
            if i % 50 == 0 :
                cv2.imshow("Solution ( Error : " + str( min_err ) + " ) ", img_solution)
                cv2.waitKey(0)









