#!/usr/bin/python
import heapq

def skyline_get_edge_X(buildings) :
    '''
    Critical x axis values in the list of buildings
    Input : list of tuples(buildings)
    Return : Maximum x axis value for the given buildings
    '''
    return list(sorted(set([x for x, y, l in buildings] + [x+l for x, y, l in buildings])))

def belongs_in_X(x, building) :
    '''
    Determine if the building exists on the x axis
    '''
    bx,by,bl = building
    if(bx <= x <= bx+bl) :
      return True
    return False

def highest_at_X(currX, buildings) :
    '''
    Returns
    1. The actual highest building
    2. highest building with left edge
    '''
    prevy = 0
    edge_prevy = 0
    bldg = None
    bldg_edge = None
    for (x,y,l) in buildings :
        if (prevy < y) :
           prevy = y
           bldg = (x,y,l)
        if (currX == x):
           if (edge_prevy < y) :
              edge_prevy = y
              bldg_edge = (x,y,l)

    return bldg,bldg_edge

def add_to_skyline(x, minhp, bldg_highest, bldg_highest_left_edge, res) :
    if (bldg_highest is None):
        return
    (hx,hy,hl) = bldg_highest
    # => The x is the right edge of some building
    # The end of the building and no other building started here
    if (bldg_highest_left_edge is None) :
        if (x == hx+hl):
          while (x >= minhp[0][1]):
           heapq.heappop(minhp)
          res.append((x,hy))
          res.append((x,-minhp[0][0]))
        return

    (lhx,lhy,lhl) = bldg_highest_left_edge
    # if there exists a building that is highest and the highest with left edge at x
    while ( lhx >= minhp[0][1] or hx >= minhp[0][1]) :
        heapq.heappop(minhp)
    if lhy :
        heapq.heappush(minhp, (-lhy, lhx+lhl))

    # => There is a new highest building or there is an end of a building
    if ( res[-1][1] + minhp[0][0] ) :
       if (bldg_highest != bldg_highest_left_edge) :
          # Add the highest point
          res.append((lhx,hy))
          # Add the left lowest point if its dropping down
          res.append((lhx,lhy))
       else :
          # Add the lowest point from where it came up
          res.append((lhx,res[-1][1]))
          # Add the highest point
          res.append((lhx,hy))

def skyline(buildings) :
    list_X = skyline_get_edge_X(buildings)
    #print "list of X in order "
    #print list_X

    skyline_list=[(0,0)]
    minhp = [(0, float("inf"))]
    for x in list_X :
        bldgs_at_X=[]
        for building in buildings:
            if belongs_in_X(x, building) :
                bldgs_at_X.append(building)
        #print "Buildings at X ", x
        #print bldgs_at_X

        bldg_highest, bldg_highest_left_edge = highest_at_X(x, bldgs_at_X)
        add_to_skyline(x, minhp, bldg_highest, bldg_highest_left_edge, skyline_list)

    print skyline_list[1:]


def main() :
    bldgs = [(1,3,2),(0,4,1),(2,3,3),(2,5,2),(4,1,2),(5,2,1)]
    #bldgs = [(2,10,7),(3,15,4),(5,12,7),(15,10,5),(19,8,5)]
    skyline(bldgs)

if __name__ == "__main__" :
    main()
