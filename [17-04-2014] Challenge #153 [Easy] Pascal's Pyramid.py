#[17-04-2014] Challenge #153 [Easy] Pascal's Pyramid
#http://www.reddit.com/r/dailyprogrammer/comments/20l2it/17042014_challenge_153_easy_pascals_pyramid/

known_pyramids = {1:[[0, 1, 0],[0,0,0,0]], 2:[[0, 1, 0], [0,1,1,0],[0,0,0,0,0]]}

def pascal_pyramid(n):
    if n in known_pyramids:
        return known_pyramids[n]
    else:
        pyramid = [[0, 1, 0]]
        for level in range(1,n):
            row = [ ]
            for x in range (0,level+1):

                row.append(pascal_pyramid(n-1)[level-1][x]+\
                           pascal_pyramid(n-1)[level-1][x+1]+\
                           pascal_pyramid(n-1)[level][x+1])

            pyramid.append([0]+row+[0])
    pyramid.append([0]*(n+3))
    known_pyramids[n] = pyramid
    return pyramid

def print_pyramid(p):
    for level in p[:-1]:
        print(level[1:-1])

pyramid1 = pascal_pyramid(14)
print_pyramid(pyramid1)