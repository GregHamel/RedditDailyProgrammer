#[01-07-14] Challenge #147 [Easy] Sport Points
#http://www.reddit.com/r/dailyprogrammer/comments/1undyd/010714_challenge_147_easy_sport_points/

#Checks if a score is possible given a point value system (such as American Football.).
def check_score(score, *points):
    points = set(points)

    for x in range((score//min(points))+1):
        newpoints  = set()
        for a in points:
            if score % a == 0:
                print ("Valid Score")
                return
            for b in points:
                if a+b <= score:
                    newpoints.add(a+b)
        points = points.union(newpoints)

    print("Invalid Score")


check_score(35, 3, 6, 7, 8)
