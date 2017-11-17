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

0 -> 4  0 -> 4
1 -> 3  1 -> 3
2 -> 5  2 -> 5
4 -> 1  3 -> 5
5 -> 2  4 -> 1
        5 -> 2

Lets assume we know MAX X = 6 in examples

def skyline_max_X(buildings):
    # This returns the maximum x axis value in the list of buildings
    
def belongs_in_x(building):
    # Determines if the building exists on the x axis AND (it's on the ending edge)

def highest_at_x(buildings):
    # Returns 2 buildings, it could be the same
    # 1. The actual highest building
    # 2. The highest building not on the edge.
    
    
def skyline(buildings):
    for x in range(skyline_max_X(buildings)+1):
        list = []
        for building in buildings:
            if belongs_in_x(building):
               list.append(building)
        # Now figure out the highest building in list
        building_highest, building_highest_not_edge = highest_at_x(list)

1. Load the code on Github
2. Send me a link to Github url
        
        
def skyline(buildings):
    buildings.sort()    // [(0, 3, 3), (0, 4, 1), (1, 3, 2), (2, 5, 2), (4, 1, 2), (5, 2, 1)]
    prevx = 0;
    prevy = 0;
    count = 0;
    for bldg in buildings:
        (x,y,z) = bldg
        if ( prevx == x)
           if (prevy < y)
              prevy = y
        else 
           // Add the tuple (prevx, prevy)to the final result array 
           result[count] = (prevx,prevy)
           //if x value changes
           if ( prevx 
           
