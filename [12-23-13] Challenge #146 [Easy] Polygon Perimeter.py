#[12-23-13] Challenge #146 [Easy] Polygon Perimeter
#http://www.reddit.com/r/dailyprogrammer/comments/1tixzk/122313_challenge_146_easy_polygon_perimeter/

import math
def perimiter(n,r):
    print( "{0:.3f}".format(2*n*r*math.sin(math.pi/n)) )

perimiter(5, 3.7)