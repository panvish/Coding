# IBM
Skyline
Input - Array of tuples (x,y,l) where x is a location on the x axis, y is height, l is length. Think of x,y,l as a rectangle.

(y-axis)


* * 
| * * *       <-- (1,3,2) i.e. a rectangle/(2 dimensional building) starting at 1, height of 3, length of 2
| *   *
|_*___*__ (x, axis)
0 1 2 3 4

Example input [(1,3,2),(0,4,1),(0,3,3),(2,5,2),(4,1,2),(5,2,1)] <-- buildings

Output should be silhouette of the buildings (2 dimensional) along x axis (road)

Example output [(0,4),(1,4),(1,3),(2,3),(2,5),(3,5),(4,5),(4,1),(5,1),(5,2),(6,2),(6,0)] < non-optimized
               [(0,4),(1,3),(2,5),(4,1),(5,2),(6,0)] <- optimization
    ***          
*** * *
* *** * ***
*     *** *  ***
****************
