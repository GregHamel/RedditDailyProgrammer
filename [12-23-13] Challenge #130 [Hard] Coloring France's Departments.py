#[12-23-13] Challenge #130 [Hard] Coloring France's Departments
#http://www.reddit.com/r/dailyprogrammer/comments/1tj0kl/122313_challenge_130_hard_coloring_frances/
import random
import copy
import time
import cProfile

data = [x.strip().split() for x in open("challenge130H.txt").readlines()]
verts = [x[0] for x in data[1:]]
connections = [x[1:] for x in data[1:]]

adjacency_list = {k:v for k,v in zip(verts, connections)}
blank_color_list = {k:v for k,v in zip(verts, [None]*len(verts))}

#Greedy Algorithm. Doesn't produce optimal solution
##def greedy_color():
##    largest = (0,0,0)
##    for k,v in adjacency_list.items():
##        if len(v) > largest[2] and color_list[k] == None:
##            largest = (k,v,len(v))
##    print(largest)
##    connections = adjacency_list[largest[0]]
##    for x in range(len(adjacency_list)):
##        bordering = False
##        for y in connections:
##            if y not in color_list:
##                continue
##            if color_list[y] == x:
##                bordering = True
##                break
##        if bordering:
##            continue
##        else:
##            color_list[largest[0]] = x
##            break

##for x in range(len(adjacency_list)):
##    greedy_color()
##    print(color_list)

start=time.time()

#Function assigns a random coloring to the input list.
def random_color(color_list):
    remaining = [x for x,y in color_list.items()]
    random.shuffle(remaining)
    while remaining:
        choice = remaining.pop()
        connections = adjacency_list[choice]
        for x in range(len(adjacency_list)):
            bordering = False
            for y in connections:
                if y not in color_list:
                    continue
                if color_list[y] == x:
                    bordering = True
                    break
            if bordering:
                continue
            else:
                color_list[choice] = x
                break

def check_num_colors(color_list):
    return len(set(v for k,v in color_list.items()))

#Produces n random colorings and returns the best one.
def random_coloring_heuristic(n):
    best_coloring = []
    best_score = len(adjacency_list)
    for test in range(n):
        clist = copy.copy(blank_color_list)
        random_color(clist)
        score = check_num_colors(clist)
        if score < best_score:
            best_score = score
            best_coloring = clist
    return (best_score, best_coloring)

estimate, coloring_guess = random_coloring_heuristic(50000)
print("Number of colors used: ",estimate, coloring_guess)

print(time.time()-start)

##cProfile.run("random_coloring_heuristic(10000)")