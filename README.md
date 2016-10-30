# PolyPic

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)   

An exploration of optimization techniques to reproduce images by the use of polygons.

Inspired on the cool work done by [Michael Fogleman](https://github.com/fogleman/primitive).

# How it works

A *target* image is provided as input. Then, a *source* image is created by drawing a random set of translucent simple shapes in a black canvas. Finally, we run different optimization schemes to minimize the dissimilarity between *source* and *target* images, producing the artistic-ish abstract picture approximation.
 
The goal of the optimization routines explored is to modify parameters of the shapes in *source* image, such as the color or geometric attributes, in order to reduce the overall squared difference of pixel intensities with respect to the *target* image. 

Three routines were considered and implemented to tackle this problem:

- Genetic Algorithm
- Simulated Annealing
- Hill Climbing


# Results

By using just 60 translucent simple shapes (circles, ellipses and triangles, respectively) we recreate the well-known artwork.

<img src="https://github.com/Alfo5123/PolyPic/blob/master/examples/MONA_LISA.jpg" width="425"/> <img src="https://github.com/Alfo5123/PolyPic/blob/master/examples/MONA_LISA_APROX.jpg" width="425"/> 
<img src="https://github.com/Alfo5123/PolyPic/blob/master/examples/MONA_LISA_APROX_2.jpg" width="425"/> <img src="https://github.com/Alfo5123/PolyPic/blob/master/examples/MONA_LISA_APROX_3.jpg" width="425"/> 

<img src="https://github.com/Alfo5123/PolyPic/blob/master/examples/STARRY_NIGHT.jpg" width="425"/> <img src="https://github.com/Alfo5123/PolyPic/blob/master/examples/STARRY_NIGHT_APROX.jpg" width="425"/> 

<img src="https://github.com/Alfo5123/PolyPic/blob/master/examples/LANDSCAPE.jpg" width="425"/> <img src="https://github.com/Alfo5123/PolyPic/blob/master/examples/LANDSCAPE_APROX.jpg" width="425"/> 

