#[8/08/2014] Challenge #174 [Hard] Convex Hull Problem
#http://www.reddit.com/r/dailyprogrammer/comments/2cyss3/8082014_challenge_174_hard_convex_hull_problem/
import random

numpoints = 10000
points = [(random.randint(1,10000),(random.randint(1,10000) )) for x in range(numpoints)]


def find_point(points, weight1, weight2):

    best_point = None
    best_score = None
    for p in points:
        score = (p[0]*weight1)+(p[1]*weight2)
        if best_point != None:
            if score > best_score:
                best_score = score
                best_point = p
        if best_point == None:
            best_score = score
            best_point = p

    return best_point

def est_hull(points, complexity):
    weights = [1,0,-1]
    for x in range(1,complexity):
        weightlevel = 1/(2**x)
        weights.append(weightlevel)
        weights.append(-weightlevel)
        weights.append(1-weightlevel)
        weights.append(-1+weightlevel)
    weights = set(weights)

    hull_points = []
    for w in weights:
        for z in weights:
            if abs(w)+abs(z)==1:
                hull_points.append(find_point(points, w,z))


    return set(hull_points)

print(est_hull(points, 10))

